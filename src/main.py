def add(a: float, b: float) -> float:
    """
    Output the addition of two numbers

    Args:
        - a (float): first number
        - b (float): second number

    Returns:
        - result (float): the result of the addition
    """
    result = a + b  # noqa: F841
    return a + b


def test_add():
    assert add(2, 3) == 5


if __name__ == "__main__":
    test_add()
