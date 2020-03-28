def input_name():
    student_name = []
    while True:
        print("Please enter the Names of the students")
        names = input()
        if names ==  "exit":
            print(student_name)
            return(student_name)
        else:
            student_name.append(names)
            continue
        
subjects = ["phy" , "maths" , "udru"]


def input_marks():
    for student in input_name(): 
        student_marks = []
        phy_marks = input("Enter Phy marks please: ")
        student_marks.append(phy_marks)
        maths_marks = input("Enter maths marks please: ")
        student_marks.append(maths_marks)
        udru_marks = input("Enter udru marks please: ")
        student_marks.append(udru_marks)
        print(student_marks)
        
input_marks()




