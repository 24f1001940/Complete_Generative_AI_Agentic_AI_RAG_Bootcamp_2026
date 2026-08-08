# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Object Oriented Programming (OOPS)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1_name="Ali"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1_age= 15
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1_rollno= 34


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2_name="Abcd"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2_age= 45
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2_rollno= 67


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 1000 thousands 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class      
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # house blueprint   ->  actual house   


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student class  -> student objects

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # object is an isinstance of a class


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class student:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1 = student()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2 = student()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student3 = student()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student4 = student()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ai agent 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # agent      ojbjects  travel email reserach 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1.name = "ali"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2.name= "abcd "



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # what is a constructor?


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Create Object

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ↓

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Constructor Runs Automatically

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ↓

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Object gets its own data

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class student:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.name= "Ali"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.age = 20
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         # print("Constructor Executed")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print(self)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1 = student()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student1.name)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student1.age)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2 = student()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name,age,marks):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.name= name
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.age = age
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.marks= marks
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def display(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Name",self.name)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("AGE",self.age)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Marks",self.marks)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1 = Student("Ali",20,91)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2 = Student("Sara",22,78)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1.display()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2.display()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student1.name)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student1.age)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student1.marks)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student2.name)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student2.age)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student2.marks)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class attribute vs instance attribute 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class student:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     college="XYZ"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.name = name


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student1= student("Ali")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student2= student("musa")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student1.name)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student1.college)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class AIModel:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     company="OpenAI"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,model_name,temperature):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.model_name=model_name

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.temperature=temperature

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def info(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Company:",self.company)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Model:",self.model_name)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Temperature:",self.temperature)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # model1=AIModel("GPT-4",0.7)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # model2=AIModel("GPT-4.1",0.2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # model1.info()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # model2.info()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Inheritance

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name,age):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.name=name
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.age=age
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def display(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print(self.name,self.age)    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Teacher:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name,age):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.name=name
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.age=age
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def display(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print(self.name,self.age)  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Person

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ↓

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Student

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ↓

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # GraduateStudent

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Person:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name,age):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.name=name

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.age=age

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def display(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Name:",self.name)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Age:",self.age)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Student(Person):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self, name, age,roll):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         super().__init__(name, age)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.roll=roll
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def show_roll(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Roll Number:",self.roll)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student=Student("Ali",34,101)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student.display()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # student.show_roll()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Employee(Person):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name,age,salary):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         super().__init__(name,age)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.salary=salary

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def show_salary(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Salary:",self.salary)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # emp=Employee("John",30,60000)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # emp.display()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # emp.show_salary()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Person:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def greet(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Hello")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Student(Person):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class GraduateStudent(Student):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # obj= GraduateStudent()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # obj.greet()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Camera:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def capture(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Capturing image")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class GPS:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def location(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Getting location")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Smartphone(Camera,GPS):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # phone=Smartphone()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # phone.capture()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # phone.location()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Vehicle:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def start(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Vehicle Started")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Car(Vehicle):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Bike(Vehicle):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # car=Car()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # bike=Bike()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # car.start()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # bike.start()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class AIModel:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def predict(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Generating prediction")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class GPTModel(AIModel):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class GeminiModel(AIModel):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # gpt=GPTModel()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # gemini=GeminiModel()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # gpt.predict()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # gemini.predict()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Polymorphism

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Dog:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Dog says: Bark")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Cat:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Cat says: Meow")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Cow:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Cow says: Moo")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # dog = Dog()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # cat = Cat()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # cow = Cow()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # dog.sound()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # cat.sound()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # cow.sound()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # animals = [Dog(),Cat(),Cow()]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for animal in animals:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     animal.sound()




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #method overriding

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Animal:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Animals make sounds")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Dog(Animal):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Dog says: Bark")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Cat(Animal):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Cat says: Meow")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # dog = Dog()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # cat = Cat()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # dog.sound()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # cat.sound()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Animal:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Animals make sounds")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Dog(Animal):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #         super().sound()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Dog says: Bark")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # dog = Dog()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # dog.sound()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # # # #     def introduction(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("I am a student")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # class Teacher:

# # # # # # # # # # # # # # # # # # # # # # # # # # # #     def introduction(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("I am a teacher")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # def introduce(person):

# # # # # # # # # # # # # # # # # # # # # # # # # # # #     person.introduction()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # introduce(Student())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # introduce(Teacher())


