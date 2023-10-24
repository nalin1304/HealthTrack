import pymongo

# Replace the connection string with your own MongoDB connection string
client = pymongo.MongoClient("mongodb+srv://HealthTrack:HealthTrack@cluster0.azdhcau.mongodb.net/?retryWrites=true&w=majority")

db = client["HealthTrack"]
student_data = db["student_data"]

# name, class (standard), age, weight, height, blood group, blood pressure, pulse, vision, ear, squint, throat

def add_student_data(name, standard, age, weight, height, blood_group, blood_pressure, pulse, vision, ear, squint, throat):
    student = {
        "name": name,
        "class": standard,
        "age": age,
        "weight": weight,
        "height": height,
        "blood_group": blood_group,
        "blood_pressure": blood_pressure,
        "pulse": pulse,
        "vision": vision,
        "ear": ear,
        "squint": squint,
        "thorat": thorat
    }
    student_data.insert_one(student)
for i in range(0,15):
    name = input("Enter name: ")
    standard = input("Enter class: ")
    age = input("Enter age: ")
    weight = input("Enter weight: ")
    height = input("Enter height: ")
    blood_group = input("Enter blood group: ")
    blood_pressure = input("Enter blood pressure: ")
    pulse = input("Enter pulse: ")
    vision = input("Enter vision: ")
    ear = input("Enter ear: ")
    squint = input("Enter squint: ")
    thorat = input("Enter thorat: ")

    add_student_data(name, standard, age, weight, height, blood_group, blood_pressure, pulse, vision, ear, squint, thorat)