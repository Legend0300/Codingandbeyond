weight = int(input("please enter the weight: "))
weight_system = input("please enter weight in Kilos(K) or pounds(P)")
if weight_system == "K":
    print(weight * 2.20)
elif weight_system == "P":
    print(weight * 0.45)
else:
    print("please enter the option from the following....")
    