# # # # # # # # # # # # # # # # # # # # # # # # # # # class CreditCard:

# # # # # # # # # # # # # # # # # # # # # # # # # # #     def pay(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Payment using Credit Card")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # class UPI:

# # # # # # # # # # # # # # # # # # # # # # # # # # # #     def pay(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Payment using UPI")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # class Wallet:

# # # # # # # # # # # # # # # # # # # # # # # # # # # #     def pay(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Payment using Wallet")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # def process_payment(method):

# # # # # # # # # # # # # # # # # # # # # # # # # # # #     method.pay()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # process_payment(CreditCard())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # process_payment(UPI())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # process_payment(Wallet())





# # # # # # # # # # # # # # # # # # # # # # # # # # # # What is Encapsulation ?
# # # # # # # # # # # # # # # # # # # # # # # # # # # #   combining data and methods that opearte on that data into a single unit, whic is the class

# # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name):

# # # # # # # # # # # # # # # # # # # # # # # # # # #         self.name=name


# # # # # # # # # # # # # # # # # # # # # # # # # # # student=Student("Ali")

# # # # # # # # # # # # # # # # # # # # # # # # # # # print(student.name)


# # # # # # # # # # # # # # # # # # # # # # # # # # # student.name="Sara"

# # # # # # # # # # # # # # # # # # # # # # # # # # # print(student.name)

# # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # #         self._marks=90

# # # # # # # # # # # # # # # # # # # # # # # # # # # student=Student()

# # # # # # # # # # # # # # # # # # # # # # # # # # # print(student._marks)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # private members

# # # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # # #         self.__marks=90


# # # # # # # # # # # # # # # # # # # # # # # # # # # # student=Student()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(student.__marks)


# # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # #         self.__marks=90

# # # # # # # # # # # # # # # # # # # # # # # # # # #     def display(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # #         print(self.__marks)
# # # # # # # # # # # # # # # # # # # # # # # # # # # student=Student()

# # # # # # # # # # # # # # # # # # # # # # # # # # # student.display()

# # # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # #         self.__marks=90

# # # # # # # # # # # # # # # # # # # # # # # # # # #     def get_marks(self):

# # # # # # # # # # # # # # # # # # # # # # # # # # #         return self.__marks

# # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # # # # # # # # # # # #         self.__marks=0
# # # # # # # # # # # # # # # # # # # # # # # # # #     def get_marks(self):

# # # # # # # # # # # # # # # # # # # # # # # # # #         return self.__marks

# # # # # # # # # # # # # # # # # # # # # # # # # #     def set_marks(self,marks):

# # # # # # # # # # # # # # # # # # # # # # # # # #         if 0<=marks<=100:

# # # # # # # # # # # # # # # # # # # # # # # # # #             self.__marks=marks

# # # # # # # # # # # # # # # # # # # # # # # # # #         else:

# # # # # # # # # # # # # # # # # # # # # # # # # #             print("Invalid Marks")


# # # # # # # # # # # # # # # # # # # # # # # # # # student=Student()

# # # # # # # # # # # # # # # # # # # # # # # # # # student.set_marks(95)

# # # # # # # # # # # # # # # # # # # # # # # # # # print(student.get_marks())




# # # # # # # # # # # # # # # # # # # # # # # # # # @property


# # # # # # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # # # # # # # # # # # #         self.__marks=90

# # # # # # # # # # # # # # # # # # # # # # # # # #     @property
# # # # # # # # # # # # # # # # # # # # # # # # # #     def marks(self):

# # # # # # # # # # # # # # # # # # # # # # # # # #         return self.__marks

# # # # # # # # # # # # # # # # # # # # # # # # # #     @marks.setter
# # # # # # # # # # # # # # # # # # # # # # # # # #     def marks(self,value):

# # # # # # # # # # # # # # # # # # # # # # # # # #         if 0<=value<=100:

# # # # # # # # # # # # # # # # # # # # # # # # # #             self.__marks=value


# # # # # # # # # # # # # # # # # # # # # # # # # # student=Student()

# # # # # # # # # # # # # # # # # # # # # # # # # # print(student.marks)

# # # # # # # # # # # # # # # # # # # # # # # # # # student.marks=97

# # # # # # # # # # # # # # # # # # # # # # # # # # print(student.marks)




# # # # # # # # # # # # # # # # # # # # # # # # # class BankAccount:

# # # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,balance):

# # # # # # # # # # # # # # # # # # # # # # # # #         self.__balance=balance

# # # # # # # # # # # # # # # # # # # # # # # # #     def deposit(self,amount):

# # # # # # # # # # # # # # # # # # # # # # # # #         self.__balance+=amount

# # # # # # # # # # # # # # # # # # # # # # # # #     def withdraw(self,amount):

# # # # # # # # # # # # # # # # # # # # # # # # #         if amount<=self.__balance:

# # # # # # # # # # # # # # # # # # # # # # # # #             self.__balance-=amount

# # # # # # # # # # # # # # # # # # # # # # # # #         else:

# # # # # # # # # # # # # # # # # # # # # # # # #             print("Insufficient Balance")

# # # # # # # # # # # # # # # # # # # # # # # # #     def show_balance(self):

# # # # # # # # # # # # # # # # # # # # # # # # #         print("Balance:",self.__balance)

# # # # # # # # # # # # # # # # # # # # # # # # # account=BankAccount(1000)

# # # # # # # # # # # # # # # # # # # # # # # # # account.deposit(500)

# # # # # # # # # # # # # # # # # # # # # # # # # account.withdraw(200)

# # # # # # # # # # # # # # # # # # # # # # # # # account.show_balance()

# # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # abstract class
# # # # # # # # # # # # # # # # # # # # # # # # # abc 
# # # # # # # # # # # # # # # # # # # # # # # # # from abc import ABC, abstractmethod
# # # # # # # # # # # # # # # # # # # # # # # # from abc import ABC, abstractmethod

# # # # # # # # # # # # # # # # # # # # # # # # class Animal(ABC):

# # # # # # # # # # # # # # # # # # # # # # # #     @abstractmethod
# # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # #         pass

# # # # # # # # # # # # # # # # # # # # # # # # # animal = Animal()
# # # # # # # # # # # # # # # # # # # # # # # # class Dog(Animal):

# # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # #         print("Dog says: Bark")

# # # # # # # # # # # # # # # # # # # # # # # # class Cat(Animal):

# # # # # # # # # # # # # # # # # # # # # # # #     def sound(self):
# # # # # # # # # # # # # # # # # # # # # # # #         print("Cat says: Meow")


# # # # # # # # # # # # # # # # # # # # # # # # dog = Dog()

# # # # # # # # # # # # # # # # # # # # # # # # cat = Cat()

# # # # # # # # # # # # # # # # # # # # # # # # dog.sound()

# # # # # # # # # # # # # # # # # # # # # # # # cat.sound()
# # # # # # # # # # # # # # # # # # # # # # # from abc import ABC, abstractmethod

# # # # # # # # # # # # # # # # # # # # # # # class Shape(ABC):

# # # # # # # # # # # # # # # # # # # # # # #     @abstractmethod
# # # # # # # # # # # # # # # # # # # # # # #     def area(self):
# # # # # # # # # # # # # # # # # # # # # # #         pass

# # # # # # # # # # # # # # # # # # # # # # # class Rectangle(Shape):

# # # # # # # # # # # # # # # # # # # # # # #     def __init__(self,length,width):

# # # # # # # # # # # # # # # # # # # # # # #         self.length=length

# # # # # # # # # # # # # # # # # # # # # # #         self.width=width

# # # # # # # # # # # # # # # # # # # # # # #     def area(self):

# # # # # # # # # # # # # # # # # # # # # # #         return self.length*self.width
# # # # # # # # # # # # # # # # # # # # # # # rectangle = Rectangle(10,5)

# # # # # # # # # # # # # # # # # # # # # # # print(rectangle.area())



# # # # # # # # # # # # # # # # # # # # # # # from abc import ABC, abstractmethod

# # # # # # # # # # # # # # # # # # # # # # # class AIModel(ABC):

# # # # # # # # # # # # # # # # # # # # # # #     @abstractmethod
# # # # # # # # # # # # # # # # # # # # # # #     def generate(self,prompt):
# # # # # # # # # # # # # # # # # # # # # # #         pass


# # # # # # # # # # # # # # # # # # # # # # # class GPTModel(AIModel):

# # # # # # # # # # # # # # # # # # # # # # #     def generate(self,prompt):

# # # # # # # # # # # # # # # # # # # # # # #         return f"GPT Response: {prompt}"

