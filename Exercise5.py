#Write a function that returns the second-largest element in a tuple of integers.
#Add, remove, and insert elements in the list.
def secondLargest(l):
    l.sort()
    secondLargest=l[-2]
    return secondLargest

n=int(input("Enter the number of list elements:"))
lists=[]
for i in range(n):
    item=int(input(f"Enter the {i+1}th element"))
    lists.append(item)
print(lists)
sl=secondLargest(lists)
print(f"Second Largest element is {sl}")