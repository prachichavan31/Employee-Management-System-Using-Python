class EmployeeManager:
    #list 
    def __init__(self):
        self.employee=[]

    # import txt
    def load_data(self):
        try:
            with open("employee.txt","r") as f:
                for line in f:
                    eid,name,age,salary=line.strip().split(",")
                    self.employee.append({
                        "eid":int(eid),
                        "name":name,
                        "age":int(age),
                        "salary":int(salary)
                    })
        except FileNotFoundError:
            print("File not found!")

    # read function
    def read_data(self):
        print("Employee details are: ")
        for data in self.employee:
            print(f"id:{data['eid']},name:{data['name']},age:{data['age']},salary:{data['salary']}")

    # save data to file
    def save_data(self):
        with open("employee.txt","w") as w:
            for e in self.employee:
                w.write(f"{e['eid']},{e['name']},{e['age']},{e['salary']}\n")

    # add employee
    def add_employee(self):
        eid=int(input("Enter id: "))
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        salary=int(input("Enter salary: "))

        self.employee.append({
            "eid":eid,
            "name":name,
            "age":age,
            "salary":salary
        })

        self.save_data()
        print("Data added!")

    # update employee
    def update_employee(self):
        eid=int(input("Enter id to update: "))
        for i in self.employee:
            if eid == i['eid']:
                print("Employee found!")
                new_name=input("Enter new name: ")
                new_age=int(input("Enter new age: "))
                new_salary=int(input("Enter new salary: "))
                i['name'] = new_name
                i['age'] = new_age
                i['salary'] = new_salary

        self.save_data()
        print("Data is updated!!")

    # delete employee
    def delete_employee(self):
        eid=int(input("Enter id to delete: "))
        found=False
        for i in self.employee:
            if eid == i['eid']:
                self.employee.remove(i)
                found = True
                break
        if found:
            self.save_data()
            print("Employee removed successfully..")
        else:
            print("Employee not found!")


# obj creation
obj=EmployeeManager()
obj.load_data()
while True:
    print("1.Read Employee")
    print("2.Add Employee")
    print("3.Update Employee")
    print("4.Delete Employee")
    print("5.Exit")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        obj.read_data()
    elif ch == 2:
        obj.add_employee()
    elif ch == 3:
        obj.update_employee()
    elif ch == 4:
        obj.delete_employee()
    elif ch == 5:
        break
