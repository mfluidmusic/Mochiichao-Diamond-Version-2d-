import React, { useState } from 'react';
import { spriteSlug, spriteUrl, SpriteView } from '../lib/sprites';

interface Props {
  id?: string | number | null;
  name?: string | null;
  slug?: string | null;
  view?: SpriteView;
  className?: string;
  alt?: string;
  /** Rendered if the species has no sprite or the file fails to load. */
  fallback?: React.ReactNode;
}

/** Original local Mochiichao sprite with a graceful fallback (never hits the network beyond the app itself). */
export default function MochiiSprite({ id, name, slug, view = 'front', className, alt, fallback }: Props) {
  const resolved = spriteSlug({ id, name, slug });
  const [failed, setFailed] = useState(false);
  if (!resolved || failed) return <>{fallback ?? <span className="text-4xl">👾</span>}</>;
  return (
    <img
      src={spriteUrl(resolved, view)}
      alt={alt ?? name ?? resolved}
      onError={() => setFailed(true)}
      className={className ?? 'max-w-full max-h-full pixelated rendering-pixelated'}
      style={{ imageRendering: 'pixelated' }}
      draggable={false}
    />
  );
}
