import requests

BASE_URL = "http://127.0.0.1:8080"

def test_hello():
    response = requests.get(f"{BASE_URL}/hello")
    print("\n/hello:", response.json())

def test_user(username):
    response = requests.get(f"{BASE_URL}/user/{username}")
    print(f"\n/user/{username}:", response.json())

def test_search(query):
    response = requests.get(f"{BASE_URL}/search", params={"q": query})
    print(f"\n/search?q={query}:", response.json())

def main():
    test_hello()
    test_user("Valentine")
    test_search("Flask")

if __name__ == '__main__':
    main()
