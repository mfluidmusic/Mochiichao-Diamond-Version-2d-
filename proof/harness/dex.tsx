// Proof-only dex gallery (the game has no dex screen yet). Renders every species
// through the real MochiiSprite component, plus one deliberately missing species
// to show the graceful fallback.
import React from 'react';
import MochiiSprite from '../../src/components/MochiiSprite';
import species from './species.json';

export default function Dex() {
  return (
    <div className="min-h-screen bg-slate-950 text-teal-50 font-mono p-6">
      <h1 className="text-teal-400 text-xl font-bold mb-1">Mochiioteca — original sprite set (proof harness)</h1>
      <p className="text-slate-400 text-xs mb-4">{species.length} species · front (top) / back (bottom) · served from /sprites/mochiichao/* · no external requests</p>
      <div className="grid grid-cols-9 gap-2">
        {(species as any[]).map(s => (
          <div key={s.id} className="bg-slate-900 border border-teal-900 rounded p-1 flex flex-col items-center">
            <div className="w-24 h-24 flex items-center justify-center"><MochiiSprite id={s.id} name={s.name} view="front" /></div>
            <div className="w-24 h-24 flex items-center justify-center"><MochiiSprite id={s.id} name={s.name} view="back" /></div>
            <div className="text-[10px] text-slate-200 truncate w-full text-center">{s.id} {s.name}</div>
            <div className="text-[9px] text-slate-500">{s.elements.join('/')}</div>
          </div>
        ))}
        <div className="bg-slate-900 border border-red-900 rounded p-1 flex flex-col items-center">
          <div className="w-24 h-48 flex items-center justify-center">
            <MochiiSprite id="999" name="Unknownmon" fallback={<div className="w-20 h-20 rounded-full bg-slate-800 border-2 border-red-500 flex items-center justify-center text-3xl">👾</div>} />
          </div>
          <div className="text-[10px] text-red-300">fallback demo</div>
        </div>
      </div>
    </div>
  );
}