# # # # # # # # # # # # # # # # # # # # # # # class GeminiModel(AIModel):

# # # # # # # # # # # # # # # # # # # # # # #     def generate(self,prompt):

# # # # # # # # # # # # # # # # # # # # # # #         return f"Gemini Response: {prompt}"

# # # # # # # # # # # # # # # # # # # # # # # gpt=GPTModel()

# # # # # # # # # # # # # # # # # # # # # # # gemini=GeminiModel()

# # # # # # # # # # # # # # # # # # # # # # # print(gpt.generate("Hello"))

# # # # # # # # # # # # # # # # # # # # # # # print(gemini.generate("Hello"))





# # # # # # # # # # # # # # # # # # # # # # # __init__   __str__  
# # # # # # # # # # # # # # # # # # # # # # # dunder    double underscore    

# # # # # # # # # # # # # # # # # # # # # # # __init__       
# # # # # # # # # # # # # # # # # # # # # # # __str__
# # # # # # # # # # # # # # # # # # # # # # # __repr__
# # # # # # # # # # # # # # # # # # # # # # # __len__
# # # # # # # # # # # # # # # # # # # # # # # __eq__
# # # # # # # # # # # # # # # # # # # # # # # __add__

# # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name):

# # # # # # # # # # # # # # # # # # # # # #         self.name=name


# # # # # # # # # # # # # # # # # # # # # # student=Student("Ali")

# # # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # # #     def __init__(self,name):

# # # # # # # # # # # # # # # # # # # # # #         self.name=name


# # # # # # # # # # # # # # # # # # # # # # student=Student("Ali")

# # # # # # # # # # # # # # # # # # # # # # print(student) 











# # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # #     def __init__(self,name):

# # # # # # # # # # # # # # # # # # # # #         self.name=name

# # # # # # # # # # # # # # # # # # # # #     def __str__(self):

# # # # # # # # # # # # # # # # # # # # #         return f"Student Name: {self.name}"


# # # # # # # # # # # # # # # # # # # # # student=Student("Ali")

# # # # # # # # # # # # # # # # # # # # # print(student)

# # # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # # #     def __init__(self,name):

# # # # # # # # # # # # # # # # # # # # #         self.name=name

# # # # # # # # # # # # # # # # # # # # #     def __repr__(self):

# # # # # # # # # # # # # # # # # # # # #         return f"Student('{self.name}')"


# # # # # # # # # # # # # # # # # # # # # student=Student("Ali")

# # # # # # # # # # # # # # # # # # # # # print(student)       Student('Ali')



# # # # # # # # # # # # # # # # # # # # class Playlist:

# # # # # # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # # # # # #         self.songs=["Song1","Song2","Song3"]

# # # # # # # # # # # # # # # # # # # #     def __len__(self):

# # # # # # # # # # # # # # # # # # # #         return len(self.songs)


# # # # # # # # # # # # # # # # # # # # playlist=Playlist()

# # # # # # # # # # # # # # # # # # # # print(len(playlist))

# # # # # # # # # # # # # # # # # # # # eq()

# # # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # # #     def __init__(self,name):

# # # # # # # # # # # # # # # # # # # #         self.name=name


# # # # # # # # # # # # # # # # # # # # s1=Student("Ali")

# # # # # # # # # # # # # # # # # # # # s2=Student("Ali")

# # # # # # # # # # # # # # # # # # # # print(s1==s2)   

# # # # # # # # # # # # # # # # # # # class Student:

# # # # # # # # # # # # # # # # # # #     def __init__(self,name):

# # # # # # # # # # # # # # # # # # #         self.name=name

# # # # # # # # # # # # # # # # # # #     def __eq__(self,other):

# # # # # # # # # # # # # # # # # # #         return self.name==other.name


# # # # # # # # # # # # # # # # # # # s1=Student("Ali")

# # # # # # # # # # # # # # # # # # # s2=Student("Ali")

# # # # # # # # # # # # # # # # # # # print(s1==s2)


# # # # # # # # # # # # # # # # # # # # add()
# # # # # # # # # # # # # # # # # # # class Wallet:

# # # # # # # # # # # # # # # # # # #     def __init__(self,balance):

# # # # # # # # # # # # # # # # # # #         self.balance=balance

# # # # # # # # # # # # # # # # # # #     def __add__(self,other):

# # # # # # # # # # # # # # # # # # #         return self.balance+ other.balance


