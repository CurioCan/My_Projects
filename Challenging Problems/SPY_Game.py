def spy_game(nums):
    # returns True if it contains 0 0 7 in order
    # takes a list

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works

    return len(code) == 1 # returns a bool