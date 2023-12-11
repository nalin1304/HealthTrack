import pymongo

# Replace the connection string with your own MongoDB connection string
client = pymongo.MongoClient("mongodb+srv://HealthTrack:HealthTrack@cluster0.azdhcau.mongodb.net/?retryWrites=true&w=majority")

db = client["HealthTrack"]
student_data = db["student_data"]

# name, class (standard), age, weight, height, blood group, blood pressure, pulse, vision, ear, squint, throat

def add_student_data(name, standard, age, weight, height, blood_group, blood_pressure, pulse, haemoglobin, tooth_cavity, gum_inflamation, tarter, gum_bleeding, plaque, stains, vision, ear, squint, throat, allergies):
    student = {
        "name": name,
        "class": standard,
        "age": age,
        "weight": weight,
        "height": height,
        "blood" :{"blood_group": blood_group,"blood_pressure": blood_pressure,"pulse": pulse, "haemoglobin": haemoglobin},
        "oral": {"tooth_cavity": tooth_cavity,"gum_inflamation": gum_inflamation,"tarter": tarter,"gum_bleeding": gum_bleeding,"plaque": plaque,"stains": stains},
        "vision": vision,
        "ear": ear,
        "squint": squint,
        "throat": throat,
        "allergies": allergies,
        "recommendation": []
    }
    student_data.insert_one(student)
for i in range(0,15):
    print("General Details")
    name = input("Enter name: ")
    standard = input("Enter class: ")
    age = input("Enter age: ")
    weight = input("Enter weight: ")
    height = input("Enter height: ")
    blood_group = input("Enter blood group: ")
    blood_pressure = input("Enter blood pressure: ")
    pulse = input("Enter pulse: ")
    haemoglobin = input("Enter haemoglobin: ")
    print("Oral Details")
    tooth_cavity = input("Enter tooth cavity: ")
    gum_inflamation = input("Enter gum inflamation: ")
    tarter = input("Enter tarter: ")
    gum_bleeding = input("Enter gum bleeding: ")
    plaque = input("Enter plaque: ")
    stains = input("Enter stains: ")
    print("Other Details")
    vision = input("Enter vision: ")
    ear = input("Enter ear: ")
    squint = input("Enter squint: ")
    throat = input("Enter throat: ")
    print("Allergies")
    no_allergy = input("Enter number of allergies: ")
    allergies = []
    for i in range(0,int(no_allergy)):
        print("-------------------")
        allergy_name = input("Enter allergy name: ")
        allergy_what_happend = input("Enter what happend: ")
        allergy_how_severe = input("Enter how severe: ")
        allergy_medication = input("Enter medication: ")
        allergies.append({
            "allergy_name": allergy_name,
            "what_happend": allergy_what_happend,
            "how_severe": allergy_how_severe,
            "medication": allergy_medication,
        })

    add_student_data(name, standard, age, weight, height, blood_group, blood_pressure, pulse, haemoglobin, tooth_cavity, gum_inflamation, tarter, gum_bleeding, plaque, stains, vision, ear, squint, throat, allergies)

    print("Student added successfully! \n\n\n")