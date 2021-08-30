import io
import random
import time

import requests
from bs4 import BeautifulSoup
from bs4 import element

# mba today prefix
mba_today_prefix = "https://www.mba.today"
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


def get_addresses():

    # work with schools
    for school in schools_list:

        if school.url == "https://www.mba.today/school/":
            continue
        else:
            page_text = get_payload(school.url)
            soup = get_soup_from_text(page_text)

            # pause somewhat randomly
            timeout = random.uniform(0.5, 1.5)
            time.sleep(timeout)

            schoolinfo = soup.find_all(
                attrs={"itemtype": "http://schema.org/CollegeOrUniversity"}
            )
            output = ""
            for child in schoolinfo[0].descendants:
                if isinstance(child, element.NavigableString):
                    output += str(child.string) + "\n"

            # show output
            school_text = (
                "================================================================================"
                + "\n"
            )
            school_text += parse_address(output)
            school_text += (
                "================================================================================"
                + "\n"
            )
            # status
            print(f"processed: {school.name}")

            # write output string to file
            write_schools_to_file("aacsb_addresses.txt", school_text)


def get_soup_from_text(page_text):
    return BeautifulSoup(page_text, "html.parser")


def get_payload(url):
    return requests.get(url).text


def make_schools():
    # create mba today pages
    page_text = get_payload(aacsb_schools_url)
    soup = get_soup_from_text(page_text)

    usa_canada_schools = soup.select(f"#{united_states_canada_id}")
    links = usa_canada_schools[0].find_all("a")

    # create urls from school list
    for link in links:
        schools_list.append(School(link.string, f"{mba_today_prefix}{link['href']}"))


def parse_address(address_text):
    parts = address_text.split("\n")
    essential_parts = []
    output = ""
    for part in parts:
        if len(part) > 1 and not part.startswith(","):
            essential_parts.append(part)

    for part in essential_parts:
        output += f"{part}\n"

    return output


def print_schools():
    # print school list to screen
    print(f"how many schools: {len(schools_list)}")

    for school in schools_list:
        print(school)


def write_schools_to_file(filename, school_text):
    # write schools to file
    with io.open(filename, "a") as f:
        f.write(school_text)


def write_schools_to_textfile():
    # write schools list to file
    output = ""
    for school in schools_list:
        output += str(school) + "\n"

    # write schools to file
    f = open("schools.txt", "w")
    f.write(output)
    f.close()


def main():
    # screen scraping to get AACSB schools
    print("SCRAPING")

    # create
    make_schools()

    get_addresses()


if __name__ == "__main__":
    main()
