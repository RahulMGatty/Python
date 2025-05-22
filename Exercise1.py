#Generate prime and fibnacci within the given range by user input
start=int(input("enter the Start:"))
end=int(input("Enter the end:"))

def prime(start,end):
    primenumber=[]
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                primenumber.append(i)
    return primenumber

def fibonacci(s,e):
    fibo=[]
    a,b=0,1
    while a<e:
        fibo.append(a)
        a,b=b,a+b
    return fibo

primenumber=prime(start,end)
fibonacci=fibonacci(start,end)

print(f"Prime numbers for the given start value {start} and end value {end} is {primenumber}")
print(f"The fibonacci series for the given start value {start} and end value {end} is {fibonacci}")
print("Done!")
