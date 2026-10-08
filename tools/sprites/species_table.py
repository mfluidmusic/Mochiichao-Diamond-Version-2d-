"""Merged Mochiichao species table (single source of truth for the sprite set).

Sources merged (abbreviations used in `src`):
  ST  = src/lib/species.ts          (the game's live SPECIES_DB)
  GR  = src/lib/global_roster.json  (canon roster 001-046 + 331; elements + api_search_tags)
  GD  = src/world/GameData.ts       (starter / mochiichao list with colors + descriptions)
  MD  = owner Drive doc mochiichao-diamond.jsx      (SPECIES, colors + desc)
  BS  = owner Drive doc MochiichaoBattleSystem.jsx  (SPECIES_DB 1-10, colors)
  WM  = owner Drive doc mochiichao-world-map.jsx    (encounter/trainer tables)
  DIW = mhvnsnt/Dream-Infinite-World src/components/MochiichaoCanvas.tsx
Where sources disagree, every value is kept (types_game vs elements vs alt_types).
"""

def S(id, name, elements, desc, colors, evo=None, prev=None, types_game=None, alt_types=None,
      aliases=(), src=(), stage=1, tags=()):
    return dict(id=id, name=name, aliases=list(aliases), elements=elements, types_game=types_game or [],
                alt_types=alt_types or [], description=desc, colors=colors, evolves_to=evo, evolves_from=prev,
                stage=stage, sources=list(src), tags=list(tags))

