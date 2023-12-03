from pathlib import Path

path = Path("data")


def safe_index(grid, row, col):
    try:
        ret = grid[row][col]
    except IndexError:
        ret = ""
    return ret


grid = []
symbols = {}
for row, line in enumerate(open(path / "day3.txt")):
    grid.append(list(line.strip()))
    for col, c in enumerate(line.strip()):
        if not c.isdigit() and c != ".":
            symbols[(row, col)] = c

gear_ratio = []
for (row, col), s in symbols.items():
    numbers = []
    for row1, col1 in [
        (row, col + 1),
        (row, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
        (row + 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row - 1, col - 1),
    ]:
        number = []
        # Found adjacent digit
        if safe_index(grid, row1, col1).isdigit():
            # Scan left for more digits
            col2 = col1
            while safe_index(grid, row1, col2).isdigit():
                number.append(safe_index(grid, row1, col2))
                grid[row1][col2] = "#"
                col2 -= 1
            number.reverse()

            # Scan right for more digits
            col2 = col1 + 1
            while safe_index(grid, row1, col2).isdigit():
                number.append(safe_index(grid, row1, col2))
                grid[row1][col2] = "#"
                col2 += 1

        # Final number is concatenating both
        if len(number) > 0:
            numbers.append(int("".join(number)))

    if len(numbers) == 2:
        gear_ratio.append(numbers[0] * numbers[1])

print(sum(gear_ratio))
