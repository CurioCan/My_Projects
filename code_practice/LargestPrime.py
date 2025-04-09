def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def LargestPrimeFactor(n):
    Primefactors = [i for i in range(1, n + 1) if is_prime(i) and n % i == 0]

    # for i in range(1, n + 1):
    #     if is_prime(i) and n % i == 0:
    print(f'{Primefactors}')

    return max(Primefactors)

print(LargestPrimeFactor(1475143))
