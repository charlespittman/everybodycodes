#! /usr/bin/env python
# https://everybody.codes/event/2024/quests/2


def get_input(part, use_example=False):
    examples = {
        1: [
            "WORDS:THE,OWE,MES,ROD,HER\n",
            "\n",
            "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE, THE FLAME SHIELDED THE HEART OF THE KINGS, POWE PO WER P OWE R, THERE IS THE END",
        ],
        2: [
            "WORDS:THE,OWE,MES,ROD,HER\n",
            "\n",
            "AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE\n",
            "THE FLAME SHIELDED THE HEART OF THE KINGS\n",
            "POWE PO WER P OWE R\n",
            "THERE IS THE END",
        ],
        3: [
            "WORDS:THE,OWE,MES,ROD,RODEO",
            "\n",
            "HELWORLT\n",
            "ENIGWDXL\n",
            "TRODEOAL",
        ],
    }
    data = examples[part]
    if not use_example:
        with open(f"p{part}.txt") as f:
            data = f.readlines()
    return data


def parse_data(data, part):
    runes = [rune.strip() for rune in data[0].split(":")[1].split(",")]
    if part == 1:
        engravings = data[-1].split(",")
    if part == 2:
        engravings = [engraving.strip() for engraving in data[2:]]
        reversed_runes = []
        for rune in runes:
            reversed_runes.append("".join(reversed(rune)))
        runes += reversed_runes
    if part == 3:
        ltr = [engraving.strip() for engraving in data[2:]]
        rtl = ["".join(reversed(e)) for e in ltr]
        ttb = ["".join(x) for x in list(zip(*ltr))]
        btt = ["".join(reversed(e)) for e in ttb]
        print(ltr)
        print(rtl)
        print(ttb)
        print(btt)
        engravings = ltr + rtl + ttb + btt
    return runes, engravings


def count_runes(runes, engravings):
    rune_count = 0
    for engraving in engravings:
        count = 0
        for rune in runes:
            ec = engraving.count(rune)
            count += ec
            rune_count += ec
        # print(engraving, count)
    return rune_count


def count_rune_chars(runes, engravings):
    char_count = 0

    for engraving in engravings:
        runes_matched = []
        indexes = []
        for rune in runes:
            if rune in engraving:
                runes_matched.append(rune)
        for index, char in enumerate(engraving):
            for rune in runes_matched:
                # print(rune, engraving[index : index + len(rune)])
                if engraving[index : index + len(rune)] == rune:
                    indexes.append([index, index + len(rune)])
        indexes = merge_intervals(indexes)
        for r in indexes:
            char_count += r[1] - r[0]
    return char_count


def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals based on the starting points
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Otherwise, add the current interval to the merged list
            merged_intervals.append(current)

    return merged_intervals


if __name__ == "__main__":
    for part in [1, 2, 3]:
        data = get_input(part, True)
        runes, engravings = parse_data(data, part)
        # print(runes)
        # print(engravings)
        print(f"part {part}:", count_runes(runes, engravings))
        print(f"part {part}:", count_rune_chars(runes, engravings))
