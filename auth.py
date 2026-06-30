# pip3 install passlib
# pip3 install "python-jose[cryptography]"

import secrets
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr

security_app = HTTPBasic()

class User(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

fake_users_db = {
    "kalpesh" : {
        "name" : "Kalpesh Sanwlot",
        "username" : "kalpesh",
        "email" : "kalpesh@gmail.com",
        "password" : "$2a$12$Ut3c5PZ4GH8pzRj1puQwyO0Rjub6cF/gK0dSMsBk0DOtdNCV3WH3a" 
    },
    "jyotirmay" : {
        "name" : "Jyotirmay Verma",
        "username" : "jyotirmay",
        "email" : "jyotirmay@gmail.com",
        "password" : ""
    }
}

bcrypt_lib = CryptContext(schemes=["bcrypt"])

# 1. Sign Up
def signup(input_user_object: User):
    username = input_user_object.username

    user_from_db = fake_users_db.get(username)

    if user_from_db:
        # if user is already present in the db then raise an error.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists, please try a different username")

    db_user = {}
    db_user["username"] = input_user_object.username
    db_user["name"] = input_user_object.name
    db_user["email"] = input_user_object.email

    #password -> bcrypt password
    encoded_password = bcrypt_lib.hash(input_user_object.password)

    db_user["password"] = encoded_password

    fake_users_db[username] = db_user

# authenticate user
# We need to authenticate the user user with every API call.
def authenticate_user(username: str, password: str):
    # username = user_details.username
    user_from_db = fake_users_db[username]

    if username not in fake_users_db:
        # user doesn't exist.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found, please signup first."
        )

    # User found in the database.
    # Verify the password - In the Database, we are storing the encoded password using Bcrypt, so to verify we can not simply compare the incoming password and the password present in the database, we need to use the verify() method from Bcrypt to verify the incoming and the database password.
    if bcrypt_lib.verify(password, user_from_db["password"]):
        # Password is matching -> Authentication successful. 
        # Generate a token and return.
        return username
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Credentials."
    )

# authenticate_user("kalpesh", "abcd")

# pip install "passlib[argon2]"
# argon_lib = CryptContext(schemes=["agron2"])
# argon_lib.hash(password)
# argon_lib.verify(raw_pass, encoded_password)