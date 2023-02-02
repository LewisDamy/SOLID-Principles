"""
    SINGLE RESPONSABILITY PRINCIPLE
        Definition:
        - Every software component should have one and only one (responsability) reason to change

        Concept Learned:
        - COHESION
            Degree to which the various parts of a software component are related
        - COUPLING
            Level of inter dependency between various software components
"""


# Cohesion Example
class CohesionizedSquare:
    def __init__(self) -> None:
        self.side = 5

    def calculateArea(self) -> int:
        return self.side * self.side

    def calculatePerimeter(self) -> int:
        return self.side * 4
    
    def draw(self) -> None:
        if self.highResolutionMonitor:
            # Render a high resolution image of a square
            pass 
        else:
            # Render a normal image of a square
            pass
    
    def rotate(self, degree: int) -> None:
        # Rotate the image of the square clockwise to
        # the required degree and re-render
        pass


# Fixed Square Example SRP
class Square:
    def __init__(self) -> None:
        self.side = 5
    
    def calculateArea(self) -> int:
        return self.side * self.side
    
    def calculatePerimeter(self) -> int:
        return self.side * 4
    
class SquareUI:
    def __init__(self) -> None:
        pass

    def draw(self) -> None:
        if self.highResolutionMonitor:
            pass
        else:
            pass
    
    def rotate(self, degree: int) -> None:
        pass

########################################################################
# Example 2: Coupling
########################################################################
import mysql.connector
from mysql.connector import Error

class Student:
    def __init__(self, studentId, date, address) -> None:
        self.studentId  = studentId
        self.date       = date
        self.address    = address
    
    def save(self) -> None:
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='Test',
                user='userTest',
                password='secretPassword'
            )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connect to mySQL server " + db_info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def getStudentId(self):
        return self.studentId

    def setStudentId(self, studentId):
        self.studentId = studentId

# Solution: Student + StudentRepository classes

class StudentRepository:
    def save(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='Test',
                user='userTest',
                password='secretPassword'
            )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connect to mySQL server " + db_info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

class Student:
    def __init__(self, studentId, date, address) -> None:
        self.studentId  = studentId
        self.date       = date
        self.address    = address
    
    def save(self) -> None:
        myRepo = StudentRepository(self)

    def getStudentId(self):
        return self.studentId

    def setStudentId(self, studentId):
        self.studentId = studentId
