# # # import csv
# # # with open("students.csv","r") as file:
# # #     # reader= csv.reader(file)
# # #     reader = csv.DictReader(file)
# # #     next(reader)
# # #     for row in reader:
# # #         print(row)

# # #         print(row["Name"])

# # # javascript object notation  json 




# # # {
# # #     "name":"Ali",
# # #     "age":21,
# # #     "city":"Delhi"
# # # }

# # import json
# # with open("student.json","r") as file:
# #     data= json.load(file)

# # print(data)

# # print(data["name"])
# # print(data["age"])

# # student={
# #     "name":"ABCD",
# #     "age": "22",
# #     "city":"MUmbai"

# # }

# # with open("student.json","w") as file:
# #     data2= json.dump(student,file,indent=4)

# # print(data2)



# response={

# "model":"gpt-4",

# "answer":"Python is easy.",

# "tokens":120

# }

# import json

# with open("response.json","w") as file:

#     json.dump(response,file,indent=4)







class InsufficientBalanceError(Exception):
    pass 

balance = 500
try:

    amount = 100

    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance")
except InsufficientBalanceError as e:
    print(e)





class MissingAPIKeyError(Exception):
    pass


api_key=""

if not api_key:
    raise MissingAPIKeyError("Api key not available")


