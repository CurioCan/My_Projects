def count_divisors(number):
    count = 0
    for divisor in range(1, int(number**0.5)+1):
        if number % divisor == 0:
            count += 2 if divisor * divisor != number else 1
    return count

def find_number(d):
    num = 1
    while True:
        if count_divisors(num) == d:
            return num
        num +=1

print(f" The number {find_number(16)} has 16 divisors")
