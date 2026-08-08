# # # # # # # # # # twenty  20  
# # # # # # # # # # pydantic   data parsing     

# # # # # # # # # user = {

# # # # # # # # #     "name": "Alice",

# # # # # # # # #     "age": "25"

# # # # # # # # # }

# # # # # # # # # print(type(user["age"]))


# # # # # # # # # user = {

# # # # # # # # #     "name": "Alice",

# # # # # # # # #     "age": "Twenty"

# # # # # # # # # }

# # # # # # # # # if not isinstance(user["age"], int):

# # # # # # # # #     print("Invalid Age")

# # # # # # # # from pydantic import BaseModel
# # # # # # # # class User(BaseModel):
# # # # # # # #     name: str
# # # # # # # #     age: int

# # # # # # # # user = User(name="Ali", age=34)

# # # # # # # # # print(user)


# # # # # # # # from pydantic import BaseModel

# # # # # # # # class User(BaseModel):

# # # # # # # #     name: str

# # # # # # # #     age: int

# # # # # # # # user = User(

# # # # # # # #     name="Alice",

# # # # # # # #     age="Twenty"

# # # # # # # # )
# # # # # # # # print(user)



# # # # # # # from pydantic import BaseModel

# # # # # # # class Student(BaseModel):

# # # # # # #     name: str

# # # # # # #     age: int

# # # # # # #     course: str

# # # # # # # student = Student(

# # # # # # #     name="John",

# # # # # # #     age=20,

# # # # # # #     course="Computer Science"

# # # # # # # )

# # # # # # # print(student)


# # # # # # # from pydantic import BaseModel

# # # # # # # class PromptRequest(BaseModel):

# # # # # # #     prompt: str

# # # # # # #     max_tokens: int

# # # # # # # request = PromptRequest(

# # # # # # #     prompt="Explain Neural Networks",

# # # # # # #     max_tokens=500

# # # # # # # )

# # # # # # # print(request)


# # # # # # from pydantic import BaseModel

# # # # # # class User(BaseModel):

# # # # # #     name: str
# # # # # #     country: str = "India"
# # # # # #     age: int
# # # # # #     phone: Optional[str] = None
# # # # # # user = User(

# # # # # #     name="Alice",

# # # # # #     age=25

# # # # # # )

# # # # # # print(user)



# # # # # from pydantic import BaseModel, Field

# # # # # class User(BaseModel):

# # # # #     age: int = Field(

# # # # #         gt=0,

# # # # #         lt=120

# # # # #     )

# # # # # user = User(age=-5)

# # # # # print(user)

# # # # # from pydantic import BaseModel, EmailStr

# # # # # class User(BaseModel):

# # # # #     email: EmailStr

# # # # # user = User(

# # # # #     email="alice@example.com"

# # # # # )

# # # # # print(user)

# # # # from pydantic import BaseModel, EmailStr, Field

# # # # class Student(BaseModel):

# # # #     name: str

# # # #     age: int = Field(gt=17)

# # # #     email: EmailStr

# # # # student = Student(

# # # #     name="John",

# # # #     age=20,

# # # #     email="john@example.com"

# # # # )

# # # # print(student)

# # # from pydantic import BaseModel, Field

# # # class PromptRequest(BaseModel):

# # #     prompt: str = Field(

# # #         min_length=10,

# # #         max_length=500

# # #     )

# # #     max_tokens: int = Field(

# # #         gt=0,

# # #         le=2048

# # #     )

# # # request = PromptRequest(

# # #     prompt="Explain Artificial Intelligence.",

# # #     max_tokens=500

# # # )

# # # print(request)



# # from pydantic import BaseModel

# # class Address(BaseModel):

# #     city: str

# #     country: str


# # class Student(BaseModel):

# #     name: str

# #     age: int

# #     address: Address


# # student = Student(

# #     name="Alice",

# # #     age=21,

# # #     address={

# # #         "city": "Delhi",

# # #         "country": "India"

# # #     }

# # # )

# # # print(student)

# # # print(student.address.city)

# # # print(student.address.country)


# # from typing import List

# # from pydantic import BaseModel


# # class Student(BaseModel):

# #     name: str

# #     skills: List[str]


# # student = Student(

# #     name="Alice",

# #     skills=[

# #         "Python",

# #         "Machine Learning",

# #         "SQL"

# #     ]

# # )

# # print(student)

# from pydantic import BaseModel

# class User(BaseModel):

#     name: str

#     age: int


# user = User(

#     name="Alice",

#     age=25

# )

# print(user.model_dump())
# print(user.model_dump_json(indent=2))



# data = {

#     "name":"Alice",

#     "age":25

# }

# user = User(**data)

# print(user)

# class Address(BaseModel):

#     city: str

#     country: str


# class Student(BaseModel):

#     name: str

#     address: Address


# class Teacher(BaseModel):

#     name: str

#     address: Address


from pydantic import BaseModel

class UserInfo(BaseModel):

    username: str

    subscription: str


class PromptRequest(BaseModel):

    user: UserInfo

    prompt: str

    model: str

    max_tokens: int


request = PromptRequest(

    user={

        "username":"Alice",

        "subscription":"Premium"

    },

    prompt="Explain Deep Learning",

    model="gpt-4",

    max_tokens=500

)

print(request)




a=5
b=10
c=a*b
print(c)


price = 5
quantity = 10

total_price = price * quantity

print(total_price)




avoid duplicate code  



write clear comments 

#increment x 

# increase retry count after a failed api request 

