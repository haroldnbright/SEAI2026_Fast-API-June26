# Pydantic - Python library used for data validation.
# Python is a dynamically typed language.

# x = 10
# print(x, " -> ", type(x))
# x = "masai"
# print(x, " -> ", type(x))
# 
# For production grade applications, data validation is very important.
# Because dynamically typed behaviour of Python can lead to unexpected erros.
# age <- 'thirty'
# DRY - Don't Repeat Yourself

# Type Hinting
def create_student(name: str, age: int, college: str):
    # Insert student details ject in database.
    # Before inserting these details in db, we should validate first.
    if type(name) == str and type(age) == int and type(college) == str:
        print(name)
        print(age)
        print(college)
    else:
        raise TypeError('Input data type is not correct.')

def update_student(name: str, age: int, college: str):
    # Insert student details ject in database.
    # Before inserting these details in db, we should validate first.
    if type(name) == str and type(age) == int and type(college) == str:
        print(name)
        print(age)
        print(college)
    else:
        raise TypeError('Input data type is not correct.')

# create_student("Kalpesh", 22, "Masai")

# Validating student details manually like this is not a good idea, as it leads to code repetition and is prone to errors.

# Pydantic - Data Validation
from pydantic import BaseModel, EmailStr
from typing import Dict, List

# Type Validation - Data Type Validation
# Ideal Student Objet - How a student object should look like ? 
# emergency_contact_numbers = {'father' : 8923789, 'mother' : 983748}
# marks = [90, 80, 60.6,]
# Validate an email - <......>@<....>.<...>
class Student(BaseModel):
    name: str
    email: EmailStr
    age: int
    college: str
    marks: float
    emergency_contact_numbers: Dict[str, int]

student_info = {'name' : 'Kalpesh', 'email' : 'kalpesh@gmail.com', 'age' : 22, 'college' : 'Masai', 'marks' : 90.1, 'emergency_contact_numbers' : {'father' : 123456, 'mother' : 98765} }

# ** => Unpacking - Taking values from a collection (list, dict ...) and assigning them to variables in one line 
student = Student(**student_info)
print(student)


