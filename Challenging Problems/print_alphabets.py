def print_big(letter):
    patterns = {
        1: '  *  ',
        2: ' * * ',
        3: '*   *',
        4: '*****',
        5: '**** ',
        6: '   * ',
        7: ' *   ',
        8: '*  * ',
        9: '*    ',
        10: '*  **',
        11: '    *',
        12: '  *  *',
        13: '* *  ',
        14: '** **',
        15: '* * *',
        16: '**  *',
        17: '**   ',
        18: '     ',
    }

    alphabet = {
        'A': [1, 2, 4, 3, 3],
        'B': [5, 3, 5, 3, 5],
        'C': [4, 9, 9, 9, 4],
        'D': [5, 3, 3, 3, 5],
        'E': [4, 9, 4, 9, 4],
        'F': [5, 9, 5, 9, 9],
        'G': [4, 9, 10, 3, 4],
        'H': [3, 3, 4, 3, 3],
        'I': [4, 1, 1, 1, 4],
        'J': [11, 11, 11, 12, 6],
        'K': [8, 13, 9, 13, 8],
        'L': [9, 9, 9, 9, 4],
        'M': [3, 14, 15, 3, 3],
        'N': [3, 16, 15, 10, 3],
        'O': [4, 3, 3, 3, 4],
        'P': [4, 3, 4, 9, 9],
        'Q': [4, 2, 15, 10, 4],
        'R': [17, 13, 17, 13, 8],
        'S': [4, 9, 4, 11, 4],
        'T': [4, 1, 1, 1, 1],
        'U': [3, 3, 3, 3, 4],
        'V': [3, 2, 1, 18, 18],
        'W': [3, 3, 15, 14, 4],
        'X': [3, 2, 1, 2, 3],
        'Y': [3, 2, 1, 1, 1],
        'Z': [4, 6, 1, 7, 4],
    }

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


    # iterating through each number of an alphabet
    # and print patterns[pattern_number#]

user_input = input("Enter a word: ")
for char in user_input:
    print_big(char)
