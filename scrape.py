import time
import random

import requests
from bs4 import BeautifulSoup

# mba today prefix
mba_today_prefix = "https://www.mba.today/"
aacsb_schools_url = "https://www.mba.today/guide/aacsb-accredited-business-schools"
united_states_canada_id = "usa-canada"

# links from mba today
school_links = []

# school objects
schools_list = []


class SchoolAddress:
    def __init__(self, street, city, state):
        pass


class School:
    address = None

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self) -> str:
        return f"name: {self.name}\n" f"link: {self.url}\n"


def main():
    # screen scraping to get AACSB schools
    print("SCRAPING")

    # create
    make_schools()
    get_addresses()

    # show schools
    # print(f"how many schools: {len(schools_list)}")
    # for school in schools_list:
    #     print(school)


def make_schools():
    # create mba today pages
    page_text = get_payload(aacsb_schools_url)
    soup = get_soup_from_text(page_text)

    usa_canada_schools = soup.select(f"#{united_states_canada_id}")
    links = usa_canada_schools[0].find_all("a")

    # create urls from school list
    for link in links:
        schools_list.append(School(link.string, f"{mba_today_prefix}{link['href']}"))


def get_addresses():

    # work with schools
    for school in schools_list:
        print(school)
        page_text = get_payload(school.url)
        soup = get_soup_from_text(page_text)

        # pause somewhat randomly
        timeout = random.uniform(0.5, 2.0)
        time.sleep(timeout)

        address = soup.find_all("address")
        print(address)
        # print(f"how many addresses {len(address)}")


def parse_address(address_text):
    pass


def get_soup_from_text(page_text):
    return BeautifulSoup(page_text, "html.parser")


def get_payload(url):
    return requests.get(url).text


if __name__ == "__main__":
    main()
