# Death, Grief, and Bereavement Care

A collection of classroom games and activities for the course *Death, Grief, and Bereavement Care*, Department of Social Policy and Social Work, National Chi Nan University.

Play them at **https://ncnusw.github.io/death/**

## Escape the Jail of Assumptions (`games/jail/`)
Whole-class escape room on cross-cultural bereavement and cultural humility. One screen, one wireless keyboard. The room fills the screen; all eight cells are solved from clues inside the room (books read in a pop-up, light arithmetic, a colour-tile floor and push puzzles; no text is drawn in the room). No printed cards are needed.

- Controls (keyboard only): arrows walk · Space reads a book (or a cart's delivery slip) · walk into a stone, bucket or letter to push it · R puts them back · in one room, Enter changes the colour of the floor tile you stand on · at the cell door press Enter to open the lock, type the answer, Enter to try it, Esc to close the lock · Esc pause · ↺ RESET GAME (top right, press twice) erases progress.
- Embed in Quarto: `<iframe src="https://ncnusw.github.io/death/games/jail/" width="100%" height="100%" style="border:0" allow="autoplay; fullscreen"></iframe>`, or use the slide attribute `background-iframe="https://ncnusw.github.io/death/games/jail/" background-interactive="true"`.
- To change puzzles: edit `_private/jail/levels.js`, then run `node build.js` inside `_private/jail/` (needs Node).
