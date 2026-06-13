from fastapi import FastAPI, Depends, HTTPException
from enum import Enum

app = FastAPI()

# Type of APIs -> Create (POST) / Read (GET) / Update (PUT/PATCH) / Delete (DELETE)
# CRUD Operations
# HTTP Methods - POST, GET, PUT, PATCH, DELETE

# amazon.in/search
# amazon.in/placeorder
# amazon.in/cancelorder
# amazon.in/updateaddress

# Fake Orders Database
ORDERS = {
    "ORD-101": {
        "status": "shipped",
        "city": "Delhi",
        "amount": 2500,
        "delivery_days": 2
    },
    "ORD-102": {
        "status": "cancelled",
        "city": "Bangalore",
        "amount": 4000,
        "delivery_days": 0
    },
    "ORD-103": {
        "status": "delivered",
        "city": "Mumbai",
        "amount": 1500,
        "delivery_days": 0
    }
}

# POST Method
# http://127.0.0.1/orders/order_id=ORD-101/status=""/date=""/amount=-100

# http://127.0.0.1:8000 ==> http://localhost:8000
# LocalHost - http://localhost:8000/hello
@app.get("/hello")
def say_hello():
    return "Hello Everyone!"

@app.get("/hi")
def say_hello():
    return "Hi Everyone!"

# If we redefine an api end point again in FastAPI, it will always use the first endpoint, second one will never execute.
# @app.get("/hello")
# def say_hi():
#     return "Hi Everyone!"

# LocalHost - http://localhost:8000/bye
@app.get("/bye")
def say_bye():
    return "Bye Bye Everyone!"

# pip3 install fastapi
# pip3 install uvicorn
# uvicorn sample:app --reload

# PATH Variable
# /orders/101
# http://127.0.01:8000/orders/101
@app.get("/orders/{order_id}")
def get_order_details(order_id: str):
    # Check the DB and fetch the order wtih the given order_id.
    order = ORDERS.get(order_id)

    if not order:
        return f"No order found for the order id: {order_id}, Please provide a valid order id."

    return order

# http://127.0.0.1:8000/order/ORD-101/status -> returns order status 
# http://127.0.0.1:8000/order/ORD-101/amount -> returns order amount
# http://127.0.0.1:8000/order/ORD-101/date
# Order matters for path variables.
@app.get("/orders/{order_id}/{key}")
def get_order_field(order_id: str, key: str):
    order = ORDERS.get(order_id)

    if not order:
        return f"No order found for the order id: {order_id}, Please provide a valid order id."
    
    try:
        value = order[key]
        return value
    except KeyError:
        return f"No valid field called {key} found for the order."

# Pre defined Values.
# If we have a path operation that receives a path parameter bu we want the possible valid path paramter to be predefined, then we can use standard Python Enums

# Create an Enum class.
class FuelType(str, Enum):
    petrol = "petrol"
    diesel = "diesel"
    ev = "ev"
    cng = "cng"

@app.get("/fuel/{type}")
def get_fuel_type(type: FuelType):
    return {"fuel_type" : type}

# https://www.amazon.in/s?k=iphone
# https://www.flipkart.com/search?q=iphone
# Query Parameters - Set of key-value pairs that we provide after ? 

# http://127.0.0.1:8000/sample/?value=1000
# When we declare other function parameters those are not part of path parameters, they are automatically considered as query parameters.
# http://127.0.0.1:8000/sample/?value1=100&value2=Masai
@app.get("/sample/")
def sample_api(value1: int, value2: str):
    return {
        "value1" : value1,
        "value2" : value2
    }

# POST / PUT / PATCH / DELETE.

def verify_token(token: str):
    # verify the token provided by the user.
    if len(token) < 5:
        # Invalid token
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    print("Token Valid.")

# DRY - Don't Repeat Yourself
# When a user clicks on "My Orders" on Amazon -> User can see all the orders they have placed till now. 
# get_all_orders has a dependency on verify_token function.
# So, instead of calling the dependency manually, we can use Dependency Injection.
@app.get("/myorders/{token}")
def get_all_orders(token: str = Depends(verify_token)):
    return "All order details"


# def cancel_order(order_id: str, token: str):

# HTTP Status Codes
# 200 - success
# 404 - Not Found
# 401 - Unauthorized
# 500 - Internal Server Error
# 502 - Bad Gateway

# If there's a Dependency with return values.
def pagination(page_number: int = 9, limit: int = 20):
    return {"page_number" : page_number, "limit" : limit}

# list_products function has a dependency on pagination function.

# http://127.0.0.1:8000/lists -> list_products(page: {"page_number" : page_number, "limit" : limit})
@app.get("/lists")
def list_products(page: dict = Depends(pagination)):
    return {"page_number" : page["page_number"], "limit" : page["limit"]}