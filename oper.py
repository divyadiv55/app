from utils import *
from tabulate import tabulate

def register():
    data=read_json()
    id=len(data["students"])+1
    stud_data={
        "id":id,
         "name":input("Enter student name: "),
         "age":input("Enter a student age: "),
         "Address":input("Enter a student address: "),
         "Course":input("Enter student course: ")
          
     }
    data["students"].append(stud_data)
    write_json(data)
    print("Student registered successfully!")
    
     

def view_std():
    data=read_json()
    tab=[]
    for stud in data["students"]:
        temp=[stud["id"],stud["name"],stud["age"],stud["Address"],stud["Course"]]
        tab.append(temp)
    print(tabulate(tab,headers=["id","name","age","Address","Course"]))
    
        

def update():
    view_std()
    data=read_json()
    try:
        id=int(input("Enter a student id: "))
    except:
        print("Invalid choice!!")
        id=0
    flag="a"
    for stud in data["students"]:
            if stud["id"]==id:
                flag="b"
                choice=input("enter your choice[1,2,3,4,5]: \n1.name,\n2.age,\n3.Adress,\n4.Course\n5.all the above")
                if choice in ["1","2","3","4","5"]:
                    if choice=="1":
                        stud["name"]=input("enter student name: ")
                    elif choice=="2":
                        stud["age"]=input("enter student age: ")
                    elif choice=="3":
                        stud["Address"]=input("enter student adddress: ")
                    elif choice=="4":
                        stud["Course"]=input("enter student course: ")
                    else:
                        stud["name"]=input("enter student name: ")
                        stud["age"]=input("enter a student age: ")
                        stud["Address"]=input("enter a student address: ")
                        stud["Course"]=input("enter a course: ")
                    write_json(data)
                    print("data updated successfully")
                else:
                    print("invalid choice!!")
                    
                    
    if flag=="a":
        print(f"{id}is not found ")

def delete():
    view_std()
    data=read_json()
    try:
        id=int(input("enter a student id: "))
    except:
        print("invalid choice!")
        id=0
    flag="y"
    for stud in data["students"]:
        if stud["id"]==id:
            flag="n"
            data["students"].remove(stud)
            i=1
            for stud_1 in data["students"]:
                stud_1["id"]=i
                i+=1
            write_json(data)
            print("data is delete successfully!!")
    if flag=="y":
        print(f"{id} not found")
      
        
        