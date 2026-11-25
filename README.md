# zinger

[![make.fun · u-coral-404-one-line-big-laugh-328fb857](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)
[![rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/nmlyz/zinger/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)
[![reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/nmlyz/zinger/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)

[make.fun page](https://make.fun/competitions/u-coral-404-one-line-big-laugh-328fb857)

A tiny program that writes one funny line to a text file. The line is a
single sentence of 116 characters: an autocorrect slip in July turns a
text to a girlfriend into a Christmas temp job.

## The line

> My phone autocorrected "I love you" to "I love yule" in July, and my
> girlfriend now thinks I am a seasonal employee.

The joke lands on the calendar: "yule" only makes sense in December, so
a July typo reframes the sender as someone hired for the holidays. No
setup is needed beyond the phone doing what phones do.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). Running it twice produces byte-identical output.
