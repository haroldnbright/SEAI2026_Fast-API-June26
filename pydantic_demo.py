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
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Dict, List

# Custom Validation.
# email should only be masai.com

# Type Validation - Data Type Validation
# Ideal Student Objet - How a student object should look like ? 
# emergency_contact_numbers = {'father' : 8923789, 'mother' : 983748}
# marks = [90, 80, 60.6,]
# Validate an email - <......>@<....>.<...>
# Field Validation
# By default all the parameters defined in Pydantic BaseModel are Mandatory
class Student(BaseModel):
    name: str = Field(max_length=50, description="Provide the name of the student.")
    email: EmailStr
    age: int # age >= 0 and age <= 100
    college: str
    marks: float = Field(default=10.0)
    emergency_contact_numbers: Dict[str, int]

    # This field validator is used to validate if email belongs to masai.com or not.
    # deepak@masai.com => split by @ => ['deepak', 'masai.com']
    # In Pydantic, @classmethod is mainly used with validators because validators belong to the model class, not to a specific object instance.
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        # email - abc@masai.com
        domain_name = value.split('@')[-1]

        if domain_name != 'masai.com':
            raise ValueError('Not a valid email address.')
        
        # valid email.
        return value
    
    @field_validator('college')
    @classmethod
    def transform_college(cls, value):
        return value.lower()
    
    # By default the mode is after, that means we get the value inside field_validator after conversion.
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        # print(value, " -> ", type(value))
        if value < 0 or value > 100:
            # invalid age
            raise ValueError('Age should be in the range of 0 to 100')
        
        return value
    
    # If age < 18, then emergency_contact_numbers should have father's phone number.
    @model_validator(mode='after')
    @classmethod
    def validate_contact_number(cls, model):
        if model.age < 18 and 'father' not in model.emergency_contact_numbers:
            raise ValueError('If age of student is < 18 then father contact number is mandatory.')
        
        return model
    
    @computed_field
    @property
    def score(self) -> float:
        return self.marks * 10

student_info = {'name' : 'Kalpesh', 'email' : 'kalpesh@masai.com', 'age' : '22', 'college' : 'MASAI', 'marks' : 90.1, 'emergency_contact_numbers' : {'father' : 123456, 'mother' : 98765} }

# ** => Unpacking - Taking values from a collection (list, dict ...) and assigning them to variables in one line 
student = Student(**student_info)
print(student)


