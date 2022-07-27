`func2cli` is a wrapper around the standard Python `argparse` library that intelligently passes arguments from the command line to one or more Python functions. `func2cli` reads the docstrings of those functions and extracts relevant information that is then passed to calls of the `add_argument` method of `argparse` parsers.

The example script below uses `func2cli` to pass command line arguments to one of two simple functions.
```python
#script.py

from func2cli import FunctionParser

def add_three(a, b, c):
    """
    Add three numbers together.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.
    c : float
        The third and final number to add.

    Returns
    -------
    d : float
        The sum of a, b, and c.

    """

    return a + b + c

def write_to_path(n, path):
    """
    Write an integer to a file.

    Parameters
    ----------
    n : int
        The number to save to disk.
    path : str
        The path of the file where n should be saved.

    """

    with open(path, 'w') as f:
        f.write(n)

if __name__ == '__main__':
    parser = FunctionParser([add_three, write_to_path])
    parser.run()
```
Usage information is automatically available at the command line.
```
>>> python script.py -h
usage: script.py [-h] {add-three,write-to-path} ...

positional arguments:
  {add-three,write-to-path}
    add-three           Add three numbers together.
    write-to-path       Write an integer to a file.

options:
  -h, --help            show this help message and exit
```
`script.py` has two allowed positional arguments, one for each of the functions passed to the `FunctionParser`. Moreover, usage information for individual positional arguments can also be displayed.
```
>>> python script.py add-three -h
usage: script.py add-three [-h] a b c

positional arguments:
  a           The first number to add.
  b           The second number to add.
  c           The third and final number to add.

options:
  -h, --help  show this help message and exit
```
Finally, note that the `FunctionParser` knows what types are permissible for each argument. For example, the arguments to `add-three` should all be floats, and so an invalid argument passed at the command line raises an error.
```
>>> python script.py add-three 1 foo 3
usage: script.py add-three [-h] a b c
script.py add-three: error: argument b: invalid float value: 'foo'
```
By default, `func2cli` assumes that function docstrings look like the ones shown in `script.py` above. However, `func2cli` supports arbitrary docstring conventions by allowing the user to pass a custom `parse_func` argument to `FunctionParser`.
