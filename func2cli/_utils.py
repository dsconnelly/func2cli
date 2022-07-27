import builtins

def default_parse_func(func):
    """
    Parse a function and its docstring, and return data for argument parsing.

    The default parse assumes that the docstring has a single-line summary of
    func, followed by a blank line, and then a series of parameter descriptions
    following ten dashes (as below). The parameter descriptions should consist
    of the parameter name and type, separated by a colon, on one line, followed
    by an indented description of the parameter. The parameter list should be
    separated from the rest of the docstring by a blank line.

    Parameters
    ----------
    func : function
        The function to be parsed.

    Returns
    -------
    name : str
        A sanitized version of func.__name__.
    description : str
        A description of the behavior of func.
    params : list of dict
        A list of keyword argument dictionaries that can be passed to successive
        calls to add_argument.

    """

    name = func.__name__.replace('_', '-')
    docstring = func.__doc__

    start = docstring.index('\n') + 1
    end = docstring.index('\n\n')
    description = docstring[start:end].strip()

    header = 'Parameters\n    ----------\n'
    docstring = docstring[(docstring.index(header) + len(header)):]
    docstring = docstring[:docstring.index('\n\n')]

    params = []
    for line in [s[4:] for s in docstring.split('\n')]:
        if not line.startswith('    '):
            param_name, type_name = line.split(' : ')
            params.append({
                'param_name' : param_name,
                'metavar' : param_name.replace('_', '-'),
                'type' : getattr(builtins, type_name),
                'help' : []
            })

        else:
            params[-1]['help'].append(line.strip())

    for param in params:
        param['help'] = ' '.join(param['help'])

    return name, description, params
