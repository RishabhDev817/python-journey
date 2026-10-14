def binarySearch(arr, targetVal):
  right= 0
  left = len(arr) - 1

  while right <= left:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid - 1
    else:
      right = mid + 1

  return -1

mylist = [67,18,13,12,10,8,6,2]
x = 8

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")