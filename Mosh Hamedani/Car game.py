# help
# start - to start the car
# stop - to stop the car
# exit - exit from the car
# wrong command - Sorry, I don't understand that...
print("*" * 40)
print("  You're in the driving sit of the car\n          🚙 Let's drive it 🚙")
print("*" * 40)

started = False
while True:
    command = input("< ").lower()
    if command == "start":
        if started:
            print("Hey, your car is already started 🚙.")
        else:
            started = True
            print("Car started... Ready to go! 🚙")

    elif command == "stop":
        if not started:
            print("Car is already stopped. 🚙")
        else:
            started = False
            print("Car stopped... 🚙")
    elif command == "exit":
        print("You got out of the car! 🚙")
        break
    elif command == "help":
        print("start - to start the car\n"
              "stop - to stop the car\n"
              "exit - exit from the car\n")
    else:
        print("Invalid...")
        print("Type <help> to see guidelines")