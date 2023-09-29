import hashlib
import getpass

manager = {}

def generate_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    manager[username] = hashed_password
    print('Account created successfully!')

def login():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in manager.keys() and manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password")

def main():
    while True:
        choice = input("Enter 1 to create account, 2 to login or 0 to exit: ")
        if choice == "1":
            generate_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
