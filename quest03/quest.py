#! /usr/bin/env python
# https://everybody.codes/event/2024/quests/3


def get_input(part, use_example=False):
    examples = {
        1: [
            "..........\n",
            "..###.##..\n",
            "...####...\n",
            "..######..\n",
            "..######..\n",
            "...####...\n",
            "..........\n",
        ],
        2: [
            "..........\n",
            "..###.##..\n",
            "...####...\n",
            "..######..\n",
            "..######..\n",
            "...####...\n",
            "..........\n",
        ],
        3: [
            "..........\n",
            "..###.##..\n",
            "...####...\n",
            "..######..\n",
            "..######..\n",
            "...####...\n",
            "..........\n",
        ],
    }
    data = examples[part]
    if not use_example:
        with open(f"p{part}.txt") as f:
            data = f.readlines()
    return [list(d.strip()) for d in data]


def parse_data(data):
    pass


def print_grid(grid: list[list]) -> None:
    print("-" * 10)
    for row in grid:
        for col in row:
            print(col, end="")
        print()


def first_pass(grid: list[list]) -> list[list]:
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == "#":
                grid[y][x] = 1
    return grid


def check_direction(grid: list[list], x: int, y: int, direction: str) -> bool:
    safe = False
    try:
        cur = grid[y][x]
    except IndexError:
        return True
    if not isinstance(cur, int):
        return False
    directions = ["north", "south", "east", "west"]
    # print("x={}, y={}, grid[y][x]={}, direction={}".format(x, y, cur, direction))
    if direction == "west":
        if x > 0:
            check = grid[y][x - 1]
        if x == 0:
            safe = True
        elif check == cur:
            safe = True
        else:
            safe = False
    elif direction == "east":
        if x < len(grid[0]) - 1:
            check = grid[y][x + 1]
        if x == len(grid[0]) - 1:
            safe = True
        elif check == cur:
            safe = True
        else:
            safe = False
    elif direction == "north":
        if y > 0:
            check = grid[y - 1][x]
        if y == 0:
            safe = True
        elif check == cur:
            safe = True
        else:
            safe = False
    elif direction == "south":
        if y < len(grid) - 1:
            check = grid[y + 1][x]
        if y == len(grid) - 1:
            safe = True
        elif check == cur:
            safe = True
        else:
            safe = False
    else:
        raise ValueError("Direction must be one of: {}".format(", ".join(directions)))

    return safe


def check_surroundings(grid: list[list], x: int, y: int) -> bool:
    safe = False
    if part == 3:
        orthagonal = False
    else:
        orthagonal = True
    check_orthagonal = all(
        [
            check_direction(grid, x, y, "north"),  # North
            check_direction(grid, x, y, "south"),  # South
            check_direction(grid, x, y, "west"),  # East
            check_direction(grid, x, y, "east"),  # West
        ]
    )

    if orthagonal:
        safe = check_orthagonal
    else:
        check_diagonal = all(
            [
                check_direction(grid, x, y - 1, "west"),  # Northwest
                check_direction(grid, x, y - 1, "east"),  # Northeast
                check_direction(grid, x, y + 1, "west"),  # Southwest
                check_direction(grid, x, y + 1, "east"),  # Southeast
            ]
        )
        safe = check_orthagonal and check_diagonal
    return safe


def mine(grid: list[list]) -> list:
    to_update = []
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if check_surroundings(grid, x, y):
                to_update.append((x, y))
    for coord in to_update:
        x, y = coord
        grid[y][x] += 1
    return to_update


def count_blocks(grid: list[list]) -> int:
    total = 0
    for row in grid:
        for col in row:
            try:
                col = int(col)
            except ValueError:
                col = 0
            total += col
    return total


def run(grid):
    print_grid(grid)
    grid = first_pass(grid)
    print_grid(grid)
    while mine(grid):
        print_grid(grid)
    return count_blocks(grid)


if __name__ == "__main__":
    results = {}
    for part in [1, 2, 3]:
        grid = get_input(part, use_example=False)
        print(f"Part {part}")

        # It says to treat the grid as having infinite blank area around the map, so we're going to insert a couple blanks around the border (I stopped checking boundaries after confirming parts 1 and 2 work).
        if part == 3:
            grid.insert(0, list("." * len(grid[0])))
            grid.append(list("." * len(grid[0])))
            for row in grid:
                row.insert(0, ".")
                row.append(".")
        results[part] = run(grid)
        print(f"Blocks mined: {results[part]}")

    assert results[1] == 118
    assert results[2] == 2694
    assert results[3] == 9947
