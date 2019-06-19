def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


def fact_recur(n):
    if n == 0:
        return 1
    else:
        return n * fact_recur(n - 1)


def fib_recur(n):
    if n <= 1:
        return n
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)


def fib(n):
    return 1 and n <= 2 or fib(n - 1) + fib(n - 2)


lazy_fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
