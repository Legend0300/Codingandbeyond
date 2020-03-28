def get_names(name_for_what):
    names = []
    while True:
        print("Please enter "+str(name_for_what)+" Name or leave blank to stop")
        name = input()
        if name == '' or not name:
            print("You entered " + str(names))
            print("-"*20)
            return names
        names.append(name)


def get_score(student,subject):
    got_marks = False
    marks = 0.0
    try_count = 0
    while not got_marks:
        try:
            print("Please"+"e"*try_count+" enter "+str(student)+"'s marks for subject " + str(subject))
            marks = float(input())
            got_marks = True
        except:
            marks = 0.0
            try_count+=1
    return marks


students = get_names("Student")
subjects = get_names("Subject")
scores = {}

for student in students:
    scores[student] = {}
    for subject in subjects:
        marks = get_score(student,subject)
        scores[student][subject] = marks
print(scores)