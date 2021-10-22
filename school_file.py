SEPARATOR = "================================================================================"

count = 0
word = "Fax"

def read_school_file(filename):
    f = open(filename, "r")
    for line in f:
        parser(line)

def parser(line: str):

    global count
    
    if line.strip() == "Fax":
        count += 1
        print(f"{count}")

def main():
    # screen scraping to get AACSB schools
    print("PARSING")

    if word == "Fax":
        print("DUDE")    

    read_school_file("aacsb_addresses.txt")

    # init db

    # create
    # make_schools()

    # get_addresses()


if __name__ == "__main__":
    main()