import pyrebase

#Config
firebaseConfig = {



#initialize app
firebase = pyrebase.initialize_app(firebaseConfig)

# initialize storage
db = firebase.database()






# Create data

data = {
	"age":20,
	"address": "Japan",
	"employed":False,
	"name":"JJ"
}
db.child("SRM").child("Students").push(data)

# Update and delete (Replace remove with update, and the field in json form )
students = db.child("SRM").child("Students").get()

for student in students.each():
	if student.val()["name"] == "Chandru":
		db.child("SRM").child("Students").child(student.key()).remove()

# Filtering or reading data
students = db.child("SRM").child("Students").order_by_child("age").end_at(20).get()

# for student in students:
# 	print(student.val())