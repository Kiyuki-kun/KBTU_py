def all_true(t):
    return all(t)

test_tuple_1 = (True, True, True)
test_tuple_2 = (True, False, True)
test_tuple_3 = (False, False, False)

print(all_true(test_tuple_1))
print(all_true(test_tuple_2))
print(all_true(test_tuple_3))
