def myfunc(str="Isomorphism"):
    odd_string = str[1::2]
    even_string = str[::2]

    odd_string = odd_string.upper()
    even_string = even_string.lower()

    new_string = ""

    if len(str) % 2 == 0:
        for i in range(len(str) // 2):
            new_string += even_string[i] + odd_string[i]
    else:
        for i in range((len(str) // 2) + 1):
            if i == len(str) // 2:
                new_string += even_string[i]
            else:
                new_string += even_string[i] + odd_string[i]

    return new_string

print(myfunc())