import array
array = []
while True:
      number = int(input(("enter random numbers ....")))
      array.append(number)
      if len(array) > 5:
          break
n = len(array)      
for i in range(n-1):
    swap = False   
    for j in range (n-i-1):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
            swap = True
    if not swap:
       break

print(array)
