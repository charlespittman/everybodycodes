#! /usr/bin/env python
# https://everybody.codes/event/2024/quests/6

from collections import defaultdict


def get_input(part, use_example=False):
    examples = {
        1: ["RR:A,B,C", "A:D,E", "B:F,@", "C:G,H", "D:@", "E:@", "F:@", "G:@", "H:@"],
        2: ["RR:A,B,C", "A:D,E", "B:F,@", "C:G,H", "D:@", "E:@", "F:@", "G:@", "H:@"],
        3: ["RR:A,B,C", "A:D,E", "B:F,@", "C:G,H", "D:@", "E:@", "F:@", "G:@", "H:@"],
    }
    data = examples[part]
    if not use_example:
        with open(f"p{part}.txt") as f:
            data = f.readlines()
    return [d.strip() for d in data]


def parse_data(data: list[str]) -> dict[str, list[str]]:
    result = defaultdict(list)
    for d in data:
        start, edges = d.split(":")
        edges = edges.split(",")
        for edge in edges:
            result[start].append(edge)
    return result


def get_paths(root):
    if root in ["ANT", "BUG"]:
        return []
    ret = []
    if root == "@":
        return [["@"]]
    for branch in branches[root]:
        for path in get_paths(branch):
            ret.append([root] + path)
    return ret


def most_powerful_path(paths, shorten=False):
    most_powerful = []
    by_length = defaultdict(list)
    for path in paths:
        by_length[len(path)].append(path)
    for k, v in by_length.items():
        if len(v) == 1:
            most_powerful = v[0]
            break
    if shorten:
        return "".join([c[0] for c in most_powerful])
    return "".join(most_powerful)


if __name__ == "__main__":
    use_sample_data = False
    results = {}
    for part in [1, 2, 3]:
        print(f"Part {part}")

        data = get_input(part, use_example=use_sample_data)
        branches = parse_data(data)
        paths = get_paths("RR")

        if part == 1:
            results[1] = most_powerful_path(paths)
        if part in [2, 3]:
            results[part] = most_powerful_path(paths, shorten=True)

        print(results[part])
