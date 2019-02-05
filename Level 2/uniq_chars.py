def unique_chars_in_string(input_string):
    if input_string == "":
        return True
    for i in range(0, len(input_string)-1):
        pointer = input_string[i]
        for j in range(i+1, len(input_string)-1):
            if pointer == input_string[j]:
                return False
    return True