"""
Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order. 
This method should return a list of redundant integers in ascending sorted order (as illustrated below). 

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]

duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]

"""


def insertionSort(list):
    for i in range(1, len(list)):
        pointer = list[i]
        j = i - 1
        while j>=0 and pointer < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = pointer
    return(list)
        

def duplicate_items(list_numbers):
    newList = []
    insertionSort(list_numbers)
    for i in range(0, len(list_numbers)):
        pointer = list_numbers[i]
        for j in range(i+1, len(list_numbers)):
            if (pointer == list_numbers[j]):
                newList.append(pointer)
            else:
                break
    return(newList)