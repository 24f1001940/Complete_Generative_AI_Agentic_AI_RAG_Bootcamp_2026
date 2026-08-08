# # # # def greet(name="Student"):
# # # #     print(f"Hello {name}")
# # # # # greet("abc")
# # # # greet()
# # # # greet("abcd")



# # # # def generate_response(model="gpt-4"):
# # # #     print("Using",model)

# # # # generate_response()

# # # def connect(host="localhost",port=8000):
# # #     print(host,port)

# # # connect()


# # # def add(a=5, b):

# # # def student(name,age):
# # #     print(name,age)
# # # # student("Ali","15")

# # # student(age=21,name="Ali")



# # # def movie(name,year,rating):
# # #     print(name,year,rating)

# # # movie("Omar Series", year=2009,rating=5)
# # # movie(name="Avatar",2009,67)




# # #Variable arguments

# # def total(*numbers):
# #     print(numbers)

# # total(2,4,6)


# # def total2(*numbers):
# #     print(sum(numbers))

# # total2(10,20)
# # total2(1,2,3,4,5,6,7,8,9,10)   



# # def predict(*inputs):
# #     print(inputs)

# # predict(24,343,234)



# # # **kwargs
# # def profile(**details):
# #     print(details)
# # profile(name="Ali",age=5)

# # def demo(a,b=5,*args,**kwargs):
# #     print(a)
# #     print(b)
# #     print(args)        # alt+shift+bottom arrow button
# #     print(kwargs)
# # demo(10,20,30,40,name="Ali",city="Delhi")




# # # lambda functions 
# # # def sq(x):
# # #     return x*x

# # # sq2= lambda x:x*x
# # # print(sq(5))
# # # print(sq2(5))

# students = [("Ali", 92), ("musa", 56), ("saqib", 57)]
# st = sorted(students, key=lambda x: x[1])
# print(st)



# #map function
# numbers=[1,2,3,4,5]
# result=list(map(lambda x:x*x,numbers))
# print(result)

# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)




# numbers =[1,2,3,4,5]
# result = list(map(lambda x:x*x,filter(lambda x:x%2 ==0 ,numbers)))
# print(result)





# name = "Ali"
# print("Hello", name)

# name = "Sara"
# print("Hello", name)

# name = "John"
# print("Hello", name)



# def greet(name):
#     print(f"Hello {name}")

# greet("Ali")
# greet("Sara")
# greet("John")



# #keep functions small 

# #meaningful variables names 

# a=100
# b=5
# c= a*b


# price = 100
# quantity= 5
# total_price = price* quantity

# # def x():


# # def calculate_total():

# discount= price *0.10
# tax = price * 0.10

# tax_rate = 0.10
# tax = price * tax_rate


# # 6. use modules 
# # def calulate_area(radius):
# #     return 3.14*radius*radius

# # from math_utils import calculate_area
# # print(calculate_area(5))

# # add docstrings 
# def square(number):
#     """
#     returns the square of number.
#     """

#     return number*number



# number = int(input())
# try:
#     number=int(input())
# except ValueError:
#     print("Invalid number")


# # returning values in function instead of printing
# # aboid global variables



# # project/

# # main.py

# # utils.py

# # model.py

# # config.py

# # data/


# structured data     predefined format 

# Ali
# 21
# Delhi


# Name,Age,City
# Ali,21,Delhi
# Sara,22,Mumbai
# John,20,Delhi


# json 

# {
#     "name":"Ali",
#     "age":21,
#     "city":"Delhi"
# }












