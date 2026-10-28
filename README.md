# Death, Grief, and Bereavement Care

A collection of classroom games and activities for the course *Death, Grief, and Bereavement Care*, Department of Social Policy and Social Work, National Chi Nan University.

Play them at **https://ncnusw.github.io/death/**

## Locked games

Light in the Stacks, Palliative Shift and Bereavement Shift open only with the class password. The published pages hold an encrypted copy of each game, so neither the game nor the password can be read from the source. The unencrypted sources live in `_private/` on the teacher's computer and are never pushed (see `.gitignore`).

To change the password, run from the repo folder (Node.js required), then push:

```
node _private/lock.js _private/bereavement-shift.html games/bereavement-shift/index.html NEWPASSWORD bereavement-shift "Bereavement Shift" "Bereavement Shift"
node _private/lock.js _private/palliative-shift.html games/palliative-shift/index.html NEWPASSWORD palliative-shift "Palliative Shift" "Palliative Shift"
node _private/lock.js _private/stacks/index.html games/stacks/index.html NEWPASSWORD stacks "書庫裡的光 Light in the Stacks" "Light in the Stacks<br><span style=\"font-size:.6em\">書庫裡的光</span>"
```

To edit Light in the Stacks, change `_private/stacks/tools/story.py`, run `python _private/stacks/tools/build_data.py`, then lock it again with the line above.

