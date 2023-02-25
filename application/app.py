# imports

from getpass import getpass
import pyrebase
import os

# Configuration for Pyrebase
firebaseConfig = {
 
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)

# Get the Firebase authentication instance
auth = firebase.auth()

# Get the Firebase storage instance
storage = firebase.storage()

    
# Sign up a new user
# posible errors: user already exists or password length is low
def signup():
    email = input("Enter your email: ")
    password = getpass(prompt="Enter your password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("User created successfully.")
    except:
        print("Error creating user or user data exists")

# Sign in an existing user
def signin():
    email = input("Enter your email: ")
    password = getpass(prompt = "Enter your password: ")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Sign in successful.")
        return user
    except:
        print("Error signing in.")
        return None

# Store an image in Firebase storage
def store_image(user):
    path = input("Enter the path to the image file: ")
    filename = os.path.basename(path) # extract filename from the input path
    try:
        storage.child(filename).put(path, user['idToken'])
        print("Image stored successfully.")
        print(storage.child(filename).get_url(user['idToken']))
    except:
        print("Error storing image.")


# Main loop of the application
def main():
    user = None
    while True:
        print("\n1. Sign up\n2. Sign in\n3. Store image\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            signup()
        elif choice == "2":
            if user:
                print("You are already signed in")
            else:
                user = signin()
        elif choice == "3":
            if user:
                store_image(user)
            else:
                print("Please sign in first.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

main()
