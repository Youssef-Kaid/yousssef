
#==============================================
#Question 1:
#==============================================

# Create a Python class called "Rectangle" that represents a rectangle. 

# The Rectangle class must have the following properties and methods:

#Features:
# width (an integer)
# height (an integer)

#Methods:
# area(self): A method that calculates and returns the area of the rectangle.
# perimeter(self): A method that calculates and returns the perimeter of the rectangle.
# Create an instance of Rec

 
from calendar import c


class Rectangle:
    def __init__(self, width, height ):
        self.width = width
        self.height = height 

    def area(self):
        return self.width * self.height


    def perimeter(self): 
        return 2 * self.area()

Rec = Rectangle(4, 6)
print("\n======= Rectangle =======\n")
print(f"The area of the rectangle is {Rectangle.area(Rec)}, and the perimeter of the rectangle is {Rectangle.perimeter(Rec)}\n\n")


#==============================================
#Question 2:
#==============================================

# Create a "School" class in Python. This class should have the following features and functionality:

#Features:
#"name"
#"foundation_year"
#"students list"
#"teachers list"

class School:
    def __init__(self, name, foundation_year):
        self.name = name 
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}


# 1- add_new_student(self, student_name, class): A method used to add a new student to the school. 
#    It takes the student's name and class and adds it to the "students" list


    def add_new_student(self, student_name, class_name):
        #print("======= ADD A STUDENT =======\n")
        #student_name = input("Enter your name:\n")
        #Class = input("Enter which class you attend:\n")
        self.students.append((student_name, class_name))
        #print("Your name and class were added successfully.\n")


# 2- add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the
#    school. It takes the teacher's name and major and adds it to the "teachers" dictionary.

    def add_new_teacher(self, teacher_name, branch):
        #print("======= ADD A TEACHER =======\n")    
        #teacher_name = input("Enter your name:\n")
        #branch = input("Enter your major:\n")
        self.teachers[teacher_name] = branch
        #print("Your name and major were added successfully.\n")


# 3- view_student_list(self): A method used to display the list of students enrolled in the school.
#    List student names and classes.
    def view_student_list(self):
        print("These are the students enrolled in the school:")
        for number, (student_name, class_name) in enumerate(self.students, 1):
            print(f"{number}. {student_name} - {class_name}")


# 4- view_teacher_list(self): A method used to display the list of teachers working in the school.
#    List teacher names and majors.
    def view_teacher_list(self):
        print("\nThese are the teachers working in the school:")
        for number, (teacher_name, branch) in enumerate(self.teachers.items(), 1):
            print(f"{number}. {teacher_name} - {branch}")

school = School("ABC School", 1995)

print(f"School's name: {school.name}\nThe foundation year: {school.foundation_year}\n")
#students
student_one = school.add_new_student("youssef","A10")
student_two =  school.add_new_student("Mahar","A10")
student_three =  school.add_new_student("Mohammed","A12")

#teachers
teacher_one = school.add_new_teacher("Mike", "Maths")
teacher_two = school.add_new_teacher("Alex", "Bio")
#school.add_new_student()
#school.add_new_teacher()
school.view_student_list()
school.view_teacher_list()

#==============================================
#Question 3:
#==============================================

# Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.
# 1- first: the "Shape" class have two properties: "width" and "height."
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height 

# 2- second:  the "Rectangle" class inherit from the "Shape" class 

class Rectangle(Shape):
    def calculate_area(self): #  add an additional "calculate_area()" method.
        return self.width * self.height 

# 3- third:  the "Square" class inherit from the "Shape" class 
class Square(Shape):
    def calculate_area(self): #  add an additional "calculate_area()" method.
        return self.width * self.height 


# craete an object instance of rectangle 
rectangle_Q3 = Rectangle(12,32)
# area calculation for the rectangle 
result_rectangle = Rectangle.calculate_area(rectangle_Q3)

