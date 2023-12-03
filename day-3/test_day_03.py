from day_03 import parse_line


def test_parse_line():
    input = "467..114.."
    expected_output = {"parts": {467: {0, 1, 2}, 114: {5, 6, 7}}, "symbols": []}

    output = parse_line(input)

    assert output == expected_output


def test_parse_line_symbols():
    input = "...*......"
    expected_output = {"parts": {}, "symbols": [{2, 3, 4}]}

    output = parse_line(input)

    assert output == expected_output
