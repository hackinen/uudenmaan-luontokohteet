from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import generate_password_hash

class Database:
    def __init__(self, app):
        self.app = app
        self.db = SQLAlchemy(app)

        self.createTableUsers()
        self.createTableReviews()
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
        result = self.db.session.execute("SELECT * FROM users").fetchall()
        self.db.session.commit()
        return result

    def getName(self, username):
        sql = "SELECT name FROM users WHERE username=:username"
        result = self.db.session.execute(sql, {"username":username})
        self.db.session.commit()
        name = result.fetchone()[0]
        return name

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
        admin = result.fetchone()[0]
        self.db.session.commit()
        return admin

    def clearUsers(self):
        self.db.session.execute("DELETE FROM users")
        self.db.session.commit()


    # REVIEWS:

    def createTableReviews(self):
        sql = "CREATE TABLE IF NOT EXISTS reviews (id SERIAL PRIMARY KEY, destinationId INT, userId INT, ranking INT, comment TEXT);"
        self.db.session.execute(sql)
        self.db.session.commit()

    def createReview(self, destinationId, userId, ranking, comment):
        sql = "INSERT INTO reviews (destinationId,userId,ranking,comment) VALUES (:destinationId,:userId,:ranking,:comment)"
        self.db.session.execute(sql, {"destinationId":destinationId,"userId":userId,"ranking":ranking,"comment":comment})
        self.db.session.commit()

    def getReviewsByDestination(self, destinationId):
        result = self.db.session.execute("SELECT * FROM reviews WHERE destinationId=:destinationId", {"destinationId":destinationId})
        reviews = result.fetchall()
        self.db.session.commit()
        return reviews


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
        sql = self.db.session.execute("SELECT * FROM destinations ORDER BY name").fetchall()
        self.db.session.commit()
        return sql

    def getDestination(self, name):
        sql = "SELECT * FROM destinations WHERE name=:name"
        result = self.db.session.execute(sql, {"name":name})
        destination = result.fetchone() 
        self.db.session.commit()
        return destination

    def getDestinationById(self, id):
        sql = "SELECT * FROM destinations WHERE id=:id"
        result = self.db.session.execute(sql, {"id":id})
        destination = result.fetchone() 
        return destination

    def getBestRankedDestinations(self):
        sql = self.db.session.execute("SELECT * FROM destinations ORDER BY ranking desc LIMIT 6").fetchall()
        self.db.session.commit()
        return sql

    def addDefaultDestinations(self):
        dest = self.getDestination("Palakoski")
        print(dest)
        if dest == None:
            self.createDestination("Palakoski","Vihti",2)
            self.createDestination("Pääkslahden luontopolku","Vihti",1)
            self.createDestination("Liessaaren luontopolku","Lohja",3)
            self.createDestination("Nuuksion kansallispuisto","Espoo",5)
            self.createDestination("Sipooonkorven kansallispuisto","Sipoo",4)
            self.createDestination("Porkkalanniemen virkistysalue","Kirkkonummi",5)
            self.createDestination("Meikon ulkoilualue","Kirkkonummi",0)
            self.createDestination("Linlo","Kirkkonummi",0)
            self.createDestination("Hanikan luontopolku","Espoo",0)
            self.createDestination("Tremanskärrin luontopolku","Espoo",0)
            self.createDestination("Sarvikallion luontopolku","Tuusula",0)
            self.createDestination("Kukuljärven vaellusreitti","Loviisa",0)
            self.createDestination("Luukki","Espoo",0)
            self.createDestination("Högholmenin luontopolku","Hanko",0)
            self.createDestination("Kopparnäsin virkistysalue","Inkoo",0)
            self.createDestination("Karnaistenkorpi","Lohja",0)
            self.createDestination("Korkberget","Kirkkonummi",0)
            self.createDestination("Kytäjä-Usmin ulkoilualue","Hyvinkää",0)
            self.createDestination("Karkalin luonnonpuisto","Lohja",0)
            self.createDestination("Paavolan luontopolku","Lohja",0)


