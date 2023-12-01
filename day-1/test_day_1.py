from day_1 import calibration_value


def test_calibration_value():
    assert calibration_value('1abc2') == 12
    assert calibration_value('pqr3stu8vwx') == 38
    assert calibration_value('treb7uchet') == 77
    assert calibration_value('hkxqfrqmsixfplbkpkdfzzszjxmdjtdkjlprrvr3gghlrqckqtbng') == 33