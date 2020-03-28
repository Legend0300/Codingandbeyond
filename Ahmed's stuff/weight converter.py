help = '''here are some commands:
start: To start the caer
stop; To stop the car
quit: To exit the car'''
start = "Ther car has been started"
stop = "the car has benn stopped"
options = input(">")
if options == "help":
    print(help)
elif options == "start":
    print(start)
elif options == "stop":
    print(stop)
elif options == "exit":
    print("you have exitted the car")
else:
    print("I don't understand that...")


