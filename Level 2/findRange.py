def find_range(input_list,input_number):
    lower = 0
    upper = 0
    for i in range(0, len(input_list)):
        if input_list[i] == input_number and lower == 0:
            lower = i
            upper = i
        if input_list[i] == input_number:
            upper = i
    return Range(lower, upper)
            