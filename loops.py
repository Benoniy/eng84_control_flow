# What is a for loop
# FOR - created with

shopping_list = ['bread', 'eggs', 'milk', 'orange']

# Loop through a list
for item in shopping_list:
    print(item)

# Loop through letters in a word
for letter in "word":
    print(letter)

# Breaks
for item in shopping_list:
    print(item)
    if item == "milk":
        break  # stops the loop at milk

# Loop through a dictionary (nested or otherwise)
food_bill = {1: {"name": "James", "bill": "£10"},
             2: {"name": "GoldFinger", "bill": "£1,000,000"},
             3: {"name": "Jim", "bill": "£20"}
             }

for key, value in food_bill.items():
    print(key, value)

# Exercise - print the names and bill amounts for each individual
for value in food_bill.values():
    print(f"Name: {value['name']}\nBill: {value['bill']}\n")

# Nested iteration
for value in food_bill.values():
    for item in value.values():
        print(item)


# While loops
num = 0
while num < 10:
    print(num)
    num += 1

# Can be combined with an if statement
num = 0
while num < 10:
    print(num)
    if num == 4:
        break
    num += 1

# Can be used to ensure correct user input

user_age = input("Please enter your age: ")
while not user_age.isdigit():
    user_age = input("Please enter your age using digits: ")
print(f"You are {user_age} years old")
