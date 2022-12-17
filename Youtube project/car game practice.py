started = False
while True:
    engine = input("> ").lower()
    if engine == "start":
        if started:
            print("Your car is already started...🚙")
        else:
            started = True
            print("Car started, Ready to go...🚙")
    elif engine == "stop":
        if not started:
            print("Engine is already stopped...🚙")
        else:
            started = False
            print("Car stopped.")
    elif engine == "exit":
        print("You got out of the car...🚙")
        break
    elif engine == "help".lower():
        print("""
        start -- to start the car
        stop -- to stop the car
        exit -- to get out of the car
        """)

    else:
        print("Invalid command.\nPlease type <help> for the guidelines.")