# import required modules
import random

from game_data import data
from art import logo, vs

# variable to keep track if loser lost/ game over
game_over = False

# list of vowels to have grammatically correct output to user
vowels = ["A", "E", "I", "O", "U"]

# variable to keep track of score, start by setting to 0
current_score = 0


# function to output information for each round
def game_round(item_a, item_b):
    """Takes in two dictionaries and formats their data and outputs it to the user"""
    # check if the description starts with a vowel and output proper information to user
    if item_a['description'][0] in vowels:
        print(f"Compare A: {item_a['name']}, an {item_a['description']}, from {item_a['country']}")
    else:
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")

    print(vs)

    # check if the description starts with a vowel and output proper information to user
    if item_b['description'][0] in vowels:
        print(f"Against B: {item_b['name']}, an {item_b['description']}, from {item_b['country']}")
    else:
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")


# function to determine which item has the higher follower count
def higher(item_a, item_b):
    """Takes in two dictionaries and returns a letter corresponding to which one has the higher follower count"""
    item_a_followers = item_a['follower_count']
    item_b_followers = item_b['follower_count']

    if item_a_followers >= item_b_followers:
        return "a"
    else:
        return "b"


# variable to track if it's the first round
first_round = True

print(logo)

# keep looping until user guesses wrong
while not game_over:
    if not first_round:
        print(f"\nYou're right! Current score: {current_score}\n")

    # randomly choose 2 options from data for first round only
    if first_round:
        option_A = random.choice(data)
        option_B = random.choice(data)

    # change option B if computer has randomly generated the same item for both options
    while option_A == option_B:
        option_B = random.choice(data)

    # call function for game round
    game_round(item_a=option_A, item_b=option_B)

    # call function to determine which option is correct answer
    correct_answer = higher(item_a=option_A, item_b=option_B)

    # user input for their guess of more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # if user guessed correct, increase score and set option A of the next round as option B from this round
    # and choose a new item for option B
    if correct_answer == guess:
        current_score += 1
        # switch first_round to false to output score to user
        first_round = False
        option_A = option_B
        option_B = random.choice(data)
    else:
        # if user guessed wrong, let them know and output final score then exit game
        print(f"\nSorry that's wrong. Final score: {current_score}")
        break
