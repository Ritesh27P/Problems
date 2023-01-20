def count_substring(string, sub_string):
    value = 0
    current_position = 0
    for i in range(0, len(string)-len(sub_string)+1):
        if sub_string == (string[current_position: (current_position+len(sub_string))]):
            value += 1
        current_position += 1
    return value
