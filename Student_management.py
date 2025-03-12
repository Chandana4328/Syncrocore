#You have a list of students names in  a class room. Write a Python program that allows  a user to:
#1.add a new student to the list 
#2.check if the students in present
#3.Show or Display all the students
#4.Exit the program
Student_name=[]
Student_section=[]
Student_Class=[]
Student_Roll_NO=[]
while True:
    print("1.Add new Student_name")
    print("2.Update the Student_list")
    print("3.Display the Students_List")
    print("4.Exit")
    choice=int(input("Enter ur choice->"))
    if choice==1:
        print("Adding new Student to the list------>")
        Name=input("Enter the name of the student->")
        Section=input("Enter the Section of the student->")
        Class_room=int(input("Enter the class of the student->"))
        Roll_NO=int(input("Enter the Roll No of the student->"))
        Student_name.append(Name)
        Student_section.append(Section)
        Student_Class.append(Class_room)
        Student_Roll_NO.append(Roll_NO) 
        print("Student added Successfully ") 
    elif choice==2:
        print("Updating the student list")
        Name=input("Enter the Name of the student")
        if Name in Student_name:
            index=Student_name.index(Name)
            Change_sec=input("Enter the new Section name->")
            Change_Class_Room=input("Enter the new Class Room")
            Change_Roll_NO=int(input("Enter the new Roll No->"))
            Student_section[index]=Change_sec
            Student_Roll_NO[index]=Change_Roll_NO
            Student_Class[index]=Change_Class_Room
            print(f"Student List Updated {Student_name[index]} now is in {Student_section[index]},{Student_Roll_NO[index]},{Student_Class[index]}")
        else:
            print("Student not found")
    elif choice==3:
        print("The Students Are----->")
        if not Student_name:
            print("Student not there in the class ")
        else:
            for i in range(len(Student_name)):
                print(f"{Student_name[i]},{Student_section[i]},{Student_Roll_NO[i]},{Student_Class[i]}")
    elif choice==4:
        print("Exiting the Program")
        break
    else:
        print("Invalid Choice")
        

           