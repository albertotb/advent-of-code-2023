from collections import Counter
from pathlib import Path

path = Path("data")

total = 0
cards = []
for row, line in enumerate(open(path / "day4.txt")):
    game, numbers = line.split(":")
    winning, numbers = numbers.split("|")

    matches = [n in set(winning.split()) for n in numbers.split()]
    points = 2 ** (sum(matches) - 1) if any(matches) else 0
    total += points

    # For part 2 we save all the copies
    cards.append(list(range(row + 1, row + 1 + sum(matches))))

print(total)


# Instead of saving the card numbers you can already build the counter
# as you go, avoiding the call to Counter later
def process_cards(card, cardlist):
    total = []
    for n in card:
        total.extend([n] + process_cards(cardlist[n], cardlist))
    return total


total = []
for card in cards:
    total.extend(process_cards(card, cards))

print(sum(Counter(total).values()) + len(cards))
