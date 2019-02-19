def selection_sort(a_list):
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)):
            if a_list[j] < a_list[i]:
                a_list[j], a_list[i] = a_list[i], a_list[j]
    return a_list