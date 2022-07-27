def add_two(a, b):
    """
    Add two numbers together.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add. But for whatever reason, b has a description
        that stretches over several lines.

    Returns
    -------
    c : float
        The sum of a and b.

    """

    return a + b

def add_with_default(p, q=5):
    """
    Add two numbers with a sensible default.

    Parameters
    ----------
    p : float
        The first number to add.
    q : float
        The second number to add. Defaults to 5.

    Returns
    -------
    r : float
        The sum of p and q.

    """

    return p + q

def subtract_three(a, b, c):
    """
    Subtract three numbers.

    The usage of this function is a little more complicated, so in addition to
    its short description it has a longer description that is split over not
    just two, but three lines.

    Parameters
    ----------
    a : float
        The number we start with.
    b : float
        The first number we subtract off.
    c : float
        The second number we subtract off.

    Returns
    -------
    d : float
        The result of subtraction, maybe negated.

    """

    return a - b - c