# Command to install SQLAlchemy - pip3 install sqlalchemy
# SQLAlchemy 
# ORM -> Object Relational Model.

# SQLite
# To connect our FastAPI Server with SQL DB, we first need the DB path.
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./sqlite.db"

# Create an engine to connect with the DATABASE_URL.
engine = create_engine(DATABASE_URL, echo=True) # echo=True => Display the queries in the terminal
