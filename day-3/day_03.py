def is_symbol(char: str):
    return char != "." and char.isdigit() == False


def parse_line(value: str):
    res = {"parts": {}, "symbols": []}
    current_part = ""

    for index, char in enumerate(value):
        if char.isdigit():
            current_part += char
            if index == len(value) - 1:
                res["parts"][int(current_part)] = set(
                    range(index - len(current_part), index)
                )

        elif len(current_part) != 0:
            res["parts"][int(current_part)] = set(
                range(index - len(current_part), index)
            )
            current_part = ""

        if is_symbol(char):
            res["symbols"].append(
                set(range(max(index - 1, 0), min(index + 2, len(value) - 1)))
            )

    return res


def main():
    with open("./day-3/input.txt", "r") as file:
        lines = [parse_line(line) for line in file]

    total = 0

    for index, line in enumerate(lines):
        adjacent_symbols = set().union(*line["symbols"])

        if index > 0:
            for a_set in lines[index - 1]["symbols"]:
                adjacent_symbols.update(a_set)

        if index < len(lines) - 1:
            for a_set in lines[index + 1]["symbols"]:
                adjacent_symbols.update(a_set)

        for n, position in line["parts"].items():
            common = position & adjacent_symbols

            if len(common) > 0:
                total += n

    print(total)


if __name__ == "__main__":
    main()
