import requests
from bs4 import BeautifulSoup

def main():
    print("SCRAPING")

    school_url = "https://www.mba.today/school/alabama-a-and-m-university"
    print(get_payload(school_url))


def get_payload(url):
    return requests.get(url).text
    

if __name__ == "__main__":
    main()

