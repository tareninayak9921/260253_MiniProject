def display_record():
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