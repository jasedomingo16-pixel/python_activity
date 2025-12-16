class Animal:
    def __init__(self, species):
        self.species = species
    
    def walk(self):
        print(f"The {self.species} is walking.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(species="Canine") 
        self.name = name

    def bark(self):
        print(f"{self.name} the {self.species} says Woof!")

dog_instance = Dog("Buddy")
dog_instance.walk() 
dog_instance.bark()
print("-" * 30)


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def role(self):
        print(f"{self.name} is a salaried employee.")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        
    def project_info(self):
        print(f"Project name: {self.project_name}")

class TeamLead(Employee, Project):
    def __init__(self, name, emp_id, project_name):
        Employee.__init__(self, name, emp_id)
        Project.__init__(self, project_name)
        
    def details(self):
        print(f"Team Lead {self.name} (ID: {self.emp_id}) manages the project: {self.project_name}.")

lead = TeamLead("Dashy", "TL001", "AI Development")
lead.role()   
lead.project_info()  
lead.details()
print("-" * 30)

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    
    def move(self):
        print(f"The {self.vehicle_type} is moving.")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(vehicle_type="Car")
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}.")

class SportsCar(Car):
    def __init__(self, make, model, top_speed):
        super().__init__(make, model)
        self.top_speed = top_speed

    def race(self):
        self.move()    
        self.drive()   
        print(f"The {self.make} {self.model} can reach {self.top_speed} mph.")

sports_car = SportsCar("Ferrari", "488 GTB", 205)
sports_car.race()
print("-" * 30)


class Shape:
    def __init__(self, color):
        self.color = color
        
    def describe(self):
        print(f"This shape is colored {self.color}.")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area_circle(self):
        area = 3.14 * self.radius ** 2
        print(f"A {self.color} circle with radius {self.radius} has an area of {area:.2f}.")

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def perimeter_square(self):
        perimeter = 4 * self.side
        print(f"A {self.color} square with side {self.side} has a perimeter of {perimeter}.")

circle = Circle("Blue", 5)
circle.describe()
circle.area_circle()

square = Square("Red", 4)
square.describe()
square.perimeter_square()
print("-" * 30)


class Person:
    def __init__(self, name):
        self.name = name

    def identity(self):
        print(f"Identity: {self.name}")

class Developer(Person):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.language = programming_language

    def code(self):
        print(f"{self.name} is writing code in {self.language}.")

class Manager:
    def __init__(self, team_size):
        self.team_size = team_size

    def manage_team(self):
        print(f"Manages a team of {self.team_size} people.")

class TechLead(Developer, Manager):
    def __init__(self, name, programming_language, team_size):
        Developer.__init__(self, name, programming_language) 
        Manager.__init__(self, team_size) 

    def lead_project(self):
        self.identity() 
        self.code()    
        self.manage_team() 
        print(f"As Tech Lead, {self.name} coordinates both coding and team management.")

tech_lead = TechLead("Renz", "Python", 8)
tech_lead.lead_project()
print("-" * 30)