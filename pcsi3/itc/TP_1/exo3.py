
def fib(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib(8))
