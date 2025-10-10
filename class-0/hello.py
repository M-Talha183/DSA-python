arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
# reverse arr 
for i in range(len(arr)-1, -1 ,-1):
    print(arr[i], end=" ")
# find the miximim value in arr
min_value = arr[0]

for i in arr:
    if i < min_value:
        min_value = i 
print("\nMinimum value in arr is:", min_value)
# find the maximum value in arr

max_num = arr[0]
for i in arr :
    if i > max_num:
        max_num = i 
print("maximum value in array is ",max_num) 