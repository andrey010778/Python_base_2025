from Logic import show_all
def display_menu():
    print("1. Add")
    print("2. Change")
    print("3. Delete")
    print("4. Show all")
    print("5. Exit")


def get_menu_choice():
    while True:
        user_input = input("Choose a point of menu (1-5): ")
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please input number from 1 to 5.")
        else:
            print("Please input number")


def main():
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            print("You choose point 1")
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            show_all()
        elif choice == 5:
            print("Thanks, bye")
            break


if __name__ == "__main__":
    main()
