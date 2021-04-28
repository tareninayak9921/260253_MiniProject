from modules import displayRecord, updateRecord, deleteRecord, searchRoll, searchName, addRecord


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
        addRecord.add_record()
    elif n == 2:
        displayRecord.display_record()
    elif n == 3:
        searchName.search_student_name()
    elif n == 4:
        searchRoll.search_student_roll()
    elif n == 5:
        deleteRecord.delete_record()
    elif n == 6:
        updateRecord.update_record()

