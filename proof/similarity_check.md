# Originality check vs 649 reference sprites (Gen 1-5 Pokemon fronts, not stored in repo)

score = 0.6*silhouette IoU + 0.4*palette similarity (identical sprite = 1.0).

Calibration (measured): for 120 random Pokemon, the score to their *nearest other* Pokemon has median 0.733, p10 0.645, p90 0.795, max 0.850. So a Mochiichao sprite scoring <= ~0.8 is no closer to any Pokemon than two different Pokemon are to each other. This is a coarse automated screen, not a legal opinion; it was used together with a by-eye review against the 12 formerly mapped Pokemon.

| Mochiichao | closest reference | score | silhouette IoU | palette sim |
|---|---|---|---|---|
| 037 Terrapod | #305 lairon | 0.795 | 0.728 | 0.895 |
| 043 Duskfiend | #121 starmie | 0.79 | 0.733 | 0.876 |
| DIW-05 Dream Cruncher | #362 glalie | 0.777 | 0.774 | 0.781 |
| 023 Megalochrome | #550 basculin-red-striped | 0.776 | 0.77 | 0.785 |
| 034 Gorokappa | #565 carracosta | 0.776 | 0.757 | 0.805 |
| 032 Gearkid | #478 froslass | 0.771 | 0.71 | 0.862 |
| 036 Cragarm | #285 shroomish | 0.77 | 0.719 | 0.848 |
| 026 Inklet | #582 vanillite | 0.766 | 0.692 | 0.876 |
| 044 Ashemit | #406 budew | 0.766 | 0.81 | 0.701 |
| 040 Dreadtoise | #551 sandile | 0.757 | 0.712 | 0.825 |
| 015 Quakehound | #113 chansey | 0.755 | 0.756 | 0.754 |
| 006 Reaperdile | #597 ferroseed | 0.753 | 0.686 | 0.853 |
| 001 Mochii | #143 snorlax | 0.749 | 0.773 | 0.711 |
| 019 Zephling | #258 mudkip | 0.748 | 0.725 | 0.784 |
| 007 Tyrage | #221 piloswine | 0.747 | 0.718 | 0.791 |
| 009 Oblivirex | #228 houndour | 0.738 | 0.616 | 0.92 |
| 013 Pupbble | #506 lillipup | 0.736 | 0.663 | 0.845 |
| 039 Shellguard | #550 basculin-red-striped | 0.735 | 0.726 | 0.748 |
| 038 Sproutle | #550 basculin-red-striped | 0.734 | 0.725 | 0.748 |
| 012 Manticlaw | #293 whismur | 0.732 | 0.729 | 0.737 |
| 035 Pebblefist | #459 snover | 0.729 | 0.662 | 0.828 |
| DIW-01 Mochling | #293 whismur | 0.727 | 0.712 | 0.75 |
| BS-02 Emburrn | #449 hippopotas | 0.724 | 0.72 | 0.728 |
| 005 Chromedile | #397 staravia | 0.712 | 0.603 | 0.876 |
| DIW-04 Ragdoll Brute | #285 shroomish | 0.712 | 0.778 | 0.612 |
| 028 Krakenox | #465 tangrowth | 0.71 | 0.663 | 0.781 |
| 046 Yogiferno | #54 psyduck | 0.706 | 0.675 | 0.753 |
| 017 Cocoonode | #201 unown | 0.7 | 0.661 | 0.759 |
| 016 Squirmite | #79 slowpoke | 0.697 | 0.625 | 0.804 |
| 002 Tiidebiite | #394 prinplup | 0.693 | 0.703 | 0.678 |
| 004 Razorgater | #602 tynamo | 0.69 | 0.674 | 0.715 |
| 033 Mechapion | #304 aron | 0.687 | 0.554 | 0.886 |
| 029 Punchkid | #201 unown | 0.684 | 0.761 | 0.568 |
| 020 Aerobeak | #9 blastoise | 0.681 | 0.599 | 0.805 |
| 011 Pyropaw | #12 butterfree | 0.68 | 0.736 | 0.595 |
| 045 Pyromonk | #433 chingling | 0.675 | 0.627 | 0.748 |
| 025 Astroleviathan | #263 zigzagoon | 0.672 | 0.75 | 0.555 |
| 042 Wispkin | #201 unown | 0.672 | 0.638 | 0.723 |
| 021 Stormtalon | #529 drilbur | 0.671 | 0.681 | 0.658 |
| 014 Terradog | #16 pidgey | 0.669 | 0.563 | 0.828 |
| 003 Aquari-OS | #194 wooper | 0.664 | 0.622 | 0.726 |
| 024 Floatcalf | #395 empoleon | 0.662 | 0.624 | 0.72 |
| DIW-03 Neon Stalker | #361 snorunt | 0.661 | 0.669 | 0.648 |
| 010 Kittember | #121 starmie | 0.66 | 0.642 | 0.686 |
| 030 Strikechamp | #627 rufflet | 0.658 | 0.677 | 0.63 |
| 008 Duneclaw | #434 stunky | 0.641 | 0.563 | 0.757 |
| DIW-02 Glitch-Mochi | #366 clamperl | 0.637 | 0.688 | 0.56 |
| 018 Mothrix | #538 throh | 0.63 | 0.583 | 0.701 |
| 331 Mythar | #163 hoothoot | 0.63 | 0.558 | 0.737 |
| 027 Toxitacle | #453 croagunk | 0.622 | 0.663 | 0.56 |
| 031 Kickmaster | #71 victreebel | 0.622 | 0.655 | 0.571 |
| BS-03 Aquabble | #366 clamperl | 0.618 | 0.523 | 0.762 |
| 022 Finblade | #602 tynamo | 0.614 | 0.578 | 0.667 |
| 041 Pixilite | #280 ralts | 0.549 | 0.558 | 0.535 |
