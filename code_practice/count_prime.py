def is_prime(n):
    if n == 1 or n == 0: # 1 or 0 by convention is not a prime
        return False
    elif n == 2 or n == 3: # prime for sure
        return True
    elif n % 2 == 0 or n % 3 == 0: # if it is divisible not a prime
        return False
    else:

        # 5 <= i <= sqrt(n) for all odd numbers
        # n % i == 0
        check_list = [i for i in range(5, int(n ** 0.5) + 1)]
        for i in check_list:
            if n % i == 0:
                return False
        return True



def count_primes(num):
    # generate numbers
    whole_numbers = range(num + 1)

    count = 0
    prime_numbers = []

    for number in whole_numbers:
        if is_prime(number):
            count += 1
            prime_numbers.append(number)

    return count, prime_numbers

print(count_primes(20))


'''
PEHLA mistake 
list = [range(0, 10)] doesn't generate list of numbers instead
what it has is this 

Output # [range(0, 10)]

So, be cautious to write it as 

list = range(0, 10)
or else 
list = [ i for i in range(0, 10) ]
'''

# shorter form
def is_prime_(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1 ):
        if n % i == 0:
            return False
    return True
