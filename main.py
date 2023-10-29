from flask import Flask, render_template, request, session, redirect
import pymongo

app = Flask(" ",template_folder=r"template", static_folder=r"static")
client = pymongo.MongoClient("mongodb+srv://HealthTrack:HealthTrack@cluster0.azdhcau.mongodb.net/?retryWrites=true&w=majority")
db = client["HealthTrack"]
student_data = db["student_data"]
#session secret key
app.config["SECRET_KEY"]="1234567890"


@app.route("/dashboard")
def dashboard():
    if session.get("user") != "admin":
        return redirect("/auth")
    class_value = request.args.get("class")
    age_value = request.args.get("age")
    if class_value:
        students = student_data.find({"class": class_value})
    elif age_value:
        students = student_data.find({"age": age_value})
    else:
        students = student_data.find()
    return render_template("main.html", students=list(students))

@app.route("/auth", methods=["GET","POST"])
def auth():
    if request.method == "POST":
        user = request.form.get("user")
        pwd= request.form.get("pass")
        print(user, pwd)
        if user == "admin" and pwd == "admin":
            session["user"] = user
            print(session)
            return redirect("/dashboard")
    return render_template("auth.html")

app.run(host="0.0.0.0", port=8080, debug=True)
