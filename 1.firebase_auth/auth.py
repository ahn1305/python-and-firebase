import pyrebase

#Config
firebaseConfig = {

}


#initialize app
firebase = pyrebase.initialize_app(firebaseConfig)

# initialize auth
auth = firebase.auth()



def signup(nuser,npass):
	try:
		auth.create_user_with_email_and_password(nuser,npass)  # creates a user in firebase
		print("SignUp successful")
	except:
		print("Email already exists")


def signin(user,passw):
	try:
		auth.sign_in_with_email_and_password(user,passw) # checks if user data already in firebase, if true allows to sign in
		print("SignIn successful")
	except:
		print("Invalid Email of password !, Try again")



def main():
	print("Welcome to firebase authentication\n")
	print("************************************\n")
	print("Options: \n")
	print("1. SignUp\n")
	print("2. SignIn\n")

	choice = int(input("Enter your choice: "))

	if choice == 1:
		nemail = input("Enter email: ")
		npassword = input("Enter password: ")
		if len(npassword) < 6:
			print("Length of password must my minimum 6 values")
			exit()

		confirm_pass = input("Re-enter password: ")

		if npassword == confirm_pass:
			signup(nemail,npassword)

	elif choice == 2:
		email = input("Enter email: ")
		password = input("Enter password:  ")
		signin(email,password)


main()