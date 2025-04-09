

# dictionary
person = {
    "name": "Charitha Sri",
    "age": 18,
    "gender": "female"
}

print(person["age"])

# strings
print("I am going on a path ")

# strings cannot be assigned

# strings can be concatenated
# math arithmetic
square = 8 ** 2
cube = pow(5, 3)

# modular_exponentiation
mod_exp = pow(7, 3, 10)
# (7 ^ 3) % 10 = 3
# 343 % 10 = 3

# print("Square : " + square + " cube : " + cube + "modular :" + mod_exp)
# you cannot concatenate strings with numbers

# print the result using formatted f-strings
print(f"Square: {square} cube : {cube} modular : {mod_exp}")

# converting into string type so that we can concatenate
# print("Square: " + str(square) + " cube : " + str(cube) + " modular : " + str(mod_exp))

# pow(base, exponent, mod)
 # type()
 # ** + - / \n \t \\ \' \" floating point and how computer stores in the form of base 2so there is floating point accuracy
 # len()
 # print("*" * 19) prints the character 19 times
  # slicing [start:stop:step]
 # greet[::-1] reverse shortcut
 # you cannot assign string character or modify rather you can slice it and concatenate
 # tuples cannot be modified unless they are again declared once again
 # boolean True or False
 #dict = {
 #  "key": "value,
  # }
# list = [10, "strings", "1998"]
# dict = {
   # "list1": [12, "you can do it"],
 # }
# tuples = ("names", 87, "8999")
# sets = {"a", "b"}
# num integers, floats


# 1E2 MEANS 1 x 10 ^ 2
print(5E2)
print(7 // 3) # rounding-off // floor division
print(round(7/3, 1))
print(round(7/3))
print(7/3)
print(4**0.5) # square root

'''
don't use l O I as the variable names 
avoid inbuilt key words
'''
print(type(person))


# strings have this property called immutability that once a string it is created, the elements cannot be changed or replaced
x = "Hello World"
while x == "Hello World":
    x = x + " World"
print(x)

# name = "Sam"
# name[0] = 'P' is wrong

# safely substituting in a string from user by a template like when you open an app it takes your name and says Hii your name so it has a template and the safe_substitute
from string import Template

user_name = input("Enter your name ? ")
t = Template("Hiii $name, You may have $count new messages.")
result = t.safe_substitute(name = user_name, count = 5)
print(result)


# isinstance(ele, int) checking the data type
lst = ["reverse", "palindrome", "898989", 2776865, "mom", "wow"]
rev_list = []
for ele in lst:
    if isinstance(ele, int): # type(ele) == int
        reverse = int(str(ele)[::-1])
    elif isinstance(ele, float): # type(ele) == float
        reverse = float(str(ele)[::-1])
    else:
        reverse = str(ele)[::-1]
    rev_list.append(reverse)
print(f"The strings in \n{lst} are reversed to\n{rev_list}")


# reversing every element in a list
lst = ["reverse", "palindrome", "898989", 2776865, "mom", "wow"]
rev_list = []
indices_int = []
for ele in lst:
    if type(ele) == int:
        index = lst.index(ele)
        indices_int.append(index)
        reverse = int(str(ele)[::-1])
    else:
        reverse = str(ele)[::-1]
    rev_list.append(reverse)

#float formatting
print(f"the strings in \n{lst} are reversed\n{rev_list}\n {indices_int}")

# formatted string we have already used it in one way
print('This is a string {}'.format('INSERTED'))

#place holder
print("The {} {} {}".format('fox', 'brown', 'quick'))

#keyword_arguments
print(" {Name} Age: {Age} Gender: {Gender}".format(Name="Charitha", Age=18, Gender="Female"))

#positional_arguments
print("{1} Age: {0} Gender: {2}".format(18, "Charitha Sri", "Female"))

# normal concatenation  without a place holder by default adds a space and concatenates
greet = "Namaste"
print("Hello", greet)

#f-strings
print(f"{greet}!! garu")

print("The","quick","brown", "fox")

# floating formatting follows place holder -> "{value:width.precisionf}" width basically describes the white space
dec = 9309.924923
print(f"The result was {dec:0.6f}")

# .format() dot format method
print("The result was {:0.2f}".format(dec))
print("THe result was {d:6.4f}".format(d=dec)) # here width is 10 which is 4 spaces two tabs may be 5 width is 1 tab

# padding padd with 0 print("{value:(pad-digit0/whitespace)no_of_times.precision d/f according to int or float
print("{0:04d".format(5)) # 0005
print("{0:.<10".format("format")) #allign left and as width is 10 pad the rest with .
# allign objects : ^ center, < align left most, > align right most
# print('{:10.5}'.format('xylophone') displays 'xylop     ' 5 white spaces
# strings by default align right most
# numbers allign to left most by default
# print("{:06.2f}".format(3.1415926535) prints '003.14' 2 decimals 6 boxes and pad beginning by 0's
# '{:+d}'.format(42) displays '+42'
# **data passes as key word arguments

