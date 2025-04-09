def greet(first, last):
    print(f"Hello, {first} {last}")
data = {"first": "Charitha", "last": "Sri"}
greet(**data)

# from datetime import datetime
# '{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))

class HAL9000(object):
    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL9000'

print('{:open-the-pod-bay-doors}'.format(HAL9000()))
# internally it works this way HAL9000().__format__('open-the-pod-bay-doors')

for index, char in enumerate("Learn by doing"):
    print(f"This is the character {char} at {index}")
    print("")
passion = len("If I join IAS, I would be helping and reaching out people")
print(passion)

# sets have unique elements it doesn't have key value pairs, it doesn't add a same element again
# {}
myset = set()
print(myset)
myset.add(9)
myset.add(9)
print(myset)
# no order for the set

# grab the unique values
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
print(set(mylist))

# are sorted automatically
print(set('Mississipi'))