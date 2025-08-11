from tools.dbms import DBMS
from repository import Repository

def test_dbms():
    try:
        # Create instances
        repo = Repository()
        dbms = DBMS(repo)
        
        # Test lookup by name
        print("Testing lookup by name...")
        result = dbms.lookup(name="test")
        print(f"Lookup result: {result}")
        
        # Test lookup by id
        print("\nTesting lookup by id...")
        result = dbms.lookup(id=1)
        print(f"Lookup result: {result}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_dbms()