def calibration_value(value: str) -> int:
    start_idx = 0
    end_idx = len(value) - 1

    first_digit, last_digit = None, None

    while first_digit is None or last_digit is None:
        start = value[start_idx]
        end = value[end_idx]

        if start.isdigit() and first_digit is None:
            first_digit = start

        if end.isdigit() and last_digit is None:
            last_digit = end

        start_idx += 1
        end_idx -= 1

    if first_digit is None or last_digit is None:
        raise ValueError('No digits found in value')

    return int(first_digit + last_digit)


numbers_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_number(value, index):
    current = value[index]

    if current.isdigit():
        return current

    for key in numbers_map.keys():
        end_index = index + len(key)

        if value[index:end_index] == key:
            return numbers_map[key]

    return None


def calibration_value_2(value: str) -> int:
    index = 0
    first_digit, last_digit = None, None

    while index < len(value):
        maybe_number = get_number(value, index)

        if maybe_number is not None:
            last_digit = maybe_number
            if first_digit is None:
                first_digit = maybe_number

        index += 1


    if first_digit is None or last_digit is None:
        raise ValueError('No digits found in value')

    return int(first_digit + last_digit)


if __name__ == '__main__':
    with open('./day-1/input.txt', 'r') as file:
        print(sum(calibration_value_2(line) for line in file))

