# makehelp

makehelp

## Usage

```
usage: makehelp [-h] [--file MAKEFILE] [--inject] [target]

Process a Makefile and display help information

positional arguments:
  target                Print the full recipe (code) of a specific target

options:
  -h, --help            show this help message and exit
  --file, --makefile, -f MAKEFILE
                        Path to the Makefile (defaults to "Makefile" or "makefile" in current
                        directory)
  --inject              Inject a `help` target into the Makefile that calls makehelp (entirely
                        optional)
```
