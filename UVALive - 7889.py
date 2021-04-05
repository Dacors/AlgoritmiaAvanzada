import math as mt

while True:
  try:
    N = [int(i) for i in input().split()]  
    N = N[0]
    arr = [int(i) for i in input().split()]  
    ls1 = []
    ls2 = [] 
    area = 0
    angle = 360 / N
    sen_a = mt.sin(mt.radians(angle))
    arr.sort()
    for i in range(len(arr)):
      if i % 2 == 0:
        ls1.append(arr[i])
      else:
        ls2.append(arr[i])

    for i in range(len(ls1)):
      if i + 1 < len(ls1):
        area = area + ((ls1[i] * ls1[i+1] * sen_a)/2)
      if i + 1 < len(ls2):
        area = area + ((ls2[i] * ls2[i+1] * sen_a)/2)

    area = area + ((ls2[0] * ls1[0] * sen_a)/2)
    area = area + ((ls2[-1] * ls1[-1] * sen_a)/2)

    print('{:.3f}'.format(round(area, 3)))
  except:
    break