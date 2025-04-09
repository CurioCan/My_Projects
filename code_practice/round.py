def round(n):
    if n % 10 < 5:
        return n - (n % 10)
    else:
        return n + (10 - (n % 10))


def round_sum(a, b, c):
    return round(a) + round(b) + round(c)

# round-off and add