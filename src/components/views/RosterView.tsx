import React from 'react';
import { useGameStore } from '../../store/gameStore';
import { SPECIES_DB } from '../../lib/species';
import SpriteGenerator from '../SpriteGenerator';

export default function RosterView({ onBack }: { onBack: () => void }) {
  const party = useGameStore(s => s.party);

  return (
    <div className="flex-1 flex flex-col p-6 overflow-hidden relative">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-teal-400">Active Roster</h2>
        <button 
          onClick={onBack}
          className="bg-slate-800 hover:bg-slate-700 text-slate-300 px-4 py-2 rounded text-sm tracking-widest font-bold uppercase transition-colors"
        >
          ✕ Close
        </button>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 overflow-y-auto">
        {party.map((mochii, i) => {
          const species = SPECIES_DB[mochii.speciesId];
          const pct = Math.max(0, (mochii.hp / mochii.maxHp) * 100);
          const isFainted = mochii.hp <= 0;
          
          return (
            <div key={mochii.id} className={`bg-slate-900 border ${isFainted ? 'border-red-900 opacity-70' : 'border-teal-900'} p-4 rounded-lg flex flex-col`}>
              <div className="flex justify-between items-start mb-4">
                <div className="flex min-w-0">
                  <div className="w-16 h-16 mr-3 bg-slate-950 rounded border border-slate-800 flex items-center justify-center shrink-0">
                    {species.pokeApiId ? (
                      <img 
                        src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${species.pokeApiId}.png`}
                        alt={mochii.nickname}
                        className="max-w-full max-h-full pixelated rendering-pixelated"
                        style={{ imageRendering: 'pixelated' }}
                      />
                    ) : (
                      <span className="text-2xl">{species.types[0] === 'WATER' ? '💧' : species.types[0] === 'FIRE' ? '🔥' : '🌱'}</span>
                    )}
                  </div>
                  <div className="min-w-0">
                    <div className="font-bold text-lg text-slate-100 flex items-center gap-2 truncate">
                      {mochii.nickname} 
                      {mochii.status && <span className="bg-purple-900 text-purple-300 text-[10px] px-1 rounded shrink-0">{mochii.status}</span>}
                    </div>
                    <div className="text-xs text-slate-500 truncate">Lv. {mochii.level} {species.name}</div>
                    <div className="flex gap-1 mt-1">
                      {species.types.map(t => (
                        <span key={t} className="text-[10px] bg-slate-800 text-slate-400 px-1 rounded">{t}</span>
                      ))}
                    </div>
                  </div>
                </div>
                
                <div className="text-right shrink-0 ml-2">
                  <div className="text-xs text-slate-400 mb-1">HP {Math.ceil(mochii.hp)}/{mochii.maxHp}</div>
                  <div className="w-24 h-2 bg-slate-950 rounded overflow-hidden">
                    <div 
                      className={`h-full ${pct > 50 ? 'bg-teal-500' : pct > 20 ? 'bg-yellow-500' : 'bg-red-500'} transition-all`}
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-2 mt-auto">
                {mochii.moves.map((m, j) => (
                  <div key={j} className="bg-slate-950/50 border border-slate-800 p-2 rounded text-xs">
                     <div className="text-slate-300 truncate">{m.replace(/_MOVE/g, '').replace(/_/g, ' ')}</div>
                     <div className="text-slate-500">PP {mochii.pp[j]}/{mochii.pp[j]}</div>
                  </div>
                ))}
              </div>
            </div>
          )
        })}
      </div>
      <div className="mt-6 shrink-0 z-10 w-full mb-12">
        <SpriteGenerator />
      </div>
    </div>
  )
}
