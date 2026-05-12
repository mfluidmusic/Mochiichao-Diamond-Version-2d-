import React, { useState, useEffect, useRef } from 'react';
import { useGameStore } from '../../store/gameStore';
import { MochiiInstance } from '../../lib/types';
import { createMochii, gainExp } from '../../lib/engine';
import { SPECIES_DB } from '../../lib/species';
import { MOVES_DB } from '../../lib/moves';
import { calcTypeMultiplier, TYPES } from '../../lib/constants';

type BattleState = 'START' | 'PLAYER_TURN' | 'ANIMATING' | 'ENEMY_TURN' | 'CAUGHT' | 'VICTORY' | 'DEFEAT' | 'FLED';

export default function BattleView({ enemyId, onLeave }: { enemyId: string | null, onLeave: () => void }) {
  const party = useGameStore(s => s.party);
  const addMochii = useGameStore(s => s.addMochii);
  const gainWallet = useGameStore(s => s.gainWallet);
  const inventory = useGameStore(s => s.inventory);
  const useItemState = useGameStore(s => s.useItem);
  const updatePartyMember = useGameStore(s => s.updatePartyMember);
  const updateDex = useGameStore(s => s.updateDex);

  const [activeIdx, setActiveIdx] = useState(0);
  const playerActive = party[activeIdx];
  const [enemy, setEnemy] = useState<MochiiInstance | null>(null);

  const [bState, setBState] = useState<BattleState>('START');
  const [log, setLog] = useState<{text: string, time: string}[]>([]);
  
  // Ref for log scrolling
  const logRef = useRef<HTMLDivElement>(null);

  const pushLog = (msg: string) => {
    const time = new Date().toLocaleTimeString([], { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
    setLog(prev => [...prev.slice(-15), { text: msg, time }]);
  }

  useEffect(() => {
    if (logRef.current) {
      logRef.current.scrollTop = logRef.current.scrollHeight;
    }
  }, [log]);

  // Init battle
  useEffect(() => {
    if (!enemyId) {
      onLeave();
      return;
    }
    
    // Find first non-fainted party member
    const firstAlive = party.findIndex(p => p.hp > 0);
    if (firstAlive === -1) {
      onLeave();
      return;
    }
    setActiveIdx(firstAlive);

    const level = Math.max(1, party[0].level + Math.floor(Math.random() * 3) - 1);
    const newEnemy = createMochii(enemyId, level);
    if (newEnemy) {
      setEnemy(newEnemy);
      updateDex(enemyId, 'seen');
      pushLog(`A wild ${newEnemy.nickname} appeared!`);
      setTimeout(() => setBState('PLAYER_TURN'), 1000);
    } else {
      onLeave();
    }
  }, []);

  const handleRun = () => {
    pushLog('You fled the battle!');
    setBState('ANIMATING');
    setTimeout(onLeave, 1500);
  }

  const handleCatch = () => {
    if (!enemy) return;
    if (inventory['luigi_cube'] > 0) {
      useItemState('luigi_cube');
      pushLog(`You threw a Luigi Cube!`);
      setBState('ANIMATING');
      
      setTimeout(() => {
        // Simple catch math
        const catchRate = SPECIES_DB[enemy.speciesId].catchRate;
        const hpFactor = (3 * enemy.maxHp - 2 * enemy.hp) / (3 * enemy.maxHp);
        const chance = (catchRate * hpFactor) / 255;
        
        if (Math.random() < chance + 0.3) { // bumped for demo
          pushLog(`Gotcha! ${enemy.nickname} was caught!`);
          addMochii(enemy);
          setBState('CAUGHT');
          setTimeout(onLeave, 2000);
        } else {
          pushLog(`Oh no! The Mochiichao broke free!`);
          setBState('ENEMY_TURN');
        }
      }, 1500);
    } else {
      pushLog('You have no Luigi Cubes!');
    }
  }

  const executeDamage = (attacker: MochiiInstance, defender: MochiiInstance, moveId: string) => {
    const move = MOVES_DB[moveId];
    if (!move || move.cat === 'Status') return { damage: 0, text: `${attacker.nickname} used ${move?.name || 'a move'}!` };

    const aStat = move.cat === 'Physical' ? attacker.stats.atk : attacker.stats.spa;
    const dStat = move.cat === 'Physical' ? defender.stats.def : defender.stats.spd;
    
    let baseDmg = Math.floor( Math.floor( Math.floor(2 * attacker.level / 5 + 2) * move.bp * aStat / dStat ) / 50 ) + 2;
    
    const defenderType1 = SPECIES_DB[defender.speciesId].types[0];
    const defenderType2 = SPECIES_DB[defender.speciesId].types[1];
    
    const typeMult = calcTypeMultiplier(move.type, defenderType1, defenderType2);
    
    const isStab = SPECIES_DB[attacker.speciesId].types.includes(move.type);
    const stabMult = isStab ? 1.5 : 1;
    
    const crit = Math.random() < 0.06 ? 1.5 : 1.0;
    const roll = (85 + Math.random() * 15) / 100;
    
    const finalDmg = Math.floor(baseDmg * typeMult * stabMult * crit * roll);

    let narrative = `${attacker.nickname} used ${move.name}! `;
    if (typeMult > 1) narrative += "It's super effective! ";
    if (typeMult < 1 && typeMult > 0) narrative += "It's not very effective... ";
    if (typeMult === 0) narrative += "It had no effect... ";
    if (crit > 1) narrative += "A critical hit! ";

    return { damage: finalDmg, text: narrative };
  }

  const handlePlayerMove = (moveId: string) => {
    if (!enemy || bState !== 'PLAYER_TURN') return;
    setBState('ANIMATING');

    const result = executeDamage(playerActive, enemy, moveId);
    pushLog(result.text);

    // Update enemy HP
    const newEnemyHp = Math.max(0, enemy.hp - result.damage);
    setEnemy(prev => prev ? { ...prev, hp: newEnemyHp } : null);

    setTimeout(() => {
      if (newEnemyHp <= 0) {
        pushLog(`Enemy ${enemy.nickname} fainted!`);
        
        // Gain Exp
        const expGained = Math.floor((SPECIES_DB[enemy.speciesId].baseExpYield * enemy.level) / 5);
        pushLog(`${playerActive.nickname} gained ${expGained} EXP!`);
        
        const { leveledUp, newLevel } = gainExp(playerActive, expGained);
        if (leveledUp) {
          pushLog(`${playerActive.nickname} grew to Level ${newLevel}!`);
        }
        
        // Persist party state
        updatePartyMember(activeIdx, playerActive);
        
        gainWallet(50);
        pushLog('You found 50 Credits.');

        setBState('VICTORY');
        setTimeout(onLeave, 3000);
      } else {
        setBState('ENEMY_TURN');
      }
    }, 1500);
  }

  // Enemy Turn Effect
  useEffect(() => {
    if (bState === 'ENEMY_TURN' && enemy) {
      setTimeout(() => {
        const randomMove = enemy.moves[Math.floor(Math.random() * enemy.moves.length)];
        const result = executeDamage(enemy, playerActive, randomMove);
        pushLog(result.text);

        const newPlayerHp = Math.max(0, playerActive.hp - result.damage);
        const updatedPlayer = { ...playerActive, hp: newPlayerHp };
        
        // Update local ref & store
        updatePartyMember(activeIdx, updatedPlayer);
        
        setTimeout(() => {
          if (newPlayerHp <= 0) {
            pushLog(`${playerActive.nickname} fainted!`);
            
            // Check for next alive
            const nextIdx = party.findIndex(p => p.hp > 0);
            if (nextIdx !== -1) {
               // Fast auto-switch for demo
               pushLog(`Go! ${party[nextIdx].nickname}!`);
               setActiveIdx(nextIdx);
               setBState('PLAYER_TURN');
            } else {
               pushLog('You have no more Mochiichao. You blacked out!');
               setBState('DEFEAT');
               setTimeout(onLeave, 3000);
            }
          } else {
            setBState('PLAYER_TURN');
          }
        }, 1500);

      }, 1000);
    }
  }, [bState]);

  if (!playerActive || !enemy) return null;

  const playerPct = Math.max(0, (playerActive.hp / playerActive.maxHp) * 100);
  const enemyPct = Math.max(0, (enemy.hp / enemy.maxHp) * 100);

  return (
    <div className="flex-1 flex flex-col bg-black relative">
      {/* 3D-ish Battle Background */}
      <div className="flex-1 relative overflow-hidden" style={{
         background: 'radial-gradient(ellipse at bottom, #112233 0%, #000000 100%)',
         backgroundImage: 'linear-gradient(rgba(0, 255, 204, 0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 255, 204, 0.1) 1px, transparent 1px)',
         backgroundSize: '40px 40px',
         backgroundPosition: 'center bottom',
         transform: 'perspective(500px) rotateX(10deg)',
         transformOrigin: 'bottom'
      }}>
        
        {/* Enemy Sprite & HUD */}
        <div className="absolute top-8 left-8 w-64 bg-slate-900/80 backdrop-blur border border-red-500/50 p-3 rounded transform -rotateX-10">
           <div className="flex justify-between items-end mb-1">
             <div className="font-bold text-white uppercase">{enemy.nickname}</div>
             <div className="text-xs text-slate-400">Lv.{enemy.level}</div>
           </div>
           <div className="h-2 bg-slate-950 rounded overflow-hidden">
             <div className={`h-full ${enemyPct > 50 ? 'bg-teal-400' : enemyPct > 20 ? 'bg-yellow-400' : 'bg-red-400'} transition-all`} style={{ width: `${enemyPct}%`}}></div>
           </div>
        </div>

        <div className="absolute top-20 right-24 w-40 h-40 flex items-end justify-center transform scale-150 drop-shadow-[0_0_20px_rgba(255,0,0,0.5)]">
          {SPECIES_DB[enemy.speciesId]?.pokeApiId ? (
            <img 
              src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/${SPECIES_DB[enemy.speciesId].pokeApiId}.gif`}
              onError={(e) => {
                e.currentTarget.src = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${SPECIES_DB[enemy.speciesId].pokeApiId}.png`;
              }}
              alt={enemy.nickname} 
              className="max-w-full max-h-full pixelated rendering-pixelated"
              style={{ imageRendering: 'pixelated' }}
            />
          ) : (
            <div className="w-32 h-32 bg-slate-800 border-2 border-red-500 rounded-full flex items-center justify-center text-4xl shadow-[0_0_30px_rgba(255,0,0,0.3)]">
              {SPECIES_DB[enemy.speciesId]?.types[0] === 'WATER' ? '💧' : SPECIES_DB[enemy.speciesId]?.types[0] === 'FIRE' ? '🔥' : '🌱'}
            </div>
          )}
        </div>

        {/* Player Sprite & HUD */}
        <div className="absolute bottom-24 right-8 w-64 bg-slate-900/80 backdrop-blur border border-teal-500/50 p-3 rounded transform -rotateX-10">
           <div className="flex justify-between items-end mb-1">
             <div className="font-bold text-white uppercase">{playerActive.nickname}</div>
             <div className="text-xs text-slate-400">Lv.{playerActive.level}</div>
           </div>
           <div className="flex justify-end text-xs text-slate-400 mb-1">
             {Math.ceil(playerActive.hp)} / {playerActive.maxHp}
           </div>
           <div className="h-2 bg-slate-950 rounded overflow-hidden">
             <div className={`h-full ${playerPct > 50 ? 'bg-teal-400' : playerPct > 20 ? 'bg-yellow-400' : 'bg-red-400'} transition-all`} style={{ width: `${playerPct}%`}}></div>
           </div>
        </div>

        <div className="absolute bottom-8 left-20 w-48 h-48 flex items-end justify-center transform scale-[2] drop-shadow-[0_0_20px_rgba(0,255,204,0.5)]">
          {SPECIES_DB[playerActive.speciesId]?.pokeApiId ? (
            <img 
              src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/${SPECIES_DB[playerActive.speciesId].pokeApiId}.gif`}
              onError={(e) => {
                e.currentTarget.src = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/${SPECIES_DB[playerActive.speciesId].pokeApiId}.png`;
              }}
              alt={playerActive.nickname} 
              className="max-w-full max-h-full pixelated rendering-pixelated"
              style={{ imageRendering: 'pixelated' }}
            />
          ) : (
            <div className="w-40 h-40 bg-slate-800 border-2 border-teal-500 rounded-full flex items-center justify-center text-6xl shadow-[0_0_30px_rgba(0,255,204,0.3)]">
              {SPECIES_DB[playerActive.speciesId]?.types[0] === 'WATER' ? '💧' : SPECIES_DB[playerActive.speciesId]?.types[0] === 'FIRE' ? '🔥' : '🌱'}
            </div>
          )}
        </div>
      </div>

      {/* Battle UI Panel */}
      <div className="h-48 bg-slate-950 border-t-2 border-teal-900 flex shrink-0 z-20">
        
        {/* Battle Log */}
        <div 
          ref={logRef}
          className="flex-1 p-4 overflow-y-auto scroll-smooth border-r border-teal-900/50 flex flex-col gap-1 text-sm font-mono text-slate-300"
        >
          {log.map((l, i) => (
            <div key={i} className="animate-fade-in flex gap-2">
              <span className="text-teal-700 shrink-0">[{l.time}]</span>
              <span>&gt; {l.text}</span>
            </div>
          ))}
          {bState === 'START' && <div className="animate-pulse">&gt; Loading combat protocols...</div>}
          {bState === 'ENEMY_TURN' && <div className="animate-pulse">&gt; Awaiting enemy action...</div>}
        </div>

        {/* Action Menu */}
        <div className="flex-1 p-4 grid grid-cols-2 grid-rows-2 gap-2">
          {playerActive.moves.map((mId, i) => {
            const mv = MOVES_DB[mId];
            return (
              <button 
                key={i}
                disabled={bState !== 'PLAYER_TURN'}
                onClick={() => handlePlayerMove(mId)}
                className="bg-slate-900 border border-slate-700 hover:border-teal-400 hover:bg-teal-900/20 disabled:opacity-50 disabled:cursor-not-allowed rounded text-left px-3 py-2 flex flex-col justify-center transition-colors"
              >
                <span className="font-bold text-slate-200">{mv ? mv.name : '-'}</span>
                {mv && <span className="text-xs text-slate-500">PP {playerActive.pp[i]}/{mv.pp} | {TYPES[mv.type]?.name || mv.type}</span>}
              </button>
            )
          })}

          <button 
            disabled={bState !== 'PLAYER_TURN'}
            onClick={handleCatch}
            className="col-span-1 bg-indigo-950/30 border border-indigo-900 hover:border-indigo-400 disabled:opacity-50 rounded text-center font-bold text-indigo-300 transition-colors"
          >
            BAG (CUBE: {inventory['luigi_cube'] || 0})
          </button>

          <button 
            disabled={bState !== 'PLAYER_TURN'}
            onClick={handleRun}
            className="col-span-1 bg-red-950/30 border border-red-900 hover:border-red-400 disabled:opacity-50 rounded text-center font-bold text-red-300 transition-colors"
          >
            FLEE
          </button>
        </div>
      </div>
    </div>
  )
}
