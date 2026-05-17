import random
import csv

# === PART 1: Variables ===
name = "Lisa"
job = "QA Engineer"
print("My name is", name)
print("My job is", job)

# === PART 2: Login Test ===
username = "standard_user"
password = "secret_sauce"
if username == "standard_user" and password == "secret_sauce":
    print("Login PASSED ")
else:
    print("Login FAILED ")

# === PART 3: Test Data Generator ===
first_names = ["John", "Sarah", "Mike", "Emma"]
last_names = ["Smith", "Jones", "Brown", "Wilson"]

with open("test_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email"])
    for i in range(5):
        first = random.choice(first_names)
        last = random.choice(last_names)
        email = first.lower() + "@test.com"
        writer.writerow([first + " " + last, email])

print("test_data.csv created!")