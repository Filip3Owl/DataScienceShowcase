result = []
for i in range(15):
    for y in range(15):
        if i == 0 or y == 0 or i == 14 or y == 14:
            result.append((i, y))
        elif (i + y) % 2 == 0:
            result.append((i, y))
# Uncomment the line below to print the result
#print(f'Result: {result}')

for x in range(10):
    if x > 3:
        # Uncomment the line below to print the value of x
        #print(f'Value of x is {x}, which is greater than 3')

