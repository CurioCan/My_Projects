lst = [
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 16),
    (17, 18, 19, 20),
    (21, 22, 23, 24),
    (25, 26, 27, 28),
]

len_tuple = len(lst[0])

for i in range(len(lst)):
    for j in range(len_tuple):
        if i % len_tuple == j:
            print(f"{". " * j}{lst[i][j]}")

