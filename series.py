def fibonacci(n):
    """
    Returns the value of the provided number's index in the fibonacci sequence.
    :param n: (int): a single integer
    :return: fibonacci(n-1) + fibonacci(n-2) - (int): the fibonacci sequence value
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1 + fibonacci(n-1)
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    Returns the value of the provided number's index in the fibonacci sequence.
    :param n: (int): a single integer
    :return: lucas(n - 1) + lucas(n - 2) - (int): the lucas sequence value
    """
    if n <= 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, a=0, b=1):
    """
    Returns the value of the provided number's index in the fibonacci sequence.
    :param n: (int): a single integer
        a - (int)(optional): a starting integer for the 0 index
        b - (int)(optional): a starting integer for the 1 index
    :return: sum_series(n - 1, a, b) + sum_series(n - 2, a, b) - (int): the lucas or fibonacci sequence value
    """
    if n <= 0:
        return a
    if n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)