import React, { useState } from 'react';
import { useGameStore } from './store/gameStore';
import { SPECIES_DB } from './lib/species';

// Views
import WorldEngine from './world/WorldEngine';
import BattleView from './components/views/BattleView';
import RosterView from './components/views/RosterView';
import ShopView from './components/views/ShopView';
import IntroSequence from './components/IntroSequence';
import MochiiMindUI from './components/MochiiMindUI';

export type ViewState = 'STARTER_SELECT' | 'WORLD' | 'BATTLE' | 'ROSTER' | 'SHOP' | 'PC';

export default function App() {
  const introCompleted = useGameStore(s => s.introCompleted);
  const completeIntro = useGameStore(s => s.completeIntro);
  const [view, setView] = useState<ViewState>('WORLD');
  
  // Transient state for battle routing
  const [battleEnemyId, setBattleEnemyId] = useState<string | null>(null);

  // MochiiMind toggle
  const [isMindOpen, setIsMindOpen] = useState(false);

  if (!introCompleted) {
    return (
      <IntroSequence 
        onComplete={() => { completeIntro(); setView('WORLD'); }} 
        onEnterWorld={() => { completeIntro(); setView('WORLD'); }} 
      />
    );
  }

  // Hide the global frame if we are in the WORLD, because WORLD renders its own amazing 2.5D massive view.
  if (view === 'WORLD') {
    return (
      <>
        <WorldEngine setView={setView} setBattleEnemy={setBattleEnemyId} />
        {/* Toggle MochiiMind Button */}
        <button 
          onClick={() => setIsMindOpen(!isMindOpen)}
          className="fixed bottom-4 right-4 w-12 h-12 bg-slate-900 border-2 border-teal-500 rounded-full flex items-center justify-center text-teal-400 font-bold z-[100] shadow-[0_0_15px_rgba(20,184,166,0.3)] hover:bg-slate-800 transition-colors"
          title="Open MochiiMind"
        >
          🧠
        </button>
        <div className="z-[101]">
          <MochiiMindUI isOpen={isMindOpen} onClose={() => setIsMindOpen(false)} />
        </div>
      </>
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 text-teal-50 font-mono flex items-center justify-center p-4 selection:bg-teal-500/30">
      <div className="w-full max-w-4xl bg-slate-900 border-2 border-teal-900 rounded-xl overflow-hidden shadow-[0_0_40px_rgba(20,184,166,0.1)] flex flex-col" style={{ height: '800px' }}>
        
        {/* Header */}
        <header className="bg-slate-950 border-b-2 border-teal-900 p-4 flex justify-between items-center z-10 shrink-0">
          <div className="flex items-center gap-4">
            <h1 className="text-xl font-bold text-teal-400 tracking-wider">M. OS // CHRONICLES</h1>
            <div className="text-xs px-2 py-1 bg-teal-950 text-teal-500 rounded border border-teal-900">
              Uplink Active
            </div>
          </div>
          <div className="flex gap-4">
             <button onClick={() => setView('WORLD')} className="text-sm text-slate-400 hover:text-teal-400 uppercase tracking-widest transition-colors">
               [ Return to World ]
             </button>
          </div>
        </header>

        {/* Content Area */}
        <main className="flex-1 relative overflow-hidden flex flex-col">
          {view === 'BATTLE' && <BattleView enemyId={battleEnemyId} onLeave={() => setView('WORLD')} />}
          {view === 'ROSTER' && <RosterView onBack={() => setView('WORLD')} />}
          {view === 'SHOP' && <ShopView onBack={() => setView('WORLD')} />}
        </main>
        
        {/* Toggle MochiiMind Button */}
        <button 
          onClick={() => setIsMindOpen(!isMindOpen)}
          className="fixed bottom-4 right-4 w-12 h-12 bg-slate-900 border-2 border-teal-500 rounded-full flex items-center justify-center text-teal-400 font-bold z-[100] shadow-[0_0_15px_rgba(20,184,166,0.3)] hover:bg-slate-800 transition-colors"
          title="Open MochiiMind"
        >
          🧠
        </button>
        <div className="z-[101]">
          <MochiiMindUI isOpen={isMindOpen} onClose={() => setIsMindOpen(false)} />
        </div>
      </div>
    </div>
  );
}
