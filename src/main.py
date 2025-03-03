"""Main script for test purposes
"""

def add(a: float, b: float) -> float:
    """Output the addition of two numbers

    Arguments:
        a : first number
        b : second number

    Returns:
        result : the result of the addition
    
    Example:

        ```python
        result = add(5, 5)
        assert result == 10
        ```
    """
    result = a + b  # noqa: F841
    return a + b


def test_add():
    assert add(2, 3) == 5


if __name__ == "__main__":
    test_add()
