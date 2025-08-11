from dotenv import load_dotenv
import os
import psycopg2

# Ensure we're loading from the correct .env file
print(f"Current working directory: {os.getcwd()}")
load_dotenv()

def test_db_connection():
    # Print connection details for debugging
    print("\nAttempting connection with:")
    print(f"Database: {os.getenv('DATABASE')}")
    print(f"Username: {os.getenv('USERNAME')}")
    print(f"Host: {os.getenv('HOST')}")
    print(f"Port: {os.getenv('PORT')}")
    
    try:
        conn = psycopg2.connect(
            database=os.getenv('DATABASE'),
            user="postgres",  # Explicitly use postgres user
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )
        print("Successfully connected to database!")
        conn.close()
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_db_connection()