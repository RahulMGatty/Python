#create a tuple with different data types and print each element  also check for a element if exists in tuple.
tup=(1,2.0,'apple')
print("tuple :",tup)

search=2.0

if search in tup:
    print(f"Search Element {search} exists in tuple")
else:
    print(f"Search Element {search} doesnt exist in tuple")
