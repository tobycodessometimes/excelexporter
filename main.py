import json, csv, time

def start():
        print("""Python to excel exporter
------------
Options:
1. Info to excel  2. Coming soon
------------""")
        answer1 = input("Please input a value: ")
        if answer1 == ("1"):
             print("Success, printing..")
        else: 
            print("Please input a number listed above.")
            start()

start()


def main():
    data = {}
    data["First Name"] = input("Enter first name here: ")
    data["Last Name"] = input("Enter last name here: ")
    data["Email"] = input("Enter email here: ")
    data["Phone Number"] = input("Enter phone number here: ")
    data["Address Line 1"] = input("Enter address line 1 here: ")
    data["Address Line 2"] = input("Enter address line 2 here: ")
    data["City"] = input("Enter a city here: ")
    data["Postcode"] = input("Enter a postcode here: ")
    data["Country"] = input("Enter a country here: ")

    print("Export successful. (data.csv)")

    with open("data.csv", mode="w", newline="") as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_array = []
        data_titles = []
        for i in data:
            data_titles.append(i)
        data_writer.writerow(data_titles)
        for i in data:
            data_array.append(data[i])
        data_writer.writerow(data_array)

main()
print("Closing in 3 seconds.")
time.sleep(10000)

    