#! /usr/bin/env python
# https://everybody.codes/event/2024/quests/4


def get_input(part, use_example=False):
    examples = {
        1: ["3", "4", "7", "8"],
        2: ["3", "4", "7", "8"],
        3: ["2", "4", "5", "6", "8"],
    }
    data = examples[part]
    if not use_example:
        with open(f"p{part}.txt") as f:
            data = f.readlines()
    return [d.strip() for d in data]


def parse_data(data):
    return [int(d) for d in data]


def hammer_to_depth(nails: list[int], depth: int) -> int:
    return sum([abs(nail - depth) for nail in nails])


def part1(nails):
    min_height = min(nails)
    print(f"min:{min_height}")
    strikes = hammer_to_depth(nails, min_height)
    return strikes


def part3(nails):
    min_strikes = 10**10
    for nail in nails:
        strikes = hammer_to_depth(nails, nail)
        if strikes < min_strikes:
            min_strikes = strikes
    return min_strikes


if __name__ == "__main__":
    use_sample_data = False
    results = {}
    for part in [1, 2, 3]:
        print(f"Part {part}")

        data = get_input(part, use_example=use_sample_data)
        nails = parse_data(data)
        print(f"nail heights: {nails}")

        if part in [1, 2]:
            results[part] = part1(nails)
        else:
            results[part] = part3(nails)

        print(f"Hammer strikes: {results[part]}")
    if use_sample_data:
        assert results[1] == 10
        assert results[3] == 8
    else:
        assert results[1] == 83
        assert results[2] == 960281
        assert results[3] == 122794083
