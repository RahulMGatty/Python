# Write a Python function that takes a list of integers as parameter and function should return the maximum and minimum numbers from the list. (don’t use built-in methods)
def maxmin(lists):
    maxs=lists[0]
    mins=lists[0]
    for i in lists:
        if i>maxs:
            maxs=i
        if i<mins:
            mins=i
    return maxs,mins

n=int(input("Enter list elements number:"))
lists=[]
for i in range(n):
    items=int(input(f"Enter {i+1}th element:"))
    lists.append(items)
maxs,mins=maxmin(lists)
print(lists)
print(f"Maxmimum element in given list {maxs} and minimum {mins}")