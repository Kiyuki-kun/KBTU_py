'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) => ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
'''

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) => ['Kiwi', 'Orange', 'banana', 'cherry']
'''

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) => ['cherry', 'Kiwi', 'Orange', 'banana']
'''

'''
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) => [100, 82, 65, 50, 23]
'''

'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) => [50, 65, 23, 82, 100]
'''