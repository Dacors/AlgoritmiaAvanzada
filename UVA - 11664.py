#1 nort
#2 sur
#3 oriente
#4 occid
def invert_val(univ, x ,y):
    if univ[x][y] == 1:
        univ[x][y] = 0
    else:
        univ[x][y] = 1
    return univ

def next_pos(x, y, orient):
    if orient == 1:
        x -= 1
    elif orient == 3:
        y += 1
    elif orient == 2:
        x += 1
    elif orient == 4:
        y -= 1
    return x, y

def next_or(x, y, curr_or, univ):
    if univ[x][y] == 1:
        if curr_or == 1:
            return 3
        elif curr_or == 3:
            return 2
        elif curr_or == 2:
            return 4
        elif curr_or == 4:
            return 1
    else:
        if curr_or == 1:
            return 4
        elif curr_or == 3:
            return 1
        elif curr_or == 2:
            return 3
        elif curr_or == 4:
            return 2

def create_universe(n):

    univ = [[0 for i in range(n)] for j in range(n)]
    return univ

def fill_universe(univ, binary):

    arr_bin = list(map(int, str(binary)))

    arr_bin = arr_bin[::-1]

    n = len(univ)*len(univ)
    counter  = 0

    for i in range(len(arr_bin), n):

        arr_bin.append(0)

    for i in range(len(univ)):

        for j in range(len(univ)):

            univ[i][j] = arr_bin[counter]
            counter = counter + 1
        univ[i] = univ[i][::-1]
    return univ

def run_bitch_run(univ,x,y):
    x = n - x
    y = y - 1
    orient = 1
    
    while True:
        if  x == 0 and y == len(univ) - 1 :
            return 'Yes'
            break
        prev_x, prev_y = x ,y
        orient = next_or(x ,y, orient, univ)
        x , y = next_pos(x ,y, orient)
        if x < 0 or x >= len(univ) or y < 0 or y >= len(univ):
            return 'Kaputt!'
            break
        univ = invert_val(univ,prev_x,prev_y)

while True:
  
    arr_m = [int(i) for i in input().split()]

    n = arr_m[0]
    c = arr_m[1]
    x = arr_m[2]
    y = arr_m[3]
    if n == c == x == y == 0:
        break
    print(run_bitch_run(fill_universe(create_universe(n), bin(c)[2:]),y, x))