import React from 'react';
import { useGameStore } from '../../store/gameStore';

export default function ShopView({ onBack }: { onBack: () => void }) {
  const wallet = useGameStore(s => s.wallet);
  const inventory = useGameStore(s => s.inventory);
  const buyItem = useGameStore(s => s.buyItem);

  const shopItems = [
    { id: 'luigi_cube', name: 'Luigi Cube', cost: 250, desc: 'A sketchy syndicate-brand capture device.' },
    { id: 'mend_patch', name: 'Mend Patch', cost: 150, desc: 'Restores 50 HP.' },
    { id: 'revive_core', name: 'Revive Core', cost: 500, desc: 'Reboots a fainted Mochiichao to 50% capacity.' },
  ];

  const handleBuy = (id: string, cost: number) => {
    if (buyItem(id, cost)) {
      // success
    } else {
      alert('Insufficient funds for this purchase.');
    }
  }

  return (
    <div className="flex-1 flex flex-col p-6 overflow-hidden">
      <div className="flex justify-between items-end mb-6">
        <div>
          <button onClick={onBack} className="text-teal-500 hover:text-white mb-2 font-bold text-sm bg-slate-800 px-3 py-1 rounded">
            ← LEAVE SHOP
          </button>
          <h2 className="text-2xl font-bold text-teal-400">Syndicate Kiosk</h2>
          <p className="text-sm text-slate-500">"No returns, no refunds." - Luigi</p>
        </div>
        <div className="bg-slate-900 border border-teal-800 px-4 py-2 rounded text-teal-300 font-bold">
          Credits: {wallet}
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 flex-1 overflow-hidden">
        {/* Shop Listing */}
        <div className="flex flex-col gap-3 overflow-y-auto">
          {shopItems.map(item => (
            <div key={item.id} className="bg-slate-900 border border-slate-700 p-4 rounded flex justify-between items-center hover:border-teal-700 transition-colors">
               <div>
                 <div className="font-bold text-slate-200">{item.name}</div>
                 <div className="text-xs text-slate-500 mt-1">{item.desc}</div>
               </div>
               <div className="flex flex-col items-end gap-2">
                 <div className="text-sm font-mono text-teal-500">{item.cost} CR</div>
                 <button 
                   onClick={() => handleBuy(item.id, item.cost)}
                   className="bg-slate-800 hover:bg-teal-900 text-teal-400 text-xs px-3 py-1 rounded transition-colors"
                 >
                   Purchase
                 </button>
               </div>
            </div>
          ))}
        </div>

        {/* Current Inventory */}
        <div className="bg-slate-900 border border-slate-800 rounded-lg p-6 flex flex-col">
          <h3 className="text-lg font-bold text-slate-300 mb-4 border-b border-slate-800 pb-2">Your Inventory</h3>
          <div className="flex-1 overflow-y-auto flex flex-col gap-2">
            {Object.keys(inventory).length === 0 && <div className="text-sm text-slate-600 italic">Inventory empty</div>}
            
            {Object.entries(inventory).map(([id, count]) => {
              if (count <= 0) return null;
              const details = shopItems.find(i => i.id === id);
              return (
                <div key={id} className="flex justify-between items-center text-sm border-b border-slate-800/50 pb-2">
                  <span className="text-slate-300">{details?.name || id}</span>
                  <span className="text-teal-500 font-mono">x{count}</span>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  )
}
