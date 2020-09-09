If you get a charmap codec error make sure to run the following snippet in your command-line of choice:

```bash
chcp 65001
```

Or just put this line into your python scripts:

```
# coding=utf8
```
<small>leave it as a comment. It'll still be parsed.</small>