# Conditional statements are used to control the flow of the program
# If statements are used for this
# age = 16

# if age > 15:
#     print("You are older than 15")
# elif age < 15:
#     print("You are younger than 15")
# else:
#     print("You are 15")


# Exercise - Sell tickets according to age vs age rating of a movie
# The user tells their age
# We tell them if they can see the movie
# ratings = ('U', 'PG', '12a', '15', '18')

# Contains a dictionary of the available movies and their ratings
movies = {"superman": "15",
          "boss baby": "U",
          "deadpool": "18",
          }

# Gets the age of the user for later checks
age = int(input("Please enter your age: "))

# Prints a list of movie for the user to see
print("\nMovie List:")
for k, _ in movies.items():
    print(k)

# Selection of movie they want to see
selection = input("\nplease enter the name of the movie you want to watch: ").lower()

# Logic for if you can watch the move
if age >= 18 and movies[selection] == "18":
    print("congratulations, you can watch the movie")
elif age >= 15 and movies[selection] == "15":
    print("congratulations, you can watch the movie")
elif age >= 12 and movies[selection] == "12a":
    print("congratulations, you can watch the movie")
elif movies[selection] == "U":
    print("congratulations, you can watch the movie")
else:
    print("Sorry, unfortunately you are too young to watch that movie :(")


