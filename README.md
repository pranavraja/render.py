# render.py

Applies transformations to standard input with format strings. Useful for transforming data that has been text-tabulated, for example:

(out.txt)
```
State of Emergency	The Living End
Here I Go Again	Whitesnake
```

Running `render.py < out.txt -f "{0}"` will extract the first field, the same as `cut < out.txt -f1`. 

However we can also do more complex transformations like `render.py < out.txt -f "The song {0} is by artist {1}"`. Try it out.

# Setup

Clone the repo into a new directory, and add that directory to your `PATH`.

# Usage

Run `render.py -h` for usage documentation.

```
usage: render.py [-h] [-f FORMAT] [-d DELIMITER] [-s] [inputfile]

Apply a format transform to stdin

positional arguments:
  inputfile             Input string (default stdin)

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Format string
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter (default TAB)
  -s, --skip-first      Skip the first line of input (default False)
```
