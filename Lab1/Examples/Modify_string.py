'''
a = "Hello, World!"
print(a.upper()) => HELLO, WORLD!
'''

'''
a = "Hello, World!"
print(a.lower()) => hello, world!
'''

'''
a = "   Hello, World!   "
print(a.strip()) # returns "Hello, World!"
'''

'''
a = "Hello, World!"
print(a.replace("H", "J")) => Jello, World!
'''

'''
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
'''

'''
a = "Hello"
b = "World"
c = a + b
print(c) => HelloWorld
'''

'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) => I want 3 pieces of item 567 for 49.95 dollars.
'''

'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) => I want to pay 49.95 dollars for 3 pieces of item 567.
'''

'''
txt = "We are the so-called "Vikings" from the north." => Error( "Vikings" are between 2 str)
'''

'''
txt = "We are the so-called \"Vikings\" from the north." => We are the so-called "Vikings" from the north.
'''