import csv

def read_from_csv():
    file_name = "Name_age.csv"
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
read_from_csv()