# create an object instance of square 
square = Square(40,40)
# area calculation for the square
result_square = Square.calculate_area(square) 
 
# calculate the area of rectangle 
print("\n===== The calculation of the rectangle area  =====\n")
print(f"The width of the rectangle: {rectangle_Q3.width}")
print(f"The height of the rectangle: {rectangle_Q3.height}")
print(f"The area of the rectangle: {result_rectangle} square meters.")

# calculate the area of the square
print("\n===== The calculation of the square area  =====\n")
print(f"The width of the square: {square.width}")
print(f"The height of the square: {square.height}")
print(f"The area of the square: {result_square} square meters.\n")



#==============================================
#Question 4:
#==============================================


# Create a "Vehicle" class in Python. Make sure this class has the following properties: 
# Features:
# 1-  "make" (Brand of vehicle)
# 2-  "model" (Vehicle model)
# 3-  "year" (Year of manufacture of the vehicle)

class Vehicle:

    # The __init__ method is called automatically when we create an object.
    # It sets the make, model, and year properties.
    def __init__(self, make, model, year):
        self.make = make       # Brand of the vehicle
        self.model = model     # Model of the vehicle
        self.year = year       # Year of manufacture



# Create a "Vehicle" class and create two derived subclasses, "OffRoadVehicle" (SUV) and "SportsCar" classes.


# 1-  The "OffRoadVehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel_drive" feature.

class OffRoadVehicle(Vehicle):

    # The __init__ method includes the properties from Vehicle
    # plus the additional four_wheel_drive property.
    def __init__(self, make, model, year, four_wheel_drive):
        
        # Call the Vehicle class constructor to set make, model, and year.
        super().__init__(make, model, year)

        # Add the extra property for the OffRoadVehicle.
        self.four_wheel_drive = four_wheel_drive



# 2- Let the "SportsCar" class inherit from the "Vehicle" class and add a "max_speed" property.
class SportsCar(Vehicle):

    # The __init__ method includes the properties from Vehicle
    # plus the additional max_speed property.
    def __init__(self, make, model, year, max_speed):
        
        # Call the Vehicle class constructor to set make, model, and year.
        super().__init__(make, model, year)

        # Add the extra property for the SportsCar.
        self.max_speed = max_speed


 


# ---------------------------------------------------------
# CREATE OBJECTS
# ---------------------------------------------------------

# Create an object (instance) of the Vehicle class.
vehicle1 = Vehicle("Toyota", "Corolla", 2022)

# Create an object (instance) of the OffRoadVehicle class.
offroad1 = OffRoadVehicle("Jeep", "Wrangler", 2023, True)

# Create an object (instance) of the SportsCar class.
sportscar1 = SportsCar("Ferrari", "488", 2021, 340)


# ---------------------------------------------------------
# DISPLAY THE PROPERTIES
# ---------------------------------------------------------

# Display the properties of the Vehicle object.
print("Vehicle:")
print("Brand of the vehicle:", vehicle1.make)
print("Model of the vehicle:", vehicle1.model)
print("Year production:", vehicle1.year)

print()  # Prints an empty line


# Display the properties of the OffRoadVehicle object.
print("Off-Road Vehicle:")
print("Brand of the vehicle::", offroad1.make)
print("Model:", offroad1.model)
print("Year:", offroad1.year)
print("Four Wheel Drive:", offroad1.four_wheel_drive)

print()  # Prints an empty line


# Display the properties of the SportsCar object.
print("Sports Car:")
print("Brand of the vehicle:", sportscar1.make)
print("Model of the vehicle:", sportscar1.model)
print("Year production:", sportscar1.year)
print("Maximum Speed:", sportscar1.max_speed, "km/h")


#==============================================
#Question 5:
#==============================================


# Create a "Customer" class and an "Account" class. 


# Customer Class Features:
# 1- customer name
# 2- customer surname
# 3-  customer TR ID number
# 4- customer phone number

