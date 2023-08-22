import requests


def main():
    response = requests.get("http://www.google.com/random-address/")
    # print("Status Code: ", response.status_code)
    # print('Content-type: ', response.headers.get('Content-Type'))
    print(response.text)
    print(response.url)


if __name__ == "__main__":
    main()


