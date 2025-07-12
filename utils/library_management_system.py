from utils.crud_operations import add_books, view_books, update_books, delete_books

def library_management():
    while True:
        print(f"---" * 3, "Welcome to Library Management System", f"---" * 3, "\n")
        print("Press:\n(1) - To Add Books\n(2) - To View Books\n(3) - To Update Books\n(4) - To Delete Books\n(5) - To Exit\n")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.\n")
            continue

        if choice == 1:
            add_books()
        elif choice == 2:
            view_books()
        elif choice == 3:
            update_books()
        elif choice == 4:
            delete_books()
        elif choice == 5:
            print("Exiting the Management System...\n")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