SPECIES = [
 S("001","Mochii",["Aqua"],"A small, soft, wave-patterned creature that bounces to move and absorbs moisture from the air to power itself.",
   ["#4fc3f7","#2a86b0","#e6f9ff"],evo=("002",16),types_game=["WATER"],alt_types=["Water"],src=["ST","GR","GD","MD","WM"],stage=1,
   tags=["blue water slime","cute bouncy ball","bloop"]),
 S("002","Tiidebiite",["Aqua","Mythic"],"It has learned to control the flow of water as a martial art; its fists are wrapped in swirling water.",
   ["#3fb6d3","#1a2f6e","#e6f9ff"],evo=("003",36),prev="001",types_game=["WATER","FIGHTING"],src=["ST","GR"],stage=2,
   tags=["water warrior","blue martial artist","swirling water fists"]),
 S("003","Aquari-OS",["Aqua","Mythic"],"The supreme fluid intelligence: a floating aqua brain and mythical water guardian.",
   ["#01579b","#4fc3f7","#e6f9ff"],prev="002",types_game=["WATER","PSYCHIC"],alt_types=["Water"],aliases=["AquariiOS"],src=["ST","GR","GD"],stage=3,
   tags=["fluid intelligence","floating aqua brain","mythical water guardian"]),
 S("004","Razorgater",["Chrome"],"A small crocodile with metallic scales; razor-edged chrome plating deflects data attacks.",
   ["#90a4ae","#b0bec5","#2dd4bf"],evo=("005",18),types_game=["WATER","STEEL"],alt_types=["Chrome"],src=["ST","GR","GD","MD","BS","WM"],stage=1,
   tags=["small metallic crocodile","chrome jaws","silver lizard"]),
 S("005","Chromedile",["Chrome","Strike"],"A bipedal chrome crocodile with sharp steel teeth. Its chrome hide reflects all light, helping it hunt in shadows.",
   ["#cfd8dc","#262636","#7e57c2"],evo=("006",30),prev="004",types_game=["STEEL","DARK"],aliases=["Chromejaww"],src=["ST","GR","WM"],stage=2,
   tags=["bipedal chrome crocodile","sharp steel teeth","fierce metal reptile"]),
 S("006","Reaperdile",["Chrome","Strike"],"A huge walking tank engineered for destruction, armored in steel blades.",
   ["#4f5b66","#1b5e20","#7dff9a"],prev="005",types_game=["STEEL","DRAGON"],alt_types=["Earth"],src=["ST","GR","GD"],stage=3,
   tags=["huge walking tank crocodile","steel armor blades","metal monster destruction"]),
 S("007","Tyrage",["Core"],"A tiny dinosaur made of packed earth; its footsteps leave glowing cracks in digital terrain.",
   ["#9a6b42","#81c784","#c79a6b"],evo=("008",16),types_game=["GROUND"],alt_types=["Earth","Flame (BS)"],src=["ST","GR","GD","MD","BS","WM"],stage=1,
   tags=["tiny earth dinosaur","rocky ground dino","mud lizard"]),
 S("008","Duneclaw",["Core","Umbral"],"A desert dinosaur that wears a bone mask and hunts in the dunes.",
   ["#d4a35a","#3a2160","#e6dcc4"],evo=("009",34),prev="007",types_game=["GROUND","ROCK"],src=["ST","GR"],stage=2,
   tags=["desert dinosaur","bone mask dinosaur","dark earth beast"]),
 S("009","Oblivirex",["Core","Umbral"],"The apex predator fossilized into code: a black-boned shadow tyrant.",
   ["#262636","#e6dcc4","#b26cff"],prev="008",types_game=["GROUND","GHOST"],src=["ST","GR"],stage=3,
   tags=["fossilized dark code tyrannosaurus rex","black bone trex","shadow earth monster"]),
 S("010","Kittember",["Beast","Flame"],"A fiery little feline that slips through shadows with uncanny grace.",
   ["#ce93d8","#705898","#ff9a2e"],evo=("011",14),types_game=["FIRE"],alt_types=["Umbral"],src=["ST","GR","GD","MD","BS","WM"],stage=1,
   tags=["fiery red kitten","flame paws","cute fire cat"]),
 S("011","Pyropaw",["Beast","Flame"],"A fiery tiger cub whose stripes burn like flames.",
   ["#ce93d8","#705898","#ff9a2e"],evo=("012",34),prev="010",src=["GR"],stage=2,tags=["fiery tiger cub","flame stripes","fire beast cat"]),
 S("012","Manticlaw",["Beast","Flame"],"A huge fire manticore with a blazing mane and flaming wings.",
   ["#a98ccf","#3a2160","#ff9a2e"],prev="011",src=["GR"],stage=3,tags=["huge fire manticore","blazing mane beast","flaming wings cat"]),
 S("013","Pupbble",["Beast","Earth"],"A small puppy with a coat of pebbles.",
   ["#ffcc80","#8a857b","#c2884a"],evo=("014",16),alt_types=["Core"],src=["GR","GD","MD","WM"],stage=1,tags=["small rock puppy","stone dog","pebble puppy"]),
 S("014","Terradog",["Beast","Earth"],"An earth hound wearing natural rock armor.",
   ["#e0a868","#8a857b","#5a5650"],evo=("015",32),prev="013",src=["GR"],stage=2,tags=["earth hound","rock armor dog","ground terrier"]),
 S("015","Quakehound",["Beast","Earth"],"A massive earthquake mastiff bristling with stone spikes.",
   ["#c2884a","#5a5650","#ffcc80"],prev="014",src=["GR"],stage=3,tags=["massive earthquake mastiff","stone spikes dog","heavy rock beast"]),
 S("016","Squirmite",["Bug","Silk"],"A small white silkworm that squirms through the grass.",
   ["#e8e4d0","#c5e1a5","#2dd4bf"],evo=("017",7),alt_types=["Bug"],src=["GR","GD","MD","WM"],stage=1,tags=["small white silkworm","cute squirming bug","caterpillar"]),
 S("017","Cocoonode",["Bug","Silk"],"A green silk cocoon laced with glowing digital nodes.",
   ["#c5e1a5","#7a9a4a","#2dffd2"],evo=("018",10),prev="016",alt_types=["Bug"],src=["GR","GD"],stage=2,tags=["green silk cocoon","digital node cocoon","chrysalis"]),
 S("018","Mothrix",["Bug","Silk"],"A beautiful matrix moth with glowing neon wings of digital silk.",
   ["#141420","#39ff7a","#e8e4d0"],prev="017",src=["GR"],stage=3,tags=["beautiful matrix moth","glowing neon wings bug","digital silk moth"]),
 S("019","Zephling",["Aero","Wind"],"A tiny, breezy wind bird.",
   ["#b3e5fc","#4f8fb8","#ffffff"],evo=("020",16),alt_types=["Aero"],src=["GR","GD","MD","BS","WM"],stage=1,tags=["tiny wind bird","breezy sparrow","flying chick"]),
 S("020","Aerobeak",["Aero","Wind"],"A sleek, aerodynamic wind falcon.",
   ["#7cc4ec","#ffffff","#2b3850"],evo=("021",34),prev="019",src=["GR"],stage=2,tags=["sleek wind falcon","aerodynamic bird","flying raptor"]),
 S("021","Stormtalon",["Aero","Wind"],"A massive storm eagle with lightning talons; its wingbeats raise hurricanes.",
   ["#4a5d7e","#f6ff4a","#b3e5fc"],prev="020",src=["GR"],stage=3,tags=["massive storm eagle","lightning talons","hurricane bird"]),
 S("022","Finblade",["Aqua","Chrome"],"A sharp swordfish with chrome fins.",
   ["#cfd8dc","#3fb6d3","#5b6875"],evo=("023",30),src=["GR"],stage=1,tags=["sharp swordfish","chrome fin shark","metal fish"]),
 S("023","Megalochrome",["Aqua","Chrome"],"A giant chrome megalodon, a metallic torpedo of steel.",
   ["#90a4ae","#2dd4bf","#232a33"],prev="022",src=["GR"],stage=2,tags=["giant chrome megalodon","steel shark monster","metallic torpedo fish"]),
 S("024","Floatcalf",["Aqua","Neon"],"A cute floating whale calf with glowing neon spots.",
   ["#1a237e","#ff4fb0","#f6ff4a"],evo=("025",38),src=["GR"],stage=1,tags=["cute floating calf whale","glowing neon spots whale","bubble aqua mammal"]),
 S("025","Astroleviathan",["Aqua","Neon"],"A massive cosmic whale; fishermen say something enormous moves below the harbor.",
   ["#121a5e","#ff4fb0","#f6ff4a"],prev="024",src=["GR","MD"],stage=2,tags=["massive cosmic whale","glowing neon galactic leviathan","space ocean whale"]),
 S("026","Inklet",["Aqua","Umbral"],"A small dark squid made of shadow ink.",
   ["#262636","#80deea","#ffffff"],evo=("027",22),alt_types=["Water"],src=["GR","GD"],stage=1,tags=["small dark squid","shadow ink octopus","black water blob"]),
 S("027","Toxitacle",["Aqua","Umbral"],"A poisonous dark octopus with venomous tentacles.",
   ["#9a4ac0","#39ff7a","#262636"],evo=("028",40),prev="026",src=["GR"],stage=2,tags=["poisonous dark octopus","venomous tentacles","purple toxic squid"]),
 S("028","Krakenox",["Aqua","Umbral"],"A giant shadow kraken, the abyssal nightmare of the deep sea.",
   ["#1a237e","#2dffd2","#060a24"],prev="027",alt_types=["Deep"],src=["GR","GD","MD"],stage=3,tags=["giant shadow kraken","abyssal nightmare octopus","dark sea monster"]),
 S("029","Punchkid",["Core","Strike"],"A tiny fighting kid in oversized boxing gloves.",
   ["#ffab91","#2dd4bf","#1a2f6e"],evo=("030",20),alt_types=["Strike"],src=["GR","GD","MD"],stage=1,tags=["tiny fighting kid","boxing gloves fighter","martial arts child"]),
 S("030","Strikechamp",["Core","Strike"],"A muscular champion boxer and fighting master.",
   ["#ffab91","#2dd4bf","#ffd700"],evo=("031",35),prev="029",src=["GR"],stage=2,tags=["champion boxer","muscular martial artist","fighting master"]),
 S("031","Kickmaster",["Core","Strike"],"A champion kickboxer with deadly kicking martial arts.",
   ["#ffab91","#2dd4bf","#141420"],prev="030",src=["GR"],stage=3,tags=["champion kickboxer","deadly kicking martial arts","karate master"]),
 S("032","Gearkid",["Chrome","Core"],"A small clockwork robot child built around a steel cog.",
   ["#b0bec5","#ff9a2e","#5b6875"],evo=("033",24),alt_types=["Chrome"],src=["GR","GD","MD","BS"],stage=1,tags=["small gear robot","steel cog child","clockwork kid"]),
 S("033","Mechapion",["Chrome","Core"],"A heavy steel-armored automaton with piston arms.",
   ["#90a4ae","#ff9a2e","#323b45"],evo=("034",42),prev="032",src=["GR"],stage=2,tags=["heavy mechanic robot","steel armored machine","piston arms automaton"]),
 S("034","Gorokappa",["Chrome","Core"],"A massive mecha gorilla powered by steam: a giant mechanical kaiju.",
   ["#4f5b66","#ff9a2e","#cfd8dc"],prev="033",src=["GR"],stage=3,tags=["massive mecha gorilla","steel steam ape","giant mechanical kaiju"]),
 S("035","Pebblefist",["Core","Chrome"],"A gravel puncher with stone hands.",
   ["#8a857b","#cfd8dc","#2dd4bf"],evo=("036",25),src=["GR"],stage=1,tags=["rock fists","stone hands golem","gravel puncher"]),
 S("036","Cragarm",["Core","Chrome"],"A craggy stone giant with boulder arms.",
   ["#8a857b","#cfd8dc","#5a5650"],evo=("037",40),prev="035",src=["GR"],stage=2,tags=["boulder arms golem","craggy stone giant","rock monster"]),
 S("037","Terrapod",["Core","Chrome"],"A colossal mountain golem, an impenetrable stone titan with earthquake fists.",
   ["#5a5650","#cfd8dc","#81c784"],prev="036",src=["GR"],stage=3,tags=["colossal mountain golem","earthquake fists giant","impenetrable stone titan"]),
 S("038","Sproutle",["Flora","Chrome"],"A little plant turtle that sprouts data-leaves from its chrome-plated back to photosynthesize power.",
   ["#a5d6a7","#90a4ae","#5aa85a"],evo=("039",18),types_game=["GRASS"],alt_types=["Earth"],src=["ST","GR","MD","WM"],stage=1,
   tags=["grassy plant turtle","sprout shell tortoise","chrome leaf reptile"]),
 S("039","Shellguard",["Flora","Chrome"],"An armored bush turtle with a steel shell that guards the grove.",
   ["#5aa85a","#90a4ae","#a5d6a7"],evo=("040",32),prev="038",src=["GR"],stage=2,tags=["armored bush turtle","steel shell tortoise","grove defense turtle"]),
 S("040","Dreadtoise",["Flora","Chrome"],"A fortress: a massive dreadnought tortoise with a steel shell covered in moss.",
   ["#546e7a","#37474f","#5aa85a"],prev="039",types_game=["GRASS","STEEL"],alt_types=["Core"],src=["ST (as 039)","GR","GD","MD","BS"],stage=3,
   tags=["massive dreadnought tortoise","steel forest titan shell","chrome tree turtle"]),
 S("041","Pixilite",["Flora"],"A tiny floating digital flower sprite that glows like a neon leaf.",
   ["#39ff7a","#ff4fb0","#f6ff4a"],src=["GR"],stage=1,tags=["tiny digital flower sprite","floating pixel fairy","glowing neon leaf"]),
 S("042","Wispkin",["Umbral"],"A floating dark wisp, a spooky little shadow spirit.",
   ["#b39ddb","#3a2160","#e9e0ff"],evo=("043",28),alt_types=["Umbral"],src=["GR","GD","BS"],stage=1,tags=["floating dark wisp","shadowy soul ghost","spooky little spirit"]),
 S("043","Duskfiend",["Umbral"],"A terrifying dusk phantom: a tall shadow fiend.",
   ["#3a2160","#140a24","#2dffd2"],prev="042",src=["GR"],stage=2,tags=["terrifying dusk phantom","tall shadow fiend","creepy grim ghost"]),
 S("044","Ashemit",["Flame","Mythic"],"A little ash hermit, a smoldering mythical child that keeps a spark alive.",
   ["#8a857b","#ff9a2e","#3a3428"],evo=("045",25),src=["GR"],stage=1,tags=["little ash demon","spark hermit","smoldering mythical child"]),
 S("045","Pyromonk",["Flame","Mythic"],"A fire martial monk who fights with a burning staff.",
   ["#f08030","#8a857b","#ffd700"],evo=("046",40),prev="044",src=["GR"],stage=2,tags=["fire martial monk","burning staff ascetic","flame meditating fighter"]),
 S("046","Yogiferno",["Flame","Mythic"],"An enlightened inferno deity that floats in meditation, wrapped in a flaming aura.",
   ["#ff9a2e","#b8420f","#ffd700"],prev="045",src=["GR"],stage=3,tags=["enlightened inferno deity","floating lava god","flaming aura mythical master"]),
 S("331","Mythar",["Mythic"],"The divine celestial creator, the almighty mythical origin of all Mochiichao.",
   ["#ffd700","#fffaf0","#7e57c2"],alt_types=["Mythic"],src=["GR","GD","MD"],stage=1,tags=["divine celestial creator","glowing ethereal legendary","almighty mythical origin god"]),
 # ---- species that only exist in the owner's Drive battle-system doc (no global id) ----
 S("BS-02","Emburrn",["Flame"],"A fire starter from the battle-system prototype: a burrowing ember creature that smokes and spins fire.",
   ["#F08030","#262636","#ffc061"],src=["BS"],tags=["ember","burrow","smokescreen","fire spin"]),
 S("BS-03","Aquabble",["Aqua"],"A water starter from the battle-system prototype that withdraws into a protective bubble.",
   ["#6890F0","#d4f7fc","#1a2f6e"],src=["BS"],tags=["bubble","withdraw","bubble beam"]),
 # ---- Dream-Infinite-World MochiichaoCanvas.tsx ----
 S("DIW-01","Mochling",["Neon"],"The player partner of the Dream world: a pink, big-eared mochi creature that wanders the neon forest and fights with a data blade (Signature Slam).",
   ["#ff66cc","#2dffd2","#cccc00"],src=["DIW"],tags=["pink body","two big ears","sword"]),
 S("DIW-02","Glitch-Mochi",["Neon","Umbral"],"A corrupted mochi creature that patrols the neon forest and drops crystalline data shards (Byte Chomp).",
   ["#22ff99","#ff2a6d","#141420"],src=["DIW"],tags=["green body","glitch","data shards"]),
 S("DIW-03","Neon Stalker",["Neon","Umbral"],"A wild enemy of the neon forest that hunts from the shadows.",
   ["#141420","#ff4fb0","#2dffd2"],src=["DIW"],tags=["stalker","neon"]),
 S("DIW-04","Ragdoll Brute",["Core"],"A hulking, stitched-together wild brute of the Dream world.",
   ["#c2884a","#7e57c2","#e6dcc4"],src=["DIW"],tags=["ragdoll","brute"]),
 S("DIW-05","Dream Cruncher",["Mythic","Neon"],"A legendary boss said to await those who hoard enough data; it crunches whole worlds into shards.",
   ["#323b45","#ff2a6d","#2dffd2"],src=["DIW"],tags=["legend","data hoard","cruncher"]),
]

def slug(name):
    import re
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def lines():
    """evolution lines as lists of ids (roster json order)."""
    by = {s['id']: s for s in SPECIES}
    out, seen = [], set()
    for s in SPECIES:
        if s['evolves_from'] or s['id'] in seen: continue
        line = [s['id']]
        cur = s
        while cur['evolves_to']:
            nxt = cur['evolves_to'][0]; line.append(nxt); cur = by[nxt]
        seen.update(line); out.append(line)
    return out
