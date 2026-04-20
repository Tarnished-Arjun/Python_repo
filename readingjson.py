import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Name:", data["user"]["name"])
print("Email:", data["user"]["contact"]["email"])
print("Phone:", data["user"]["contact"]["phone"])