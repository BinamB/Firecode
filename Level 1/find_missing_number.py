def find_missing_number(list_numbers):
    for i in range(0, len(list_numbers)-1):
        if list_numbers[i] != list_numbers[i+1]-1:
            return list_numbers[i]+1