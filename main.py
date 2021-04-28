import os
z=1
while(True):
    print("\n 1. Add Record")
    print("\n 2. Display All Record")
    print("\n 3. Search Student Record By Name")
    print("\n 4. Search Student Record By Roll No")
    print("\n 5. Delete Student Record By Name")
    print("\n 6. Update Student Record")
    print("\n 7. Exit")

    n=int(print(input("Enter Your Choice:  ")))
    if(n==7):
        break
    elif(n==1):
        print("Enter The Student Details\n")
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")