# # # # # # # # # # # # # # # # # # # w1=Wallet(500)

# # # # # # # # # # # # # # # # # # # w2=Wallet(300)

# # # # # # # # # # # # # # # # # # # print(w1+w2)


# # # # # # # # # # # # # # # # # # def __contains__(self,name):
# # # # # # # # # # # # # # # # # #     return name in self.members



# # # # # # # # # # # # # # # # # # call()
# # # # # # # # # # # # # # # # # class Greeting:

# # # # # # # # # # # # # # # # #     def __call__(self):

# # # # # # # # # # # # # # # # #         print("Welcome to Python")


# # # # # # # # # # # # # # # # # greet=Greeting()

# # # # # # # # # # # # # # # # # greet()

# # # # # # # # # # # # # # # # class ShoppingCart:

# # # # # # # # # # # # # # # #     def __init__(self):

# # # # # # # # # # # # # # # #         self.items=[]

# # # # # # # # # # # # # # # #     def add_item(self,item):

# # # # # # # # # # # # # # # #         self.items.append(item)

# # # # # # # # # # # # # # # #     def __len__(self):

# # # # # # # # # # # # # # # #         return len(self.items)

# # # # # # # # # # # # # # # #     def __str__(self):

# # # # # # # # # # # # # # # #         return f"Cart: {self.items}"


# # # # # # # # # # # # # # # # cart=ShoppingCart()

# # # # # # # # # # # # # # # # cart.add_item("Laptop")

# # # # # # # # # # # # # # # # cart.add_item("Mouse")

# # # # # # # # # # # # # # # # print(cart)

# # # # # # # # # # # # # # # # print(len(cart))


# # # # # # # # # # # # # # # # Operator Overloading

# # # # # # # # # # # # # # # # +   

# # # # # # # # # # # # # # # class Wallet:

# # # # # # # # # # # # # # #     def __init__(self,balance):

# # # # # # # # # # # # # # #         self.balance=balance

# # # # # # # # # # # # # # #     def __add__(self,other):

# # # # # # # # # # # # # # #         return Wallet(self.balance+other.balance)

# # # # # # # # # # # # # # #     def __str__(self):
# # # # # # # # # # # # # # #         return f"Balance: {self.balance}"

# # # # # # # # # # # # # # # wallet1=Wallet(500)

# # # # # # # # # # # # # # # wallet2=Wallet(300)
# # # # # # # # # # # # # # # wallet3= wallet1+ wallet2

# # # # # # # # # # # # # # # # print(wallet1+wallet2)
# # # # # # # # # # # # # # # print(wallet3)


# # # # # # # # # # # # # # class Wallet:

# # # # # # # # # # # # # #     def __init__(self,balance):

# # # # # # # # # # # # # #         self.balance=balance

# # # # # # # # # # # # # #     def __sub__(self,other):

# # # # # # # # # # # # # #         return Wallet(self.balance-other.balance)

# # # # # # # # # # # # # #     def __str__(self):

# # # # # # # # # # # # # #         return f"Balance: {self.balance}"


# # # # # # # # # # # # # # wallet1=Wallet(1000)

# # # # # # # # # # # # # # wallet2=Wallet(250)

# # # # # # # # # # # # # # print(wallet1-wallet2)



# # # # # # # # # # # # # # class Prompt:

# # # # # # # # # # # # # #     def __init__(self,text):

# # # # # # # # # # # # # #         self.text=text

# # # # # # # # # # # # # #     def __add__(self,other):

# # # # # # # # # # # # # #         return Prompt(self.text+" "+other.text)

# # # # # # # # # # # # # #     def __str__(self):

# # # # # # # # # # # # # #         return self.text 

# # # # # # # # # # # # # # Build a Production-Style AI Assistant Using OOP
# # # # # # # # # # # # # # GPT
# # # # # # # # # # # # # # Gemini
# # # # # # # # # # # # # # Claude
# # # # # # # # # # # # # # Llama


# # # # # # # # # # # # #     #              AIModel
# # # # # # # # # # # # #     #                 │
# # # # # # # # # # # # #     #     ┌───────────┴───────────┐
# # # # # # # # # # # # #     #     │                       │
# # # # # # # # # # # # #     #  GPTModel              GeminiModel
# # # # # # # # # # # # #     #     │                       │
# # # # # # # # # # # # #     #     └───────────┬───────────┘
# # # # # # # # # # # # #     #                 │
# # # # # # # # # # # # #     #            AI Assistant

