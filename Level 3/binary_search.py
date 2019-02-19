def binary_search(a_list, item):
    length = len(a_list)
    half = int(round(length/2))
    print(a_list)
    if(a_list == [] or (a_list[half] != item and length == 1)):
        return False
    if (a_list[half] == item):
        return True
    elif (a_list[half] < item):
        return binary_search(a_list[half:(length)], item)
    elif (a_list[half] > item):
        return binary_search(a_list[0:half], item)  
        