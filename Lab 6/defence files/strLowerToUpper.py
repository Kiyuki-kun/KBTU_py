str = input("Enter a string: ")
def lowerToUpper(string):
    for c in string:
        yield c.upper()
         
new_str = lowerToUpper(str)
for i in new_str:
    print(i)