# # # # # # # # # # # # # from abc import ABC, abstractmethod

# # # # # # # # # # # # # class AIModel(ABC):

# # # # # # # # # # # # #     def __init__(self, model_name):
# # # # # # # # # # # # #         self.model_name = model_name

# # # # # # # # # # # # #     @abstractmethod
# # # # # # # # # # # # #     def generate(self, prompt):
# # # # # # # # # # # # #         pass

# # # # # # # # # # # # # class GPTModel(AIModel):

# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         super().__init__("GPT-4.1")

# # # # # # # # # # # # #     def generate(self, prompt):
# # # # # # # # # # # # #         return f"GPT Response: {prompt}"


# # # # # # # # # # # # # class GeminiModel(AIModel):

# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         super().__init__("Gemini 2.5")

# # # # # # # # # # # # #     def generate(self, prompt):
# # # # # # # # # # # # #         return f"Gemini Response: {prompt}"


# # # # # # # # # # # # # class APIManager:

# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         self.__api_key = "secret_key"

# # # # # # # # # # # # #     def authenticate(self):
# # # # # # # # # # # # #         print("Authentication Successful")


# # # # # # # # # # # # # class AIAssistant:

# # # # # # # # # # # # #     def __init__(self, model):

# # # # # # # # # # # # #         self.model = model

# # # # # # # # # # # # #     def ask(self, prompt):

# # # # # # # # # # # # #         print(self.model.generate(prompt))


# # # # # # # # # # # # # gpt = GPTModel()

# # # # # # # # # # # # # assistant = AIAssistant(gpt)

# # # # # # # # # # # # # assistant.ask("Explain Machine Learning")


# # # # # # # # # # # # # gemini = GeminiModel()

# # # # # # # # # # # # # assistant = AIAssistant(gemini)

# # # # # # # # # # # # # assistant.ask("Explain Machine Learning")

# # # # # # # # # # # # # class Prompt:

# # # # # # # # # # # # #     def __init__(self, text):

# # # # # # # # # # # # #         self.text = text

# # # # # # # # # # # # #     def __str__(self):

# # # # # # # # # # # # #         return self.text

# # # # # # # # # # # # # prompt = Prompt("Explain Neural Networks")

# # # # # # # # # # # # # print(prompt)


# # # # # # # # # # # # # class Prompt:

# # # # # # # # # # # # #     def __init__(self, text):

# # # # # # # # # # # # #         self.text = text

# # # # # # # # # # # # #     def __add__(self, other):

# # # # # # # # # # # # #         return Prompt(self.text + " " + other.text)

# # # # # # # # # # # # #     def __str__(self):

# # # # # # # # # # # # #         return self.text


# # # # # # # # # # # # # p1 = Prompt("Explain")

# # # # # # # # # # # # # p2 = Prompt("Transformers")

# # # # # # # # # # # # # p3 = p1 + p2

# # # # # # # # # # # # # print(p3)


# # # # # # # # # # # # # gpt = GPTModel()

# # # # # # # # # # # # # assistant = AIAssistant(gpt)

# # # # # # # # # # # # # prompt = Prompt("What is Deep Learning?")

# # # # # # # # # # # # # assistant.ask(prompt)

# # # # # # # # # # # # # iteration   
# # # # # # # # # # # # numbers = [10,20,30,40,50]
# # # # # # # # # # # # for number in numbers:
# # # # # # # # # # # #     print(number)


# # # # # # # # # # # # # iterable vs iterator 
# # # # # # # # # # # # iterator = iter(numbers)
# # # # # # # # # # # # print(iterator)

# # # # # # # # # # # # print(next(iterator))
# # # # # # # # # # # # print(next(iterator))
# # # # # # # # # # # # print(next(iterator))
# # # # # # # # # # # # print(next(iterator))



# # # # # # # # # # # # numbers = [10, 20]

# # # # # # # # # # # # iterator = iter(numbers)

# # # # # # # # # # # # while True:

# # # # # # # # # # # #     try:
# # # # # # # # # # # #         print(next(iterator))

# # # # # # # # # # # #     except StopIteration:
# # # # # # # # # # # #         print("Iteration Complete")
# # # # # # # # # # # #         break

