from series import fibonacci, lucas, sum_series
import pytest

def xtest_fibonacci_input_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def xtest_fibonacci_input_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def xtest_fibonacci_input_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def xtest_fibonacci_input_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def xtest_fibonacci_input_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def xtest_fibonacci_input_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def xtest_lucas_input_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def xtest_lucas_input_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def xtest_lucas_input_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def xtest_lucas_input_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def xtest_lucas_input_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def xtest_lucas_input_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_sum_series_input_0_fibonacci():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_input_0_lucas():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sum_series_input_1_fibonacci():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_input_1_lucas():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected


def test_sum_series_input_2_fibonacci():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_series_input_2_lucas():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected


def test_sum_series_input_3_fibonacci():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_sum_series_input_3_lucas():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected