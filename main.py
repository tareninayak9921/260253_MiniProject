import os
z = 1
while True:
    print("\n 1. Add Record")
    print("\n 2. Display All Record")
    print("\n 3. Search Student Record By Name")
    print("\n 4. Search Student Record By Roll No")
    print("\n 5. Delete Student Record By Name")
    print("\n 6. Update Student Record")
    print("\n 7. Exit")

    n = int((input("Enter Your Choice:  ")))
    if n == 7:
        break
    elif n == 1:
        print("Enter The Student Details\n")
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        cls = input("Enter Class: ")
        fee = input("Enter Fees: ")
        percentage = input("Enter The Percentage: ")
        file = open("Record/student.txt","a")
        file.write(name+"-"+roll+"-"+cls+"-"+fee+"-"+percentage+"\n")
        file.close()
    elif n == 2:
        print("\n\n List Of Present Records\n\n")
        print("NAME---ROLLNO---CLASS---FEES---PERCENTAGE")
        file = open("Record/student.txt", "r")
        while True:
            content = file.readline()
            length = len(content)
            if length == 0:
                break
            print(content.strip())
        file.close()
    elif n == 3:
        search = input("Enter Student Name: ")
        file = open("Record/student.txt", "r")
        flag = 0
        while True:
            content = file.readline()
            length = len(content)
            if length == 0:
                break
            arr = content.split("-")
            if arr[0] == search:
                print("\n Record Found!!! ")
                print("Name: ", arr[0])
                print("Roll No: ", arr[1])
                print("Class: ", arr[2])
                print("Fees: ", arr[3])
                print("Percentage: ", arr[4])
                flag=1
                break
            if flag == 0:
                print("\n Record Not Found!!!")
            file.close()




