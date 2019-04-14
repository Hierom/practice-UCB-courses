def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update


def power(x, n):
    product, k = 1, 0
    while (k < n):
        product, k = product * x, k + 1
    return product


def nth_root_of_a(n, a):
    def f(x):  # x^n -a
        return power(x, n) - a

    def df(x):  # nx^(n-1)
        return n * power(x, n - 1)

    return find_zero(f, df)


# general update formula
def improve(update, close, guess=1, max_update=100):
    k = 0
    while not close(guess) and k < max_update:
        guess, k = update(guess), k + 1
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance
