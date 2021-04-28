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
                flag = 1
                break
        if flag == 0:
            print("\n Record Not Found!!!")
        file.close()
    elif n == 4:
        search = input("Enter Student Roll No: ")
        file = open("Record/student.txt", "r")
        flag = 0
        while True:
            content = file.readline()
            length = len(content)
            if length == 0:
                break
            arr = content.split("-")
            if arr[1] == search:
                print("\n Record Found!!! ")
                print("Name: ", arr[0])
                print("Roll No: ", arr[1])
                print("Class: ", arr[2])
                print("Fees: ", arr[3])
                print("Percentage: ", arr[4])
                flag = 1
                break
        if flag == 0:
            print("\n Record Not Found!!!")
        file.close()
    elif n == 5:
        search = input("Enter Student Name: ")
        file1 = open("Record/student.txt", "r")
        file2 = open("Record/temp.txt", "w")
        flag = 0
        while True:
            content = file1.readline()
            length = len(content)
            if length == 0:
                break
            arr = content.split("-")
            if arr[0] != search:
                file2.write(content)
            if arr[0] == search:
                flag = 1
        file1.close()
        file2.close()
        if flag == 1:
            print("Record Deleted Successfully!!!")
            os.remove("Record/student.txt")
            os.rename("Record/temp.txt", "Record/student.txt")
        elif flag == 0:
            print("Deletion Unsuccessful As Record Not Found!!!")

    elif n == 6:
        flag = 0
        search = input("Enter Student Name: ")
        file1 = open("Record/student.txt", "r")
        file2 = open("Record/temp.txt", "w")
        flag = 0
        while True:
            content = file1.readline()
            length = len(content)
            if length == 0:
                break
            arr = content.split('-')
            if arr[0] == search:
                print("Current Detail\n", content)
                print("------------------")
                newRoll = input("Do you want to change roll no? Enter the new detail or press enter to continue:  ")
                newClass = input("Do you want to change class? Enter the new detail or press enter to continue:  ")
                newFees = input("Do you want to change fee? Enter the new detail or press enter to continue:  ")
                newPercentage = input("Do you want to change percentage? Enter the new detail or press enter "
                                      "to continue:  ")
                if len(newRoll) == 0:
                    newRoll = arr[1]
                if len(newClass) == 0:
                    newClass = arr[2]
                if len(newFees) == 0:
                    newFees = arr[3]
                if len(newPercentage) == 0:
                    newPercentage = arr[4]
                file2.write(arr[0]+"-"+newRoll+"-"+newClass+"-"+newFees+"-"+newPercentage+"\n")
                flag = 1
            else:
                file2.write(content)
        file1.close()
        file2.close()
        if flag == 1:
            print("Record Updated Successfully!!!")
            os.remove("Record/student.txt")
            os.rename("Record/temp.txt", "Record/student.txt")
        elif flag == 0:
            print("No such record exists!!!")


