# Symless / Synergy Pro key generator for version 1 By NightmareGaurav
import base64

name = input("What is your Name? ")
userLimit = input("How many user are going to use synergy? ")
email = input("What is your email address? ")
company = input("What is your business or company name? ")

key= "{v1;pro;" + name + ";" + userLimit + ";" + email + ";" + company + ";0;0}";
actualKey = base64.b16encode(key.encode()).decode()
print("Your Key: " + actualKey)
