a = 1
b = 2

while b > a:
    while (a + b + ((a)**2 + (b)**2)**0.5) <= 1000:
        c = (a**2 + b**2)**0.5
        if c.is_integer() and (a + b + c) == 1000:
            print(int(a*b*c))
            break

        a += 1

    b += 1
    a = 1