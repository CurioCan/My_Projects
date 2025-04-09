'''
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array
 but that are in the same order as they appear in the array .
 [1, 3, 4]
 form a subsequence of the array
 [1, 2, 3, 4]
 and so do the numbers [2, 4]
 Note that a single number in an array and the array itself are both valid
 subsequence

 Every number in subsequence must be in array
 [1, 2, 2, 3, 4, 5]
 subsequence [1, 2, 3, 5]
 but not [ 2 , 1, 2]


 so for multiple copies you have to think of it in another way
'''


def isValidSubsequence(array, sequence):
    # Write your code here.
    index_list = []
    for element in sequence:
        # index_list[element] = array.index(element)
        if element not in array:
            return False
        else:
            index_list.append(array.index(element))
            array.remove(element)

    for i in range(len(index_list) - 1):
        if index_list[i] > index_list[i + 1]:
            return False
    return True


# what I am trying to do is first thing firsts checking if
# every elemnt in subsequence is part of array or not
# noting down the index of the element
# for overcoming the multiple copies of single element index returns thr first occurence
# so what should be done is that remove that element from the list if found
# and then check the order of the sequence