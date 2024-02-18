import hashlib
import getpass

manager = {}

def create_account():
    username = input("Please enter your new username: ")
    password = getpass.getpass("Please enter your new password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in manager.keys() and manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password!")

def main():
    while True:
        choice = input("Press 1 to create an account, 2 to login and 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
