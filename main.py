import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def initialize_firestore():
   # Set up Cloud Key
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "employee-database-c9b7c-firebase-adminsdk-2ws6z-4269ba4086.json"
   # Use the application default credentials
   cred = credentials.ApplicationDefault()
   firebase_admin.initialize_app(cred, {
   'projectId': "employee-database-c9b7c",
   })

   return firestore.client()

def displayPositions(db):
   query = db.collection(u'positions').stream()
   print("{:<5} {:<15} {:<15}".format("Manager", "Position", "Pay"))
   print("{:<5} {:<15} {:<15}".format("-------","---------","----------"))
   for position in query:
      newDict = position.to_dict()
      print("{:<5} {:<15} ${:<15.2f}".format(position.to_dict()["manager"],position.to_dict()["title"],position.to_dict()["pay"]))


def displayEmployees(db):
   query = db.collection(u'employees').stream()
   print("{:<5} {:<15} {:<15}".format("State", "Full Name", "Experience"))
   print("{:<5} {:<15} {:<15}".format("-----","---------","----------"))
   for employee in query:
      newDict = employee.to_dict()
      print("{:<5} {:<15} {:<15}".format(employee.to_dict()["state"],employee.to_dict()["name"],employee.to_dict()["experience"]))


def editEmployee(db):
    employeeName = input("Please enter the employee's full name: ")
    employeeUsername = input("Input a username for the new employee: ")
    employeeExperience = input("Please enter the employee's previous experience (Degree, Previous work, etc): ")
    employeeState = input("Enter the employee's home state code (ex. ID, AL, GA, etc.): ")
    data = {
       'name': employeeName,
       'experience': employeeExperience,
       'state': employeeState
    }
    db.collection(u'employees').document(employeeUsername).set(data)


def editPosition(db):
   print("Add Position")

def deleteEmployee():
   print("Delete Employee")

def deletePosition():
   print("Delete Position")

def main():
   db = initialize_firestore()

   userSelect = "1"
   while userSelect != "7":
      print("What would you like to do?")
      print("1) Add or edit an Employee")
      print("2) Add or edit a Position")
      print("3) Display All Employees")
      print("4) Display All Positions")
      print("5) Remove an Employee")
      print("6) Remove a Position")
      print("7) Quit")
      print("")
      userSelect = input("> ")
      print("")
      if userSelect == "1":
         editEmployee(db)
         print("")
      elif userSelect == "2":
         editPosition(db)
         print("")
      elif userSelect == "3":
         displayEmployees(db)
         print("")
      elif userSelect == "4":
         displayPositions(db)
         print("")
      elif userSelect == "5":
         deleteEmployee()
         print("")
      elif userSelect == "6":
         deletePosition()
         print("")
   print("See ya.")

if __name__ == "__main__":
   main()
