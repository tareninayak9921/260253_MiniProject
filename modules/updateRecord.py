import os

def update_record():
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