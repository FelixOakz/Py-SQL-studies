#DICTIONARIES
# A simple dictionary
person = {"age": "21", "gender": "female"}
# Accessing a value
print("The person's age is " + person["age"])
# Adding a new key-value pair
person["height"] = 170
# Looping through all key-value pairs ages = { "Stacy": 20, "Michelle": 21}
for name, age in ages.items():
	print(name + " is " + str(age))
# Looping through all keys ages = { "Stacy": 20, "Michelle": 21}
for name in ages.keys():
	print(name + " is a name")
# Looping through all the values ages = { "Stacy": 20, "Michelle": 21}
for age in ages.values():
	print(str(num) + " is my age")
