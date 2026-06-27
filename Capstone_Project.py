
number_of_Students = int(input("Enter total Number of Student: "))
Student_Name=[]
Student_Marks=[]

for i in range(number_of_Students):
    name = str(input(f"Enter Student {i+1} Name: "))
    Student_Name.append(name)
    marks = int(input(f"Enter Student {i+1} Marks: "))
    Student_Marks.append(marks)



for name,marks in zip(Student_Name,Student_Marks):
    print("-----------------------------Results-------------------------------")
    print("------------------------Sir. J.J. School----------------------------")
    print("Class: 8")
    print(f"Student_name: {name}")
    print("---------------------------------------------------------------------")

    if marks > 0 and marks < 100:
        if marks >= 85:
            print("Student Pass with Grade A")
        elif marks >= 70:
            print("Student Pass with Grade B")
        elif marks >= 60:
            print("Student Pass with Grade C")
        elif marks >= 50:
            print("Student Pass with Grade D")
        elif marks >= 40:
            print("Student Pass with Grade P")
        else:
            print("Student Failed with Grade F")
    else:
        print("Negative Number and numbers more than 100 are not allowed")
    

    print("---------------------------------------------------------------------")

            
