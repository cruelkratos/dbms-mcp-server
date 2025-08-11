from dotenv import load_dotenv
from server import mcp
from .dbms import DBMS
from repository import Repository , IRepository
import os

load_dotenv()

print("Database Connection Settings:")
print(f"DATABASE: {os.getenv('POSTGRES_DATABASE')}")
print(f"USERNAME: {os.getenv('POSTGRES_USER')}")
print(f"HOST: {os.getenv('POSTGRES_HOST')}")
print(f"PORT: {os.getenv('POSTGRES_PORT')}")

# Initialize database connection
dbms = DBMS(Repository())

@mcp.tool()
def lookup_name(name):
    """Look up a person by name"""
    result = dbms.lookup(name=name)
    return result or []  # Return empty list if None

@mcp.tool()
def lookup_id(id):
    """Look up a person by ID"""
    result = dbms.lookup(id=id)
    return result or None

@mcp.tool()
def add(id, name, age, gender):
    """Add a new person"""
    return dbms.add(id, name, age, gender)
