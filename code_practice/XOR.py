numbers = [3, 10, 5, 25, 2, 8]
largest_XOR = 0

numer_1 = 0
number_2 = 0

for a in numbers:
    for b in numbers:
        XOR = a ^ b
        if XOR > largest_XOR:
            largest_XOR = XOR
            number_1, number_2 = a, b

print(f"Largest XOR of any two numbers: XOR of {number_1} and {number_2} is {largest_XOR}")