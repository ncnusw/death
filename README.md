# Death, Grief, and Bereavement Care

A collection of classroom games and activities for the course *Death, Grief, and Bereavement Care*, Department of Social Policy and Social Work, National Chi Nan University.

Play them at **https://ncnusw.github.io/death/**

## Escape the Jail of Assumptions (`games/jail/`)
Whole-class escape room on cross-cultural bereavement and cultural humility. One screen, one wireless keyboard, six tables, each holding a printed evidence card (A–F). Eight locked cells; the last needs letters from every table.

- Controls: type answers + Enter, Backspace, arrows walk, Esc pause, ? hint. Touch: ⌨ KEYPAD. 8BitDo: D-pad, Select = keypad, face button = press, Start = pause.
- Embed in Quarto: `<iframe src="https://ncnusw.github.io/death/games/jail/" width="100%" height="100%" style="border:0" allow="autoplay; fullscreen"></iframe>`, or use the slide attribute `background-iframe="https://ncnusw.github.io/death/games/jail/" background-interactive="true"`.
- To change puzzles: edit `_private/jail/levels.js`, then run `node build.js` inside `_private/jail/` (needs Node). The cards are in the teacher folder.
