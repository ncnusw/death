# Death, Grief, and Bereavement Care

A collection of classroom games and activities for the course *Death, Grief, and Bereavement Care*, Department of Social Policy and Social Work, National Chi Nan University.

Play them at **https://ncnusw.github.io/death/**

## Escape the Jail of Assumptions (`games/jail/`)
Whole-class escape room on cross-cultural bereavement and cultural humility. One screen, one wireless keyboard. The room fills the screen; cells 1–4 are solved from clues inside the room (books, pinned notes, counting, and push puzzles), cells 5–8 still use the printed evidence cards (D–F, and all six tables for the last door).

- Controls (keyboard only): arrows walk · Space reads a book or note · walk into a stone or bucket to push it · R puts them back · walk up to the cell door and type the answer, Enter to try it · Esc pause · ↺ RESET GAME (top right, press twice) erases progress.
- Embed in Quarto: `<iframe src="https://ncnusw.github.io/death/games/jail/" width="100%" height="100%" style="border:0" allow="autoplay; fullscreen"></iframe>`, or use the slide attribute `background-iframe="https://ncnusw.github.io/death/games/jail/" background-interactive="true"`.
- To change puzzles: edit `_private/jail/levels.js`, then run `node build.js` inside `_private/jail/` (needs Node). The cards are in the teacher folder.
