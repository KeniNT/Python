import bcrypt
import os

# File to store user data
USER_DATA_FILE = 'users.txt'


def hash_password(password: str) -> bytes:
    """Hashes the password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(hashed: bytes, password: str) -> bool:
    """Checks if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


def register_user(username: str, password: str) -> bool:
    """Registers a new user with the provided username and password."""
    if user_exists(username):
        print(f"Username '{username}' already exists. Please choose another.")
        return False

    hashed_password = hash_password(password)
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f"{username}:{hashed_password.decode('utf-8')}\n")
    print(f"User '{username}' registered successfully.")
    return True


def user_exists(username: str) -> bool:
    """Checks if a user already exists."""
    if not os.path.exists(USER_DATA_FILE):
        return False

    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_username, _ = line.strip().split(':')
            if stored_username == username:
                return True
    return False


def login_user(username: str, password: str) -> bool:
    """Logs in a user with the provided username and password."""
    if not os.path.exists(USER_DATA_FILE):
        print("No users registered yet.")
        return False

    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_username, stored_hashed_password = line.strip().split(':')
            if stored_username == username:
                if check_password(stored_hashed_password.encode('utf-8'), password):
                    print(f"User '{username}' logged in successfully.")
                    return True
                else:
                    print("Incorrect password.")
                    return False
    print(f"Username '{username}' not found.")
    return False


def main():
    while True:
        print("\n--- User Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)

        elif choice == '3':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
