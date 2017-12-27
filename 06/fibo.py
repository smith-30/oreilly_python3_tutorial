"""
このモジュールでは FizzBuzz 問題を実装しています。
"""

def fib(num):
    """
    doc
    """
    a, b = 0, 1
    while b < num:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(num):
    """
    doc
    """
    result = []
    a, b = 0, 1
    while b < num:
        result.append(b)
        a, b = b, a+b
    return result
