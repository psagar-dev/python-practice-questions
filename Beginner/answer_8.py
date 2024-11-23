#Write a Python program to remove duplicates from a list.

def removeDuplicates(inputList):

    return list(set(input_list))

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 7,11, 15, 11 ,15 ,7, 5, 6]

output_list = removeDuplicates(input_list)


print("Original List:", input_list)
print("List without duplicates:", output_list)

