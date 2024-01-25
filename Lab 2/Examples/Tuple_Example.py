'''
thistuple = ("apple",)
print(type(thistuple)) => <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) => <class 'str'>
'''

'''
A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
'''

'''
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
'''

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) => ('cherry', 'orange', 'kiwi')
'''

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) => ('orange', 'kiwi', 'melon')
'''

'''
Change Tuple Values

Once a tuple is created, you cannot change its values.
Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back into a tuple.
'''

'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) => apple
print(yellow) => banana
print(red) => ['cherry', 'strawberry', 'raspberry']
'''

'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''