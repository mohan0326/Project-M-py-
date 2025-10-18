import hashlib
import os

USERS_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            for line in f:
                username, hashed = line.strip().split(':')
                users[username] = hashed
    return users

def save_user(username, hashed_password):
    with open(USERS_FILE, 'a') as f:
        f.write(f"{username}:{hashed_password}\n")

def register():
    users = load_users()
    username = input("Choose any username: ").strip()
    if username in users:
        print("Username already exists.")
        return
    password = input("Choose any password: ").strip()
    hashed = hash_password(password)
    save_user(username, hashed)
    print("Registration successful.")

def login():
    users = load_users()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    hashed = hash_password(password)
    if users.get(username) == hashed:
        print("Login successful!")
    else:
        print("Invalid username / password.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select any one option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