# # # # # # # # # # # # text ="Python"
# # # # # # # # # # # # for letter in text:
# # # # # # # # # # # #     print(letter)


# # # # # # # # # # # class Counter:
# # # # # # # # # # #     def __init__(self):
# # # # # # # # # # #         self.current = 1
# # # # # # # # # # #     def __iter__(self):
# # # # # # # # # # #         return self
# # # # # # # # # # #     def __next__(self):
# # # # # # # # # # #         if self.current <=5:
# # # # # # # # # # #             number = self.current
# # # # # # # # # # #             self.current += 1
# # # # # # # # # # #             return number 
# # # # # # # # # # #         else:
# # # # # # # # # # #             raise StopIteration    

# # # # # # # # # # # counter = Counter()
# # # # # # # # # # # for number in counter:
# # # # # # # # # # #     print(number)


# # # # # # # # # # # Generator    function returns values one at a time 
# # # # # # # # # # def numbers():
# # # # # # # # # #     return [1,2,3,4,5]
# # # # # # # # # # # print(numbers())

# # # # # # # # # # def numbers():
# # # # # # # # # #     yield 1
# # # # # # # # # #     yield 2
# # # # # # # # # #     yield 3
# # # # # # # # # #     yield 4
# # # # # # # # # #     yield 5

# # # # # # # # # # print(numbers())

# # # # # # # # # # generator = numbers()
# # # # # # # # # # print(next(generator))
# # # # # # # # # # print(next(generator))
# # # # # # # # # # print(next(generator))
# # # # # # # # # # print(next(generator))
# # # # # # # # # # def count():

# # # # # # # # # #     for number in range(1, 6):

# # # # # # # # # #         yield number

# # # # # # # # # # for value in count():

# # # # # # # # # #     print(value)


# # # # # # # # # #     # memore efficiency

# # # # # # # # # # squares = (x*x for x in range(5))
# # # # # # # # # # for sq in squares:
# # # # # # # # # #     print(sq)


# # # # # # # # # # def infinite_numbers():

# # # # # # # # # #     number = 1

# # # # # # # # # #     while True:

# # # # # # # # # #         yield number

# # # # # # # # # #         number += 1

# # # # # # # # # # generator = infinite_numbers()

# # # # # # # # # # for _ in range(5):

# # # # # # # # # #     print(next(generator))
        
# # # # # # # # # # def image_batches():
# # # # # # # # # #     yield "Batch 1"
# # # # # # # # # #     yield "Batch 2"
# # # # # # # # # #     yield "Batch 3"
# # # # # # # # # #     yield "Batch 4"
# # # # # # # # # #     yield "Batch 5"
# # # # # # # # # #     yield "Batch 6"

# # # # # # # # # # for batch in image_batches():
# # # # # # # # # #     print(batch)


# # # # # # # # # def using_return():

# # # # # # # # #     print("Start")

# # # # # # # # #     return 10

# # # # # # # # #     print("End")


# # # # # # # # # print(using_return())


# # # # # # # # # def using_yield():

# # # # # # # # #     print("Start")

# # # # # # # # #     yield 10

# # # # # # # # #     print("End")


# # # # # # # # # generator = using_yield()

# # # # # # # # # print(next(generator))
# # # # # # # # # print(next(generator))


# # # # # # # # # Function Starts

# # # # # # # # # ↓

# # # # # # # # # yield 10

# # # # # # # # # ↓

# # # # # # # # # PAUSED

# # # # # # # # # ↓

# # # # # # # # # next()

# # # # # # # # # ↓

# # # # # # # # # Continue

# # # # # # # # # ↓

# # # # # # # # # Function Ends


# # # # # # # # numbers = (x*x for x in range(5))

# # # # # # # # print(numbers)


# # # # # # # # advantages of lazy evaluation 

# # # # # # # # lower memory usage 
# # # # # # # # effiicient processing of very large datasets 
# # # # # # # # better scalability 

# # # # # # # def outer():
# # # # # # #     message= "Welocme "
# # # # # # #     def inner():
# # # # # # #         print("Hello from inner function ")
# # # # # # #         print(message)
# # # # # # #     inner()
# # # # # # # outer()


# # # # # # # def greet():
# # # # # # #     message = "hello"

# # # # # # #     print(message)

# # # # # # # greet()

# # # # # # # # print(message)



# # # # # # def outer():

# # # # # #     message = "Hello Python"

