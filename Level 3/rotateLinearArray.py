def rotate_left(list_numbers,k):
    len_list = len(list_numbers)-1
    k = k % (len_list +1)
    list_numbers = list_numbers[::-1]
    list_numbers = list_numbers[len_list-k::-1] + list_numbers[len_list:len_list-k:-1]
    return list_numbers