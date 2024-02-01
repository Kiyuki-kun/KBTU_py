def find_common_elements(list1, list2):
    common_elements = []
    set2 = set(list2)

    for element in list1:
        if element in set2:
            common_elements.append(element)

    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(find_common_elements(list1,list2))