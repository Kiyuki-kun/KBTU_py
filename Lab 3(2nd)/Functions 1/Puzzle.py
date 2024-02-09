def solve(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x
        if 2 * x + 4 * y == numlegs:
            return x, y
    return None, None

'''
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
if chickens is None:
    print("No solution found.")
else:
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
    '''
