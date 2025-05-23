'''Create a class named Employee containing employee details
 such as Eid, Ename, City, Designation, Bpay, and Category. Include two methods to 
accept values for these data items and printing the details of employee for N employees'''

class Employee:
    def accept(self):
        self.eid=int(input('enter the emp id'))
        self.ename=input('enter the empname')
        self.city=input('enter the emp city')
        self.designation=input('enter the designation')
        self.bpay=float(input('enter the Bpay'))
        self.category=input('enter the category')

    def print(self):
        print("emp id",self.eid)    
        print("emp name",self.ename)
        print("emp city",self.city)
        print("emp designation",self.designation)
        print("emp bpay",self.bpay)
        print("emp category",self.category)

employees=[]

num=int(input("\nenter number of employees"))
for i in range(num):
    print(f"\nenter details for {i+1} emp")
    emp=Employee()
    emp.accept()
    employees.append(emp)

for i,emp in enumerate(employees):
    print(f"\ndetails of {i+1} employee") 
    emp.print()   