
import csv

with open("logs.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        ip = row[0]
        status = row[4]

        print(ip, status)

        if status == "401":
            print("Failed Login Attempt")
