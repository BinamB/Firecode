def merge_ranges(input_range_list):
    if (input_range_list == None or len(input_range_list) <= 1):
        return input_range_list
    out = []
    i = 1
    prev = input_range_list[0]
    while i < len(input_range_list):
        cur = input_range_list[i]
        if (prev.upper_bound >= cur.lower_bound):
            merged = Range(prev.lower_bound, max(prev.upper_bound, cur.upper_bound))
            prev = merged 
        else:
            out.append(prev)
            prev = cur
        i = i + 1
    out.append(prev)
    return out