# testing Fibonacci number function
# pylint: skip-file
from fib import fib


def test_fibonacci():
    assert fib(10) == 55


def test_hamed():
    assert fib(1) == 1
