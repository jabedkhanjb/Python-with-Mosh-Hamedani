# help
# start - to start the car
# stop - to stop the car
# exit - exit from the car
# wrong command - Sorry, I don't understand that...
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Hello, Your Car is already started...🚙!")
        else:
            started = True
            print("Car started, Ready to go...🚙!")
    elif command == "stop":
        if not started:
            print("Engine is already stopped...🚙!")
        else:
            started = False
            print("Car stopped...🚙")
    elif command == "exit":
        print("You got out of the car! 🚙")
        break

    elif command == "help":
        print("start - to start the car.\n"
              "stop - to stop the car.\n"
              "exit - exit from the car.\n")
    else:
        print("Invalid Command.\nPlease type <help> for the guidelines.")