# Description: This script draws 5 cards from a shuffled deck
# and checks for pairs, triples, straights, and all of the same suit.
# Author: Filipe Carvalho

# 1 - Import the necessary libraries
import requests
import json
from collections import Counter

# 2 - Shuffled deck 
url1 = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url1)
data = response.json()

# 3 - Get the deck ID
deck_id = data["deck_id"]

# 4 - Draw 5 cards
url2 = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response2 = requests.get(url2)
data2 = response2.json()


# 5 - Extract the drawn cards
cards = data2["cards"]

# 6 - Create empty lists to store the values and suits
values= []
suits= []


# 7 - Print the drawn cards in a readable format:

# Counter for the card number
i=1
# Loop through the drawn cards
for card in cards:
    value = card["value"]
    suit = card["suit"]
    print(f"Card {i}: {value} of {suit}")

    # Append the values and suits to their respective lists
    values.append(value)
    suits.append(suit)
    # Increment the counter
    i=i+1

# 8 - Count the occurrences of each value and suit
value_counts = Counter(values)
suit_counts = Counter(suits)

# 9 - Check for pairs and triples
pairs = [value for value, count in value_counts.items() if count == 2]
triples = [value for value, count in value_counts.items() if count == 3]


# 10 - Check for straight:

# 10.1 - Define the order of card values
value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']

# 10.2 - Convert values to their indices in the value_order list
value_indices = sorted([value_order.index(value) for value in values])

# 10.3 - Check if the values are consecutive:
# Assume it's a straight 
straight = True  
# Loop through the indices and compare each value to the next one
for i in range(len(value_indices) - 1):
    current_value = value_indices[i]
    next_value = value_indices[i + 1]
    # Check if the next value is exactly 1 more than the current
    if current_value + 1 != next_value:
        # If not, it's not a straight
        straight = False  
        break 
# 10.4 - Check for Ace-low straight: ['ACE', '2', '3', '4', '5']
if not straight and set(values) == {'ACE', '2', '3', '4', '5'} and len(values) == 5:
    straight = True

# 11 - Check for all of the same suit
all_same_suit = len(set(suits)) == 1

# 12 - Print the results and congratulate the user
if pairs:
    print(f"Congratulations! You have a pair of {', '.join(pairs)}.")
if triples:
    print(f"Congratulations! You have a triple of {', '.join(triples)}.")
if straight:
    print("Congratulations! You have a straight.")
if all_same_suit:
    print("Congratulations! All cards are of the same suit.")
if not (pairs or triples or straight or all_same_suit):
    print("No special combinations found. Try again")
