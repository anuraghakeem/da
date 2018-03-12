def binarySearch(arr, l, r, x):
    if (r >= l):
        mid = int(l + (r - l)/2)
        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1
num=int(input('enter the number of elements in array'))
arr = list()
for i in range(num):
  arr.append(int(input('enter the elements')))
x = int(input('enter the number to be searched'))
result = binarySearch(arr, 0, (len(arr)-1), x)
if result != -1:
    print ("Element is present at index",result)
else:
    print ("Element is not present in array")