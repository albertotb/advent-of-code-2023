import re
from operator import itemgetter

from num2words import num2words

text2num = {num2words(num): num for num in range(1, 10)}

total = 0
for line in open("data/day1.txt"):
    text_matches = [
        (str(num), pos)
        for text, num in text2num.items()
        for pos in [m.start() for m in re.finditer(text, line)]
    ]

    num_matches = [(m.group(), m.start()) for m in re.finditer(r"\d", line)]

    all_matches = sorted(text_matches + num_matches, key=itemgetter(1))

    first, last = (
        all_matches[0][0],
        all_matches[-1][0] if len(all_matches) > 1 else all_matches[0][0],
    )
    num = int(first + last)

    total += num

print(total)
