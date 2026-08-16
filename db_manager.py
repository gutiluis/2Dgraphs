from db import (
    initialize_db,
    add_user,
    authentication_user,
    update_password,
    delete_user,
)

from graph2d import graph_vectors


def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if authentication_user(username, password):
        print(f"[INFO] Welcome, {username}.")
        return username

    print("[ERROR] Invalid username or password.")
    return None


def user_menu(username):
    while True:
        print("\n--- User Menu ---")
        print("1. Graph vectors")
        print("2. Update password")
        print("3. Delete user")
        print("4. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            graph_vectors()

        elif choice == "2":
            new_password = input("Enter new password: ").strip()

            if update_password(username, new_password):
                print("[INFO] Password updated successfully.")
            else:
                print("[ERROR] User not found.")

        elif choice == "3":
            confirmation = (
                input("Are you sure you want to delete your account? (y/n): ")
                .strip()
                .lower()
            )

            if confirmation == "y":
                if delete_user(username):
                    print("[INFO] User deleted successfully.")
                    return

                print("[ERROR] User not found.")

        elif choice == "4":
            print("[INFO] Logged out.")
            return

        else:
            print("[ERROR] Invalid option.")


def main():
    initialize_db()

    while True:
        print("\n=== 2D Grapher ===")
        print("1. Login")
        print("2. Add user")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = login()

            if username:
                user_menu(username)

        elif choice == "2":
            add_user()

        elif choice == "3":
            print("[INFO] Goodbye.")
            break

        else:
            print("[ERROR] Invalid option.")


if __name__ == "__main__":
    main()
