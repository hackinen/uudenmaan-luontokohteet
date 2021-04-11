from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import generate_password_hash

class Database:
    def __init__(self, app):
        self.app = app
        self.db = SQLAlchemy(app)

        self.createTableUsers()
        self.createTableDestinations()
        self.addDefaultDestinations()

    # USERS:

    def createTableUsers(self):
        sql = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, username TEXT, password TEXT, admin BOOLEAN);"
        self.db.session.execute(sql)
        self.db.session.commit()

        # admin user for admin-properties
        user = self.getPassword("admin")
        if user == None:
            pwhash = generate_password_hash(getenv("PASSWORD_FOR_ADMIN"))
            self.createUser("admin","admin", pwhash, True)

    def createUser(self, name, username, passwordHash, admin):
        sql = "INSERT INTO users (name,username,password,admin) VALUES (:name,:username,:password,:admin)"
        self.db.session.execute(sql, {"name":name,"username":username,"password":passwordHash,"admin":admin})
        self.db.session.commit()

    def getUsers(self):
        result = self.db.session.execute("SELECT * FROM users").fetchAll()
        self.db.session.commit()
        return result

    def getPassword(self, username):
        sql = "SELECT password FROM users WHERE username=:username"
        result = self.db.session.execute(sql, {"username":username})
        password = result.fetchone()
        self.db.session.commit() 
        return password
    
    def usernameTaken(self, username):
        sql = "SELECT * FROM users WHERE username=:username"
        result = self.db.session.execute(sql, {"username":username})
        self.db.session.commit()
        usersFound = result.fetchall()
        return len(usersFound) > 0

    def isAdmin(self, username):
        sql = "SELECT admin FROM users WHERE username=:username"
        result = self.db.session.execute(sql, {"username":username})
        admin = result.fetchone()
        self.db.session.commit()
        return admin

    def clearUsers(self):
        self.db.session.execute("DELETE FROM users")
        self.db.session.commit()


    # DESTINATIONS:

    def createTableDestinations(self):
        sql = "CREATE TABLE IF NOT EXISTS destinations (id SERIAL PRIMARY KEY, name TEXT, town TEXT, ranking INT);"
        self.db.session.execute(sql)
        self.db.session.commit()

    def createDestination(self, name, town, ranking):
        sql = "INSERT INTO destinations (name,town,ranking) VALUES (:name,:town,:ranking)"
        self.db.session.execute(sql, {"name":name,"town":town,"ranking":ranking})
        self.db.session.commit()

    def getDestinations(self):
        return self.db.session.execute("SELECT * FROM destinations").fetchall()

    def getDestination(self, name):
        sql = "SELECT * FROM destinations WHERE name=:name"
        result = self.db.session.execute(sql, {"name":name})
        destination = result.fetchone() 
        return destination

    def addDefaultDestinations(self):
        dest = self.getDestination("Palakoski")
        if dest == None:
            self.createDestination("Palakoski","Vihti",0)
            self.createDestination("Pääkslahden luontopolku","Vihti",0)
            self.createDestination("Liessaaren luontopolku","Lohja",0)
            self.createDestination("Nuuksion kansallispuisto","Espoo",0)
            self.createDestination("Sipooonkorven kansallispuisto","Sipoo",0)
            self.createDestination("Porkkalanniemen virkistysalue","Kirkkonummi",0)
            self.createDestination("Meikon ulkoilualue","Kirkkonummi",0)
            self.createDestination("Linlo","Kirkkonummi",0)
            self.createDestination("Hanikan luontopolku","Espoo",0)
            self.createDestination("Tremanskärrin luontopolku","Espoo",0)
            self.createDestination("Sarvikallion luontopolku","Tuusula",0)
            self.createDestination("Kukuljärven vaellusreitti","Loviisa",0)

