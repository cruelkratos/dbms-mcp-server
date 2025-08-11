from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

# Use explicit names to avoid Windows environment variable conflicts
DATABASE = os.getenv('POSTGRES_DATABASE', 'postgres')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')

class IRepository(ABC):
    @abstractmethod
    def find_by_id(id):
        pass
    @abstractmethod
    def find_by_name(name):
        pass
    @abstractmethod
    def add_field(id,name,age,gender):
        pass

class Repository(IRepository):
    def __init__(self):
        self.conn = psycopg2.connect(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        self.cursor = self.conn.cursor()

    def find_by_id(self, id):
        try:
            self.cursor.execute("SELECT * FROM person WHERE id = %s", (id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error finding by id: {e}")
            return None

    def find_by_name(self, name):
        try:
            self.cursor.execute("SELECT * FROM person WHERE name = %s", (name,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error finding by name: {e}")
            return None

    def add_field(self, id, name, age, gender):
        try:
            self.cursor.execute(
                "INSERT INTO person (id, name, age, gender) VALUES (%s, %s, %s, %s)",
                (id, name, age, gender)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding field: {e}")
            self.conn.rollback()
            return False

    def __del__(self):
        # Close connection when object is destroyed
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'conn'):
            self.conn.close()