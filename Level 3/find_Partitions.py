"""
Given a sorted list of integers, find partitions such that each partition denotes a range of consecutive integers.

Note: The input list consists of sorted integers, without duplicates. Range(a,b) should be denoted as a-b where a and b are included in the range.

Example:
Input : [1,2,3,6,7,8,10,11]  
Output : [1-3, 6-8, 10-11]
"""
def find_partitions(input_list):
    fin = []
    initial = input_list[0]
    for i in range(0, len(input_list)):
        if (i == len(input_list) - 1):
            end = input_list[i]
            if (initial == end):
                fin.insert(len(fin), initial)
            else:
                fin.insert(len(fin), str(initial)+'-'+str(end))        
    
        elif(input_list[i] != input_list[i+1] - 1):
            end = input_list[i]
            if (initial == end):
                fin.insert(len(fin), initial)
            else:
                fin.insert(len(fin), str(initial)+'-'+str(end))        
            initial = input_list[i+1]

    return fin