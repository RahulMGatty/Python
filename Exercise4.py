 #Create a List n Integers and perform linear search on the list to find a number which is user input.
lists=[]
n=int(input("Enter the number of element:"))
for i in range(n):
    item=int(input(f"Enter {i+1}th element:"))
    lists.append(item)

search=int(input("Enter the element to search:"))
for i in lists:
    if i == search:
        print(f"Element {search} found in ",lists.index(i))
        break
else:
    print(f"Element {search} not found!")