import os
def delete_record():
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
