# go through these examples
class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __format__(self, format_spec):
        if format_spec == "square":
            return str(self.value ** 2)
        elif format_spec == "cube":
            return str(self.value ** 3)
        else:
            return str(self.value)

obj = CustomNumber(3)
print(format(obj, "square"))  # Output: '9'
print(f"{obj:cube}")          # Output: '27'

'''
how it works 
"{:open-the-pod-bay-doors}".format(hal),
 Python internally calls hal.__format__('open-the-pod-bay-doors').
'''

class HAL9000(object):
    # The __format__ method is called when the object is used in a formatted string
    def __format__(self, format):
        # If the format string is 'open-the-pod-bay-doors', return the special message
        if format == 'open-the-pod-bay-doors':
            return "I'm afraid I can't do that."
        # For all other format strings, return the default 'HAL 9000'
        return 'HAL 9000'

# Create an instance of the HAL9000 class
hal = HAL9000()

# The __format__ method is automatically called when using the object in a format string
print("{:open-the-pod-bay-doors}".format(hal))  # Output: I'm afraid I can't do that.
print("{:default}".format(hal))  # Output: HAL 9000


