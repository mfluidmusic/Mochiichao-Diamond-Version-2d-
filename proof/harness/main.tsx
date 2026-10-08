// Proof harness (screenshots only). Seeds the game store and renders a single
// real game view so headless Chromium can capture it. Not part of the game build.
import React from 'react';
import { createRoot } from 'react-dom/client';
import '../../src/index.css';
import { useGameStore } from '../../src/store/gameStore';
import { createMochii } from '../../src/lib/engine';
import BattleView from '../../src/components/views/BattleView';
import RosterView from '../../src/components/views/RosterView';
import WorldEngine from '../../src/world/WorldEngine';
import { FULL_WORLD } from '../../src/world/FullWorldMaps';
import Dex from './dex';

const q = new URLSearchParams(location.search);
const view = q.get('view') || 'battle';
const party = (q.get('party') || '001').split(',');
const enemy = q.get('enemy') || '004';

const members = party.map((id, i) => createMochii(id, 12 + i * 3)!).filter(Boolean);
let mapId = 'route1';
let pos = { x: 14, y: 37 };
if (view === 'world') {
  // find a tall-grass tile (6) with a grass neighbour to the right on a map with encounters
  outer: for (const [id, m] of Object.entries(FULL_WORLD)) {
    if (!m.encounters?.length || !m.tiles) continue;
    for (let y = 0; y < m.tiles.length; y++) for (let x = 0; x < m.tiles[y].length - 1; x++) {
      if (m.tiles[y][x] === 6 && m.tiles[y][x + 1] === 6) { mapId = id; pos = { x, y }; break outer; }
    }
  }
  (window as any).__grass = { mapId, pos };
}
useGameStore.setState({ introCompleted: true, party: members, currentMap: mapId, playerPos: pos,
  completedEvents: ['hex_battle_event', 'prof_speech_event'] });

function Frame({ children }: { children: React.ReactNode }) {
  return <div className="min-h-screen bg-slate-950 text-teal-50 font-mono flex items-center justify-center p-4">
    <div className="w-full max-w-4xl bg-slate-900 border-2 border-teal-900 rounded-xl overflow-hidden flex flex-col" style={{ height: 800 }}>
      <main className="flex-1 relative overflow-hidden flex flex-col">{children}</main></div></div>;
}
const el = view === 'dex' ? <Dex />
  : view === 'roster' ? <Frame><RosterView onBack={() => {}} /></Frame>
  : view === 'world' ? <WorldEngine setView={() => {}} setBattleEnemy={() => {}} />
  : <Frame><BattleView enemyId={enemy} onLeave={() => {}} /></Frame>;
createRoot(document.getElementById('root')!).render(el);
