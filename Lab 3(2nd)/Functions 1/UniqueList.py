def unique_elements(original_list):
    unique_list = []
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

'''
original_list = [1, 2, 3, 3, 4, 5, 5, 6]
print("Original List:", original_list)
print("Unique Elements:", unique_elements(original_list))
'''