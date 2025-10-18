import requests

def main():
    url = "http://127.0.0.1:8080/hello"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == '__main__':
    main()
