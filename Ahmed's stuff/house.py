name = input("please enter the name: ")
lenght = len(name)
if lenght < 3:
    print("the name is too short")
elif lenght > 50:
    print("the name is too long")
else:
    print("name looks good")
    
