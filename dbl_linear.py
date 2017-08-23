def dbl_linear(n):
    '''
    u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
    x = 1   ||  y = 2 * x + 1   ||  z = 3 * x + 1
    1           3                   4
    3           7                   10
    4           9                   13
    7           15                  22
    
    dbl_linear(10) should return 22
    '''
    sequence = [1]
    y_numbers = []
    z_numbers = []
    Y = 0
    Z = 0
    
    for i in range(n):
        y = 2 * sequence[i] + 1
        y_numbers.append(y)
        z = 3 * sequence[i] + 1
        z_numbers.append(z)
        if y_numbers[Y] < z_numbers[Z]:
            sequence.append(y_numbers[Y])
            Y += 1
        elif z_numbers[Z] < y_numbers[Y]:
            sequence.append(z_numbers[Z])
            Z += 1
        else:
            sequence.append(y_numbers[Y])
            Y += 1
            Z += 1

    return sequence[n]

print(dbl_linear(20))

# ALTERNATE SOLUTION

def dbl_linear(n):
    arr = [1]
    xi = yi = 0
    
    for i in range(n):
        x,y = arr[xi]*2+1, arr[yi]*3+1 
        arr.append( min(x,y) )
        if min(x,y) == x:
            xi += 1
        if min(x,y) == y:
            yi += 1
    return arr[n]
    
