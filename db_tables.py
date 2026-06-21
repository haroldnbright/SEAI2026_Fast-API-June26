# Create tables.
from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

# users table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String(50), nullable=False, unique=True),
    Column("address", String(100), nullable=False)
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("content", String(100), nullable=False),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
)

def create_all_tables():
    metadata.create_all(engine)