# # # # # #     def inner():

# # # # # #         print(message)

# # # # # #     return inner

# # # # # # greet = outer()

# # # # # # greet()



# # # # # # outer()

# # # # # # │

# # # # # # ├── message = "Hello Python"

# # # # # # │

# # # # # # └── return inner()

# # # # # #         │

# # # # # #         ▼

# # # # # # inner() remembers

# # # # # # ↓

# # # # # # message = "Hello Python"


# # # # # def counter():

# # # # #     count = 0

# # # # #     def increment():

# # # # #         nonlocal count

# # # # #         count += 1

# # # # #         print(count)

# # # # #     return increment

# # # # # c = counter()

# # # # # c()

# # # # # c()

# # # # # c()


# # # # def discount(rate):

# # # #     def apply(price):

# # # #         return price - (price * rate)

# # # #     return apply

# # # # student_discount = discount(0.20)

# # # # festival_discount = discount(0.50)

# # # # print(student_discount(100))

# # # # print(festival_discount(100))


# # # def greet():
# # #     print("Welcome to python")

# # # message = greet
# # # message()


# # # def greet():

# # #     print("Hello")


# # # def execute(function):

# # #     function()


# # # execute(greet)
# # # def outer():

# # #     def inner():

# # #         print("Inside Inner Function")

# # #     return inner

# # # function = outer()

# # # function()



# # def decorator(function):
# #     def wrapper():
# #         print("Starting Fucntion")
# #         function()
# #         print("Ending Function")
# #     return wrapper

# # def greet():
# #     print("Helloe Everyone")

# # decorated= decorator(greet)
# # decorated()


# # # @ syntax  
# # def decorator(function):

# #     def wrapper():

# #         print("Starting")

# #         function()

# #         print("Ending")

# #     return wrapper


# # @decorator
# # def greet():

# #     print("Hello")


# # greet()



# # def decorator(function):

# #     def wrapper(name):

# #         print("Starting")

# #         function(name)

# #         print("Ending")

# #     return wrapper


# # @decorator
# # def greet(name):

# #     print("Hello",name)


# # greet("Ali")

# # # *args **kwargs

# # def decorator(function):

# #     def wrapper(*args, **kwargs):

# #         print("Starting")

# #         function(*args, **kwargs)

# #         print("Ending")

# #     return wrapper


# # @decorator
# # def add(a, b):

# #     print(a + b)


# # add(10, 20)

# # from functools import wraps

# # def decorator(function):

# #     @wraps(function)

# #     def wrapper(*args, **kwargs):

# #         print("Running...")

# #         return function(*args, **kwargs)

# #     return wrapper


# # @decorator
# # def square(number):

# #     return number**2


# # print(square.__name__)

# # @timer 

# # def log_prompt(function):

# #     def wrapper(prompt):

# #         print(f"Prompt: {prompt}")

# #         return function(prompt)

# #     return wrapper


# # @log_prompt
# # def generate(prompt):

# #     return f"AI Response: {prompt}"


# # print(generate("Explain Machine Learning"))

# # @app.route()
# # @tf.function


# prompts = [

#     "Explain Machine Learning",

#     "What is Deep Learning?",

#     "Define Neural Networks",

#     "Explain Transformers",

#     "What is Reinforcement Learning?"
# ]

# def prompt_generator(data):

#     for prompt in data:

#         yield prompt

# generator = prompt_generator(prompts)

# for prompt in generator:

#     print(prompt)


# def prompt_builder(role):

#     def build(question):

#         return f"{role}: {question}"

#     return build

# teacher = prompt_builder("Teacher")

# print(teacher("Explain AI"))


# from functools import wraps 
# def logger(function):
#     @wraps(function)

#     def wrapper(*args,**kwargs):
#         print("Processign started ")
#         result = function(*args, **kwargs)
#         print("Processing Finished")

#         return result
#     return wrapper


# @logger
# def generate_response(prompt):
#     return f"AI Response -> {prompt}"

# print(generate_response("Explain Python"))


# responses = [

#     generate_response(prompt)

#     for prompt in prompts
# ]

# iterator = iter(responses)

# print(next(iterator))

# print(next(iterator))


# teacher = prompt_builder("Teacher")

# for prompt in prompt_generator(prompts):

#     formatted = teacher(prompt)

#     response = generate_response(formatted)

#     print(response)  




