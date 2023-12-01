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


if __name__ == '__main__':
    with open('./day-1/input.txt', 'r') as file:
        print(sum(calibration_value(line) for line in file))

