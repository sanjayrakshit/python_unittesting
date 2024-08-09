import time

import pytest
import src.my_functions as my_functions


def test_add():
    res = my_functions.add(2, 3)
    assert res == 5


def test_divide():
    res = my_functions.divide(6, 2)
    assert res == 3


def test_divide_zero_division():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)


def test_multiple():
    assert 4 == my_functions.multiply(2, 2)
    assert 10 == my_functions.multiply(2, 5)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    res = my_functions.divide(6, 2)
    assert res == 3


@pytest.mark.skip(reason="This is broken right now")
def test_add_broken():
    assert 'ab' == my_functions.add('a', 'b')


@pytest.mark.xfail(reason='This feature is not handled')
def test_divide_by_zero():
    my_functions.divide(10, 0)