import requests

def test_mcp_endpoint():
    try:
        response = requests.post(
            "http://localhost:5000/lookup_name",
            json={"args": ["test"]}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_mcp_endpoint()