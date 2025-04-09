# has 22
def has22(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] == 2 and abs(i - j) == 1:
                return True
    return False

# return True if the array contains a 2 next to a 2 somewhere
# o r you could make it shorter
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1] == 2:
            return True
    return False

from string import Template
user_name = input("Your good name ? ")
user_choice = input("Which shopping mall you wanna explore ? ")
t = Template("Welcome, $name!! You are into greatest shopping mall of the world $shopping_mall shopping mall")
result = t.safe_substitute(name=user_name, shopping_mall=user_choice)
print(f"{result}...")

Wakeup = True

if Wakeup:
    print("Good Morning!!")

import time
for i in range(10):
    print(f"{i}","", sep = '..', end = "", flush=True)
    time.sleep(1)

# when you typically use the iterable thing you just wanna print
# certain string # character number of times
# you're gonna simply put '_' without specifying any identifier
for _ in "Passion":
    print("You are born To do great things")

# for tupple unpacking
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
len(mylist)
for item in mylist:
    print(item)

print(f"tuple unpacking : ")
for (a, b) in mylist:
    print(a)

for index, char in enumerate("HELLO"):
    print(f"{char} at {index}", end = " __ ")