class Customer:
    customers_number = []

    def __init__(self, name, surname, TR_ID, phone):
        self.name = name
        self.surname = surname
        self.TR_ID = TR_ID
        self.phone = phone

        Customer.customers_number.append(self)
    
    def display_customer_information(self): # Display a single customer
        print("\n\n----------------------------------")
        print("====== CUSTOMER INFORMATION ======")
        print("----------------------------------")
        print(f"Customer name: {self.name}")
        print(f"Customer surname: {self.surname}")
        print(f"Customer TC identification: {self.TR_ID}")
        print(f"Customer phone number: {self.phone}")
        print("----------------------------------\n")

    @classmethod    # addtional display all customers at once
    def customers_list(cls): 
        print("\n----------------------------------")
        print("========= CUSTOMERS LIST =========")
        print("----------------------------------")
        for customer in cls.customers_number:
            
        
            print("----------------------------------")
            print(f"Customer name: {customer.name}")
            print(f"Customer surname: {customer.surname}")
            print(f"Customer TC identification: {customer.TR_ID}")
            print(f"Customer phone number: {customer.phone}")
            print("----------------------------------\n")

    


# Let the "Account" class use the  "Customer" class to represent a customer's bank account information.
# Account Class Properties:
# 1-  customer
# 2-  account number
# 3-  account balance


class Account:
    def __init__(self, customer, account_number, account_balance):
        self.customer = customer
        self.account_number = account_number 
        self.account_balance = account_balance
        

    def deposit(self, amount): # This "m" deposits a certain amount of money into the account.
        self.account_balance += amount 
        print("\n-------------------------------------------")
        print("=========== DEPOSIT TRANSACTION ===========")
        print("-------------------------------------------")
        print(f"The amount ${amount} was successfuly deposited.") 
        print(f"Your current balance: ${self.account_balance}")
        print("-------------------------------------------\n")
     
    
    def money_check(self, amount): # This "m"  withdraws a certain amount of money from the account.
        
        if self.account_balance < amount:
            print("\n-------------------------------------------")
            print("========= WITHDRAWAL TRANSACTION ==========")
            print("-------------------------------------------")
            print("Sorry, your account balance is insufficient.")
            print(f"This amount ${amount} cannot be withdrawn.")
            print(f"Your current balance: ${self.account_balance}")
            print("--------------------------------------------\n")

        #  the above output will be displayed when the balance is insufficient 


        else:
            # Withdraw the money
            self.account_balance -= amount

            print("\n------------------------------------------")
            print("========= WITHDRAWAL TRANSACTION =========")
            print("------------------------------------------")
            print("The transaction is successful.")
            print(f"This amount ${amount} was withdrawn.")
            print(f"Your current balance: ${self.account_balance}")
            print("------------------------------------------\n")
            
        

    def display_balance(self): # This displays the account balance.
        print("\n-----------------------------------------")
        print("============ DISPLAY BALANCE ============")
        print("-----------------------------------------")
        print(f"Customer first name: {self.customer.name}")
        print(f"Customer last name: {self.customer.surname}") 
        print("------------------------------------------")
        print(f"Account number: {self.account_number}")
        print(f"Account balance: ${self.account_balance}")
        print("------------------------------------------\n")



# self,name, surname, TR_ID, phone

customer_one = Customer("Alexander", "Mercelo", 3241, "064878788")  
customer_two = Customer("Revaldo", "Junior", 3261, "063246783")  
customer_three = Customer("Mike", "Devinchi", 3261, "063246783")



# customer, account_number, account_balance

account_one = Account(customer_one,"Nl07ING11012897", 100500)
account_two = Account(customer_two,"NL07ING11020875", 1000000)
account_three = Account(customer_three,"NL70ING11031764",1000 )


Customer.display_customer_information(customer_one)
Customer.customers_list()
Account.deposit(account_three,200)
Account.money_check(account_three,1500)
Account.display_balance(account_three)



