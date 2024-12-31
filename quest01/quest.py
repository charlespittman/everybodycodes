#! /usr/bin/env python
# https://everybody.codes/event/2024/quests/1


def get_input(part, use_example=False):
    examples = {
        1: "ABBAC",
        2: "AxBCDDCAxD",
        3: "xBxAAABCDxCC",
    }
    example = examples[part]
    if not use_example:
        with open(f"p{part}.txt") as f:
            example = f.read()
    return example


def group_monsters(monsters, size):
    return [monsters[i : i + size] for i in range(0, len(monsters), size)]


def count_monsters(monsters):
    monster_count = {}
    for m in ["A", "B", "C", "D"]:
        monster_count[m] = monsters.count(m)
    return monster_count


def count_potions(monsters, group_size=1):
    potions_per_monster = {
        "A": 0,
        "B": 1,
        "C": 3,
        "D": 5,
    }

    potions_needed = 0
    groups = group_monsters(monsters, group_size)

    for group in groups:
        monsters = count_monsters(group)
        for monster in monsters:
            potions_needed += monsters[monster] * potions_per_monster[monster]
        if group_size == 2:
            if "x" not in group:
                potions_needed += 2
        if group_size == 3:
            blanks = group.count("x")
            if blanks == 0:
                potions_needed += 6
            if blanks == 1:
                potions_needed += 2

    return potions_needed


if __name__ == "__main__":
    for part in [1, 2, 3]:
        monsters = get_input(part, use_example=True)
        print(f"part {part}:", count_potions(monsters, group_size=part))
