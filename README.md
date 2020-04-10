# effpassphrase
Uses the [EFF's](https://www.eff.org/) [long word list](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) to generate a high entropy passphrase.

# Installation

```console
pip install effpassphrase
```

# Usage

```console
$ effpassphrase --help
Usage: effpassphrase [OPTIONS]

Options:
  -c, --count INTEGER   Number of words in the passphrase.
  -s, --separator TEXT  Separator used between words in the passphrase.
  --help                Show this message and exit.
```

```console
$ effpassphrase
unfounded zips decorator expectant starch variable
```
