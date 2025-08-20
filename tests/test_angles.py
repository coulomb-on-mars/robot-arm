from arm.angles import angle_to_ticks


def test_angle_to_ticks_zero():
    assert angle_to_ticks(0) == 102


def test_angle_to_ticks_middle():
    assert angle_to_ticks(90) == 307


def test_angle_to_ticks_max():
    assert angle_to_ticks(180) == 512
