def solve(numheads, numlegs):
    for chicken in range(numheads + 1):
        rabbit = numheads - chicken
        if 2*chicken + 4*rabbit == numlegs:
            print("Chickens = " + chicken,"Rabbits = " + rabbit)
            
a = int(input("Number of Heads = "))
b = int(input("Number of Legs = "))
solve(a,b) 