export interface SaveEntry {
  id: string;
  slotId: number;
  timestamp: number;
  type: 'manual' | 'auto';
  label: string;
  data: any; // Serialized GameState
}

export const getSaves = (slotId: number): SaveEntry[] => {
  try {
    const saves = localStorage.getItem(`mochii_saves_${slotId}`);
    return saves ? JSON.parse(saves) : [];
  } catch(e) {
    return [];
  }
};

export const saveGame = (slotId: number, type: 'manual' | 'auto', label: string, gameState: any) => {
  const saves = getSaves(slotId);
  const newSave: SaveEntry = {
    id: crypto.randomUUID(),
    slotId,
    timestamp: Date.now(),
    type,
    label,
    data: gameState
  };

  let updatedSaves = [newSave, ...saves];
  
  if (type === 'auto') {
    // Keep only the newest autosave
    const autosaves = updatedSaves.filter(s => s.type === 'auto');
    if (autosaves.length > 1) {
       updatedSaves = updatedSaves.filter(s => s.id !== autosaves[autosaves.length - 1].id);
    }
  } else {
    // Keep up to 8 manual saves
    const manuals = updatedSaves.filter(s => s.type === 'manual');
    if (manuals.length > 8) {
       updatedSaves = updatedSaves.filter(s => s.id !== manuals[manuals.length - 1].id);
    }
  }

  localStorage.setItem(`mochii_saves_${slotId}`, JSON.stringify(updatedSaves));
  return newSave;
};

export const loadGame = (saveEntry: SaveEntry, loadZustandState: (state: any) => void) => {
  loadZustandState(saveEntry.data);
};

export const getSlotSummaries = () => {
  return [1, 2, 3].map(slotId => {
    const saves = getSaves(slotId);
    if (saves.length === 0) return null;
    const latest = saves.map(s => s).sort((a,b) => b.timestamp - a.timestamp)[0];
    return {
      slotId,
      player: latest.data.playerName || "Netrunner",
      map: latest.data.currentMap,
      hms: latest.data.badges.length, // using badges as an indicator
      timestamp: latest.timestamp
    };
  });
};
