import pyrebase

#Config
firebaseConfig = {

}


#initialize app
firebase = pyrebase.initialize_app(firebaseConfig)

# initialize storage
storage = firebase.storage()

# Store data
filename = input("Enter name of file that you want to store: ")
cloudfilename = input("Enter name for file on cloud: ")
storage.child("data/textfiles/"+cloudfilename).put(filename)

# Retrive data
get_filename = input("Enter name of file that you want to fetch: ")
print(storage.child("data/textfiles/"+get_filename).get_url(None))

#Download Data
down_filename = input("Enter name of file that you want to download: ")
storage.child("data/textfiles/"+down_filename).download("","cloud.txt")
