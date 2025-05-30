def get_door_choice():
    choice = input("Pick a door. (1, 2, or 3): ")
    while choice not in ["1", "2", "3"]:
        choice = input("Pick a door. (1, 2, or 3): ")
    return choice
choice = get_door_choice()

if choice == "1":
    print("1")
elif choice == "2":
    print("2")
elif choice == "3":
    print("3")