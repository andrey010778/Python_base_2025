from Logic import show_all, add_record, update_record, delete_record, conn_close
def display_menu():
    print("1. Add record")
    print("2. Update record")
    print("3. Delete record")
    print("4. Show all records")
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
            add_record()
        elif choice == 2:
            update_record()
        elif choice == 3:
            delete_record()
        elif choice == 4:
            show_all()
        elif choice == 5:
            conn_close()
            print("Thanks, bye")
            break


if __name__ == "__main__":
    main()
