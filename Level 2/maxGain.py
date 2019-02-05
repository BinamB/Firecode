def max_gain(input_list):
    maxg = 0
    max = 0
    min = input_list[0]
    for i in range(1, len(input_list)):
        if(max < input_list[i]):
            maxg = input_list[i]-min
            max = input_list[i]
        if min > input_list[i]:
            return 0
    return(max-min)