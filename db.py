#!/usr/bin/env python3

# file: db.py
# descr: db admin

import os


def initialize_db():
    if not os.path.exists("users_db.txt"):
        with open("users_db.txt", "w") as file:
            file.write("username,user_id,password\n")
        print("[INFO] Database initialized successfully.")


def add_user():
    with open("users_db.txt", "a") as file:
        username = input("Enter user: ").strip()
        user_id = input("Enter user_id: ").strip()
        password = input("Enter password: ").strip()
        file.write(f"{username},{user_id},{password}\n")
    print(f"[INFO] User {username} added successfully.")


# helper
def read_users():
    users = []
    with open("users_db.txt", "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            username, user_id, password = line.strip().split(",")

            users.append(
                {"username": username, "user_id": user_id, "password": password}
            )
    return users


# if add_user() # if read_users()
def authentication_user(username, password):
    users = read_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False


# if not login # if read_users() # if add_user()
def update_password(username, new_password):
    users = read_users()
    updated = False
    with open("users_db.txt", "w") as file:
        file.write("username,user_id,password\n")
        for user in users:
            if user["username"] == username:
                user["password"] = new_password
                updated = True
            file.write(f"{user['username']},{user['user_id']},{user['password']}\n")
    if updated:
        print(f"Password for {username} updated successfully.")
    else:
        print(f"User {username} not found.")


# if not login
def delete_user(username):
    users = read_users()
    updated_users = [user for user in users if user["username"] != username]
    with open("users_db.txt", "w") as file:
        file.write("username,user_id,password\n")
        for user in updated_users:
            file.write(f"{user['username']},{user['user_id']},{user['password']}\n")
    if len(updated_users) == len(users):
        return False
    print(f"User {username} deleted successfully.")
    return True
