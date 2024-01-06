from oper import *
print("Welcome to the students registeration system!")

while True:
    print()
    print("what would you like to do today?")
    print("1.student registeration\n2.view student\n3.update student\n4.delete student ")
    choice=input("Enter your choice: ")
    if choice in ["1","2","3","4"]:
        if choice=="1":
            print("you have choosen registeration module")
            register()
        elif choice=="2":
            print("you have choosen view module")
            view_std()
        elif choice=="3":
            print("you have choosen update module")
            update()
        else:
            print("you have choosen delete module")
            delete()
    else:
        print("Invalid choice!")
    con=input("you want to continue application[y/n]: ")
    if con=="y"or con=="Y":
        continue
    else:
        print("Thanks for using application!!")
        exit()
        