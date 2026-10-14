# Changelog

## 2026-10-14
- Added **Line Charades** (`games/line-charades/`), adapted from the earlier slide version: two teams take turns over 5 rounds; guessers close their eyes while the acting team reads its secret line (shown with its stanza), then the guesser picks the line from the whole poem. 1 point for the exact line. Adjustable reading and guessing times; 8BitDo join screen, keyboard and touch; pauses when the slide is hidden. Text: Emily Dickinson, Fr479, after Franklin (Harvard UP, 1998), credited on the title screen. Uses only the site's own sounds.
- Added **Ageism Quiz** (`games/ageism-quiz/`): 10 questions on ageism and grief, shuffled each try, with an explanation after every answer. The score screen turns rainbow at 10/10, green at 7–9, and yellow at 6 or below, so scores can be read across a large room. Try Again button, discussion questions, no sounds. Touch, keyboard (1–4, Enter) and 8BitDo.
- Launch page: added a neutral card colour for games that are not about the Dual Process Model, and removed the Loss-Oriented / Restoration-Oriented legend from the header, since not every game uses those ideas.
- Set up the site: launch page (`index.html`) built from `games.json`, with a backup game list so it also opens straight from a folder.
- Added **The Swing** (`games/swing/`), a 1–2 player Dual Process Model game: moved from the old `scripts/` folder, sound path updated to `assets/audio/`, added large touch buttons for tablets and phones and a rotate-to-landscape hint.
- Replaced the sound effects with original 8-bit jingles (`assets/audio/wow.mp3`, `assets/audio/win.mp3`).
- Added README, CHANGELOG, `.nojekyll`.
