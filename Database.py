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
        self.createTableAttractions()
        self.addDefaultAttractions()
        self.createTableFavourites()

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
    
    def getusernameById(self, id):
        sql = "SELECT username FROM users WHERE id=:id"
        result = self.db.session.execute(sql, {"id":id})
        username = result.fetchone()
        self.db.session.commit()
        return username

    def getUserId(self, username):
        sql = "SELECT id FROM users WHERE username=:username"
        result = self.db.session.execute(sql, {"username":username})
        id = result.fetchone()[0]
        self.db.session.commit()
        return id

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
        result = self.db.session.execute("SELECT u.username, r.ranking, r.comment FROM reviews r, users u WHERE r.destinationId=:destinationId AND u.id=r.userId", {"destinationId":destinationId})
        reviews = result.fetchall()
        self.db.session.commit()
        return reviews

    def countStarAverage(self, destinationId):
        sql = "SELECT AVG(ranking) FROM reviews WHERE destinationId=:destinationId"
        result = self.db.session.execute(sql, {"destinationId":destinationId})
        self.db.session.commit()
        avg = result.fetchone[0]
        return avg

    def getReviewsByUser(self, username):
        sql = "SELECT r.id, d.id, d.name, d.town, r.ranking, r.comment FROM reviews r JOIN destinations d ON d.id=r.destinationId WHERE userId=(SELECT id FROM users WHERE username=:username);"
        result = self.db.session.execute(sql, {"username":username}).fetchall()
        self.db.session.commit()
        return result

    def deleteReview(self,reviewId):
        sql = "DELETE FROM reviews WHERE id=:reviewId"
        self.db.session.execute(sql, {"reviewId":reviewId})
        self.db.session.commit()
     

    # DESTINATIONS:

    def createTableDestinations(self):
        sql = "CREATE TABLE IF NOT EXISTS destinations (id SERIAL PRIMARY KEY, name TEXT, town TEXT);"
        self.db.session.execute(sql)
        self.db.session.commit()

    def createDestination(self, name, town):
        sql = "INSERT INTO destinations (name,town) VALUES (:name,:town)"
        self.db.session.execute(sql, {"name":name,"town":town})
        self.db.session.commit()

    def getDestinations(self):
        sql = self.db.session.execute("SELECT d.id, d.name, d.town, COALESCE(ROUND(AVG(r.ranking),1),0), COUNT(r.ranking) FROM destinations d LEFT JOIN reviews r ON r.destinationId=d.id GROUP BY d.id ORDER BY d.name;").fetchall()
        self.db.session.commit()
        return sql

    def getDestination(self, name):
        sql = "SELECT * FROM destinations WHERE name=:name"
        result = self.db.session.execute(sql, {"name":name})
        destination = result.fetchone() 
        self.db.session.commit()
        return destination

    def getDestinationById(self, id):
        sql = "SELECT d.id, d.name, d.town, COALESCE(ROUND(AVG(r.ranking),1),0) FROM destinations d LEFT JOIN reviews r ON r.destinationId=d.id WHERE d.id=:id GROUP BY d.id;"
        result = self.db.session.execute(sql, {"id":id})
        destination = result.fetchone() 
        return destination

    def getBestRankedDestinations(self):
        sql = self.db.session.execute("SELECT d.id, d.name, d.town, ROUND(AVG(r.ranking),1), COUNT(r.ranking) FROM reviews r JOIN destinations d ON r.destinationId=d.id GROUP BY d.id ORDER BY AVG(r.ranking) DESC, COUNT(r.ranking) DESC LIMIT 6;").fetchall()
        self.db.session.commit()
        return sql

    def deleteDestination(self, destinationId):
        sql = "DELETE FROM destinations WHERE id=:destinationId"
        self.db.session.execute(sql, {"destinationId":destinationId})
        sql2 = "DELETE FROM attractions WHERE destinationId=:destinationId"
        self.db.session.execute(sql2, {"destinationId":destinationId})
        self.db.session.commit()


    # ATTRACTIONS:

    def createTableAttractions(self):
        sql = "CREATE TABLE IF NOT EXISTS attractions (id SERIAL PRIMARY KEY, destinationId INT, name TEXT, info TEXT);"
        self.db.session.execute(sql)
        self.db.session.commit()

    def createAttraction(self, destinationId, name, info):
        sql = "INSERT INTO attractions (destinationId,name,info) VALUES (:destinationId,:name,:info)"
        self.db.session.execute(sql, {"destinationId":destinationId,"name":name,"info":info})
        self.db.session.commit()

    def createAttractionWithNoInfo(self, destinationId, name):
        self.createAttraction(destinationId, name, None)

    def getAttraction(self, name):
        sql = "SELECT * FROM attractions WHERE name=:name"
        result = self.db.session.execute(sql, {"name":name})
        destination = result.fetchone() 
        self.db.session.commit()
        return destination

    def getAttractionsByDestination(self, destinationId):
        result = self.db.session.execute("SELECT * FROM attractions WHERE destinationId=:destinationId", {"destinationId":destinationId})
        reviews = result.fetchall()
        self.db.session.commit()
        return reviews

    def deleteAttraction(self, attractionId):
        sql = "DELETE FROM attractions WHERE id=:attractionId"
        self.db.session.execute(sql, {"attractionId":attractionId})
        self.db.session.commit()


    # FAVOURITES:

    def createTableFavourites(self):
        self.db.session.execute("CREATE TABLE IF NOT EXISTS favourites (id SERIAL PRIMARY KEY, userId INT, destinationId INT);")
        self.db.session.commit()

    def createFavourite(self,username,destinationId):
        sql = "INSERT INTO favourites (userId,destinationId) VALUES ((SELECT id FROM users WHERE username=:username),:destinationId)"
        self.db.session.execute(sql, {"username":username,"destinationId":destinationId})
        self.db.session.commit()

    def getFavouritesByUser(self, username):
        sql = "SELECT f.userId, f.destinationId, d.name, d.town FROM favourites f JOIN destinations d ON d.id=f.destinationId WHERE userId=(SELECT id FROM users WHERE username=:username);"
        result = self.db.session.execute(sql, {"username":username}).fetchall()
        self.db.session.commit()
        return result

    def deleteFavourite(self, username, destinationId):
        sql = "DELETE FROM favourites WHERE userId=(SELECT id from users WHERE username=:username) AND destinationId=:destinationId"
        self.db.session.execute(sql, {"username":username,"destinationId":destinationId})
        self.db.session.commit()

    def isFavourite(self,username,destinationId):
        sql = "SELECT * FROM favourites WHERE userId=(SELECT id FROM users WHERE username=:username) AND destinationId=:destinationId;"
        result = self.db.session.execute(sql, {"username":username,"destinationId":destinationId}).fetchall()
        self.db.session.commit()
        return len(result) != 0


    # DEFAULT DATA: 

    def addDefaultDestinations(self):
        dest = self.getDestination("Palakoski")
        if dest == None:
            self.createDestination("Palakoski","Vihti")
            self.createDestination("Pääkslahden luontopolku","Vihti")
            self.createDestination("Liessaaren luontopolku","Lohja")
            self.createDestination("Nuuksion kansallispuisto","Espoo")
            self.createDestination("Sipooonkorven kansallispuisto","Sipoo")
            self.createDestination("Porkkalanniemen virkistysalue","Kirkkonummi")
            self.createDestination("Meikon ulkoilualue","Kirkkonummi")
            self.createDestination("Linlo","Kirkkonummi")
            self.createDestination("Hanikan luontopolku","Espoo")
            self.createDestination("Tremanskärrin luontopolku","Espoo")
            self.createDestination("Sarvikallion luontopolku","Tuusula")
            self.createDestination("Kukuljärven vaellusreitti","Loviisa")
            self.createDestination("Luukki","Espoo")
            self.createDestination("Högholmenin luontopolku","Hanko")
            self.createDestination("Kopparnäsin virkistysalue","Inkoo")
            self.createDestination("Karnaistenkorpi","Lohja")
            self.createDestination("Korkbergetin luonnonsuojelualue","Kirkkonummi")
            self.createDestination("Kytäjä-Usmin ulkoilualue","Hyvinkää")
            self.createDestination("Karkalin luonnonpuisto","Lohja")
            self.createDestination("Paavolan luontopolku","Lohja")


    def addDefaultAttractions(self):
        attraction = self.getAttraction("Palakoskenkierros")
        if attraction == None:
            self.createAttraction(1,"Palakoskenkierros","4,3 km, paljon korkeuseroja")
            self.createAttraction(1,"Mummusalin näköalakallio","parkkipaikalta 1 km")
            self.createAttractionWithNoInfo(2,"Laukkakallio")
            self.createAttractionWithNoInfo(3,"Luontotietorastit")
            self.createAttraction(3,"Luonnontie-terveysluontopolku","2 km")
            self.createAttraction(4,"Punarinnankierros","2 km rengasreitti")
            self.createAttraction(4,"Haukankierros","4 km rengasreitti")
            self.createAttraction(4,"Korpinkierros","6-7,2 km rengasreitti")
            self.createAttraction(4,"Takalan polku","1,5 km/suunta")
            self.createAttraction(4,"Kaarniaispolku","2,7 km rengasreitti")
            self.createAttraction(4,"Soidinkierros","4 km rengasreitti")
            self.createAttraction(4,"Nahkiaispolku","2 km rengasreitti")
            self.createAttraction(4,"Klassarinkierros","3,9 km rengasreitti")
            self.createAttraction(4,"Yhdysreitti Haukkalampi-Haltia","4,6 km/suunta")
            self.createAttraction(4,"Nuuksion kansallispuiston läpi vievä reitti","noin 14 km")
            self.createAttraction(5,"Byabäckenin luontopolku","1,4 km; rengasreittinä 2,1 km")
            self.createAttraction(5,"Kalkinpolttajanpolku","4,8 km rengasreitti")
            self.createAttraction(5,"Högberget","näköalapaikka, osa kalkinpolttajanpolkua")
            self.createAttraction(5,"Storträsk","1 km/suunta, osittain esteetön")
            self.createAttraction(6,"Vetokannaksentaival","2,1 km")
            self.createAttraction(6,"Telegrafbergetin lenkki","2,2 km rengasreitti")
            self.createAttraction(6,"Pampskatanin pisto","1,4 km")
            self.createAttraction(7,"Kuikankierros","3,2 km")
            self.createAttraction(7,"Meikonkierros","8,3 km")
            self.createAttraction(7,"Kotokierros","4,4 km")
            self.createAttractionWithNoInfo(8,"useita luontopolkuja")
            self.createAttractionWithNoInfo(9,"Soukankalliot")
            self.createAttractionWithNoInfo(9,"Sundsberget")
            self.createAttractionWithNoInfo(9,"Hanikan lintutorni")
            self.createAttraction(10,"Tremanskärrin reitti","2,8 km")
            self.createAttraction(10,"Kurkijärven reitti","3,4 km")
            self.createAttraction(11,"Seittelinreitti","3,4 km rengasreitti")
            self.createAttractionWithNoInfo(11,"Sarvikallion näköalapaikka")
            self.createAttraction(12,"Vaellusreitti","noin 8 km rengasreitti")
            self.createAttraction(13,"Eri mittaisia reittejä","2,5 km, 5,6 km, 8,6 km")
            self.createAttraction(14,"Högholmenin reitti","lyhyt, noin 1km")
            self.createAttractionWithNoInfo(15,"Useita polkuja merellisessä maastossa")
            self.createAttractionWithNoInfo(15,"Rävberget")
            self.createAttraction(16,"Karnaistenkorven luontopolku","3,3-7,7 km")
            self.createAttraction(17,"Korkberget","korkea kallionäköalapaikka, josta näkymä Humaljärvelle")
            self.createAttraction(18,"Haiskarin kierros","6,1 km")
            self.createAttraction(18,"Kolmen lammen kierros","9,8 km")
            self.createAttraction(18,"Niittulahden kierros","10,2 km")
            self.createAttraction(18,"Kahden piilon kierros","11,5 km")
            self.createAttraction(18,"Mustan kiven kierros","12,3 km")
            self.createAttraction(18,"Seitsemän veljeksen vaellusreitti","19,8 km")
            self.createAttraction(19,"luontopolku","6,5 km")
            self.createAttraction(20,"Paavolan luontopolku","1 km")
            self.createAttractionWithNoInfo(20,"Paavolan tammi")