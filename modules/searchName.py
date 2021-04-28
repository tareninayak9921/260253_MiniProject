def search_student_name():
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
