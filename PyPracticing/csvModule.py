import csv

with open("csvtest.csv") as file:
    contents = csv.reader(file)
    for row in contents:
        print(row)
