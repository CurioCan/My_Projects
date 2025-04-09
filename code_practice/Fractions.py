numbers = [1, 3, 5, 7]
fractions = []

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i < j:
            fraction = numbers[i] / numbers[j]
            fractions.append(fraction)

print(fractions[2])
