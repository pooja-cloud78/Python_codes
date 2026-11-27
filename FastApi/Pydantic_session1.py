# Before pydantic

class Student:
    def __init__(self, name:str, age:int, gpa:float):
        self.name = name
        self.age = age
        self.gpa = gpa

s = Student(name = 99, age = "Twenty", gpa = False) 
print(s.name," ", s.age," ", s.gpa)     

# Basemodel class will ensures for correct types validation

print("-" * 20)
print("After Pydantic")
# After Pydantic

from pydantic import BaseModel

class Student(BaseModel):
    name : str
    age: int
    gpa: float

s1 = Student(name = "Ram", age = 30, gpa = 2.3)  
print(s1)  

# s2 = Student(name = 99, age = "abc", gpa = "False")  
# print(s2)         # shows error for name and age(False is converted to 0(Lax mode))

# Real world approach in API data will arrive in dictionary

raw_data = {
    "name": "Sham",
    "age": 20,
    "gpa": 3.5
}

s2 = Student(**raw_data)     # sending data in dict form
print(s2)

print("-" *20)

# change the type of gpa but its convertable so no error here
raw_data1={
    "name": "Sham",
    "age": 29,
    "gpa": "3.4"         #convert the type and will work
}

s3 = Student(**raw_data1)
print(s3)
print(type(s3.name), type(s3.age), type(s3.gpa))

# change the type of age to float but its not convertable
raw_data2={
    "name": "Sham",
    "age": 12.4,            # shows error for age as its float
    "gpa": "3.4"         
}

# s4 = Student(**raw_data2)
# print(s4)

# ValidationError
from pydantic import ValidationError

# different types of name,age and missing gpa
raw_data4 = {
    "name": 1234,
    "age": "Twenty"
} 
 
try:
    s5 = Student(**raw_data4)
except ValidationError as e:
    print(f"Total number of errors: {e.error_count()}")  
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")  
   
print("-" * 20)

"""
Try writing a small Product(BaseModel) in your notebook with fields: 
product_id: int, name: str, price: float, in_stock: bool, 
and test it with:

Valid coerced inputs (product_id="50", price="199.99", in_stock="1").
A broken input inside try / except ValidationError as e: and print e.error_count().
"""

from pydantic import BaseModel,ValidationError

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    in_stock:bool

input = {
    "product_id": "50",
    "price": "199.99",
    "in_stock": "1"
}    

try:
    p = Product(**input)
except ValidationError as e:
    print(f"Total errors: {e.error_count()}")
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")    

print("*" * 20)

# Validation types
print("validation types")        

from pydantic import BaseModel,ValidationError

class Product(BaseModel):
    product_id: int
    name: str
# Required and non-nullable
# what happens when value is not provided in dict

value = {
    "product_id": "50"         # name is missing here
}    

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")

print("-"*20)
# Required and Non-nullable 
# what happens if value is None
value = {
    "product_id" : "50",
    "name": None          # error of valid string type (not none)
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")

print("-"*20)

from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str | None

# Required and nullable 
# what happens when value is not provided in dict 
value = {
    "product_id" : "50"               # shows one error of missing field
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")


print("-"*20)
# Required and nullable 
# what happens if value is None
value = {
    "product_id" : "50",
    "name": None
}

try:
    p1 = Product(**value)
    print(p1)              # no error as name can be str or none
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")
            