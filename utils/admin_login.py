from utils.library_management_system import library_management

admin_data = {
    "Ayush": "pass123",
    "Ashish": "pass456",
    "Om": "pass789"
}

def admin_login():
    while True:
        print(f"---" * 8, " Log in System ", "---" * 8, "\n")
        username = input("Enter user name (or type 'q' to Exit): ").title()
        if username.lower() == "q":
            print("Exiting the system.\n")
            print("---" * 8)
            break
        elif username == "":
            print("Username cannot be empty.")
            continue
        elif username not in admin_data:
            print("User not found. Try Again.")
            continue
        else:
            tries = 3
            while tries > 0:
                ask_pass = input("Enter password: ")
                if ask_pass == admin_data[username]:
                    print("\nAccess Granted\n")
                    library_management()
                    break
                else:
                    tries -= 1
                    if tries == 0:
                        print("No tries left. Exiting the system.\n")
                        break
                    else:
                        print(f"Incorrect Password. Number of tries left: {tries}")
