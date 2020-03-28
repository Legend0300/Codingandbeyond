names = {"ahmed" : "29th" , "hamza" : "30th"}
while True:
    print("Please enter the name to know the BD")
    name = input()
    if name in names:
        print(names[name] , "is the birthday of " , name)
    else:
        print("sorry" , name , "is not present in the list")
        break
    

    