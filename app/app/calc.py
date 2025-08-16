""" 
Calculator functions 
"""

def add(x: int, y: int) -> int:
    """
    Add two integers.
    Args:
        x (int): The first number.
        y (int): The second number.
    Returns:
        int: The sum of x and y.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers.")

    return x + y

def add_strings(s1: str, s2: str) -> str:
    """
    Concatenate two strings.
    Args:
        s1 (str): The first string.
        s2 (str): The second string.
    Returns:
        str: The concatenation of s1 and s2. 
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both s1 and s2 must be strings.")

    return s1 + s2