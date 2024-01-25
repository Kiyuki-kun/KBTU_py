'''
thislist = ["apple", "banana", "cherry"]
print(thislist) => ['apple', 'banana', 'cherry']
print(len(thislist)) => 3
print(type(mylist)) => <class 'list'>
print(thislist[1]) => "banana"
print(thislist[-1]) => "cherry"
'''

'''
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
'''

'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) => ['cherry', 'orange', 'kiwi']
print(thislist[:4]) => ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:]) => ['cherry', 'orange', 'kiwi', 'melon', 'mango']
'''

'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) => ['apple', 'blackcurrant', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) => ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) => ['apple', 'watermelon']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) => ['apple', 'banana', 'watermelon', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) => ['apple', 'banana', 'cherry', 'orange']
'''

'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) => ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) => ['apple', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) => ['apple', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry"]
del thislist => deletes the list
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) => Empty list
'''

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist) => ['apple', 'banana', 'mango']
'''