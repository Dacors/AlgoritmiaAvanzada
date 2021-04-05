def validate_matrioshka(arr, limit):
    if len(arr) % 2 != 0:
        return False 

    sub_arr = []
    
    if abs(arr[0]) >= limit:
        return False
    
    if arr[0] + arr[-1] != 0:
        psi = 0
        if abs(arr[0]) + abs(arr[-1]) >= limit:
            return False
        while psi + 1 < len(arr):
            for j in range(psi, len(arr)):
                if arr[psi] + arr[j] == 0:
                    sub_arr.append(arr[psi:j+1])
                    psi = j + 1
                    break
                elif j + 2 > len(arr):
                    return False
        for i in range(len(sub_arr)):
            if validate_matrioshka(sub_arr[i],limit) == False:
                return False
    else:
        
        r = 0
        for i in range(len(arr)):
            if arr[0] + arr[i] == 0 and i + 1 < len(arr):
                r = i
        if r > 0:
            if abs(arr[0]) + abs(arr[-1]) >= limit:
                return False
            psi = 0
            while psi + 1 < len(arr):
                for j in range(psi, len(arr)):
                    if arr[psi] + arr[j] == 0:
                        sub_arr.append(arr[psi:j+1])
                        psi = j + 1
                        break
                    elif j + 2 > len(arr):
                        return False
            for i in range(len(sub_arr)):
                if validate_matrioshka(sub_arr[i],limit) == False:
                    return False
        else:
            limit = abs(arr[0])
            arr = arr[1:-1]
            if arr == []:
                return True
            if validate_matrioshka(arr,limit) == False:
                return False
            else:
                return True


while True:
  try:
    arr = [int(i) for i in input().split()]
    if validate_matrioshka(arr,float('inf')) == True:
        print(':-) Matrioshka!')
    else:
        print(':-( Try again.')
  except:
    break