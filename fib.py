"""Finbonachi"""


def fib(num: int) -> int:
    """Return fibonachi"""
    return num if num < 2 else fib(num - 1) + fib(num - 2)
