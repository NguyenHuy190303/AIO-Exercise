import math

def factorial(n):
    """Tính giai thừa của một số nguyên dương n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def approx_sin(x, n):
    """Ước lượng sin(x) bằng chuỗi Taylor đến n số hạng."""
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2*i + 1) / factorial(2*i + 1)
        result += term
    return result

def approx_cos(x, n):
    """Ước lượng cos(x) bằng chuỗi Taylor đến n số hạng."""
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2*i) / factorial(2*i)
        result += term
    return result

def approx_sinh(x, n):
    """Ước lượng sinh(x) bằng chuỗi Taylor đến n số hạng."""
    result = 0
    for i in range(n):
        term = x**(2*i + 1) / factorial(2*i + 1)
        result += term
    return result

def approx_cosh(x, n):
    """Ước lượng cosh(x) bằng chuỗi Taylor đến n số hạng."""
    result = 0
    for i in range(n):
        term = x**(2*i) / factorial(2*i)
        result += term
    return result
