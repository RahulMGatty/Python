#Create an empty list. Input ‘n’ items. Count total number of Odd, Even, and zero items in the list and display the contents of new lists.
number=[]
n=int(input("Enter number of list elements:"))

for i in range(n):
    item=int(input(f"element {i+1}:"))
    number.append(item)
print("List:",number)

odd=[]
even=[]
negative=[]
zerocount=0

for i in number:
    if i==0:
        zerocount+=1
    elif i%2==0:
        even.append(i)
    elif i<0:
        negative.append(i)
    else:
        odd.append(i)
    
print(f"Odd numbers {odd}\nEven numbers {even}")
print(f"Negative numbers found {negative}\nCount of zeros found {zerocount}")