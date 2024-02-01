def unique_list(lst):
    unique = []
    for elem in lst:
        if elem not in unique:
            unique.append(elem)
    print(unique)
    
lst = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list(lst)