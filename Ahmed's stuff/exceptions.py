while True:
    print("please guess the number")
    number = int(input())
    if number == 11:
        print("you guessed the right number")
        break
    elif number != 11:
        try:
            print(x)
        except Exception:
            print("this  is not equal to the number")
        else:
            print("you guessed the right number")
        finally:
            print("please try again")
