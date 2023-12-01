from day_1 import calibration_value, calibration_value_2


def test_calibration_value():
    assert calibration_value('1abc2') == 12
    assert calibration_value('pqr3stu8vwx') == 38
    assert calibration_value('treb7uchet') == 77
    assert calibration_value('hkxqfrqmsixfplbkpkdfzzszjxmdjtdkjlprrvr3gghlrqckqtbng') == 33


def test_calibration_value_part_2():
    assert calibration_value_2('two1nine') == 29