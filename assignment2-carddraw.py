# Description: This script draws 5 cards from a shuffled deck
# and checks for pairs, triples, straights, and all of the same suit.
# Author: Filipe Carvalho

# Import the requests library
import requests
import json

# Shuffled deck
url1 = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url1)
data = response.json()
deck_id = data["deck_id"]
# print(deck_id)

# Draw 5 cards
url2 = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response2 = requests.get(url2)
data2 = response2.json()

# Define the values and suits of the drawn cards
cards = data2["cards"]
values = [card['value'] for card in cards]
suits = [card['suit'] for card in cards]

# Print the drawn cards
for card in cards:
    print(f"Card: {card['value']} of {card['suit']}")

# Check for pairs, triples, and all of the same suit
value_counts = {value: values.count(value) for value in values}
suit_counts = {suit: suits.count(suit) for suit in suits}

# Check for pairs and triples
pairs = [value for value, count in value_counts.items() if count == 2]
triples = [value for value, count in value_counts.items() if count == 3]

# Check for straight
value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
value_indices = sorted([value_order.index(value) for value in values])
straight = all(value_indices[i] + 1 == value_indices[i + 1] for i in range(len(value_indices) - 1))

# Check for all of the same suit
all_same_suit = len(set(suits)) == 1

# Congratulate the user
if pairs:
    print(f"Congratulations! You have a pair of {', '.join(pairs)}.")
if triples:
    print(f"Congratulations! You have a triple of {', '.join(triples)}.")
if straight:
    print("Congratulations! You have a straight.")
if all_same_suit:
    print("Congratulations! All cards are of the same suit.")
if not (pairs or triples or straight or all_same_suit):
    print("No special combinations found.")
