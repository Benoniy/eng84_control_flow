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
             2: {"name": "GoldFinger", "bill": "£1,=000,000"},
             3: {"name": "Jim", "bill": "£20"}
             }

for key, value in food_bill.items():
    print(key, value)

# Exercise - print the names and bill amounts for each individual
for value in food_bill.values():
    print(f"Name: {value['name']}\nBill: {value['bill']}\n")
