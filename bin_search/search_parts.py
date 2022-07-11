n_store = int(input())
list_store = list(map(int,input().split()))
n_customer = int(input())
list_customer = list(map(int, input().split()))

list_store.sort()

def find_item(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return find_item(array, target, start, mid - 1)
  else:
    return find_item(array, target, mid + 1, end)

for i in list_customer:
  if (find_item(list_store, i, 0, n_store - 1)):
    print("Yes")
  else:
    print("No")
