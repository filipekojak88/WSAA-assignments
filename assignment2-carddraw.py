import requests
import json

url1 = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url1)
data = response.json()
deck_id = data["deck_id"]
# print(deck_id)

url2 = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response2 = requests.get(url2)
data2 = response2.json()
# print(data2)
cards = data2["cards"]
for card in cards:
    print(f"Card: {card['value']} of {card['suit']}")
