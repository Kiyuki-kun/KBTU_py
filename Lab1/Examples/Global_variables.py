'''
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
'''

'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc() => Python is fantastic

print("Python is " + x) => Python is awesome
'''

'''
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
'''

'''
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

print("Python is " + x) => Python is fantastic
'''

