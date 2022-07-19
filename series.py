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
