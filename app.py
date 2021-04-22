from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

from Database import Database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")

db = Database(app)

@app.before_request
def set_dest():
    if 'dest' in request.args:
        session["destinationId"] = request.args['dest']

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    passwordConfirm = request.form["passwordConfirm"]

    if name == None or name == "":
        error = "Valitse jokin nimi"
        return render_template("newuser.html", error=error)

    if username == None or username == "":
        error = "Valitse jokin nimimekki"
        return render_template("newuser.html", error=error)

    if password == None or password == "":
        error = "Puuttuva salasana"
        return render_template("newuser.html", error=error)

    if isNotValid(name):
        error = "Liian lyhyt nimi"
        return render_template("newuser.html", error=error)

    if isNotValid(username):
        error = "Liian lyhyt nimimerkki"
        return render_template("newuser.html", error=error)

    if isNotValid(password):
        error = "Liian lyhyt salasana"
        return render_template("newuser.html", error=error)

    if db.usernameTaken(username):
        error = "Valitsemasi nimimerkki on jo käytössä!"
        return render_template("newuser.html", error=error)

    if password != passwordConfirm:
        error = "Salasanat eivät täsmää"
        return render_template("newuser.html", error=error)

    passwordHash = generate_password_hash(password)
    db.createUser(name, username, passwordHash, False)

    session["username"] = username
    return redirect("/mainpage")


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = db.getPassword(username)
       
    if user == None:
        #invalid username
        error = "Väärä käyttäjätunnus"
        return render_template("index.html", error=error)
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            #correct username and password
            session["username"] = username
            return redirect("/mainpage")
        else:
            #invalid password
            error = "Väärä salasana"
            return render_template("index.html", error=error)


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/newuser")
def newuser():
    return render_template("newuser.html")


@app.route("/newreview",methods=["POST"])
def newreview():
    try:
        isLoggedIn()
        comment = request.form["comment"]
        userId = db.getUserId(session["username"])
        ranking = request.form["stars"]

        if ranking == None:
            error = "Anna arvio 1-5"
            return render_template("destination.html", destination=destination, reviews=reviews, attractions=attractions, error=error)

        db.createReview(session["destinationId"],userId, ranking, comment)
        return redirect("/destination")
    except Exception as e:
        print(e)
        return redirect("/")


@app.route("/newdestination",methods=["POST"])
def newdestination():
    try:
        isLoggedIn()
        admin = db.isAdmin(session["username"])
        if admin:
            name = request.form["name"]
            town = request.form["town"]

            if name == None or name == "":
                error = "Anna luontokohteen nimi"
                return render_template("profile.html",name=db.getName(session["username"]),username=session["username"],admin=admin, destinations=db.getDestinations(), error=error)

            if town == None or town == "":
                error = "Anna luontokohteen sijaintikunta"
                return render_template("profile.html",name=db.getName(session["username"]),username=session["username"],admin=admin, destinations=db.getDestinations(), error=error)

            db.createDestination(name,town)
            return redirect("/profile")

    except Exception as e:
        print(e)
        return redirect("/")


@app.route("/newattraction",methods=["POST"])
def newattraction():
    try:
        isLoggedIn()
        admin = db.isAdmin(session["username"])

        if admin:
            destinationId = request.form["destination"]
            attraction = request.form["attractionName"]
            info = request.form["info"]

            if attraction == None or attraction == "":
                error2 = "Anna lisättävän polun/nähtävyyden nimi"
                return render_template("profile.html",name=db.getName(session["username"]),username=session["username"],admin=admin, destinations=db.getDestinations(), error2=error2)

            if info == None or info == "":
                db.createAttractionWithNoInfo(destinationId,attraction)
                return redirect("/profile")

            db.createAttraction(destinationId,attraction,info)
            return redirect("/profile")

    except Exception as e:
        print(e)
        return redirect("/")


@app.route("/mainpage")
def mainpage():
    try:
        bestRanked = db.getBestRankedDestinations()
        return render_template("mainpage.html",bestRanked=bestRanked)
    except:
        return redirect("/")


@app.route("/destinations")
def destinations():
    try:
        isLoggedIn()
        allDestinations = db.getDestinations()
        return render_template("destinations.html", allDestinations=allDestinations)
    except:
        return redirect("/")


@app.route("/destination")
def destination():
    try:
        isLoggedIn()
        destination = db.getDestinationById(session["destinationId"])
        reviews = db.getReviewsByDestination(session["destinationId"])
        attractions = db.getAttractionsByDestination(session["destinationId"])
        return render_template("destination.html", destination=destination, reviews=reviews, attractions=attractions)
    except Exception as e:
        print(e)
        return redirect("/")


@app.route("/profile")
def profile():
    try:
        admin = db.isAdmin(session["username"])
    except:
        admin = False

    try:    
        name = db.getName(session["username"])
        destinations = db.getDestinations()
        return render_template("profile.html",name=name,username=session["username"],admin=admin,destinations=destinations)
    except Exception as e:
        print(e)
        return redirect("/")


def isLoggedIn():
    session["username"]

def isNotValid(input):
    if len(input) < 2:
        return True
    return False