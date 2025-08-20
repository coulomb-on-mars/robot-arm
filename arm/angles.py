"""Utilities for servo angle conversions."""

def angle_to_ticks(angle: float, min_us: int = 500, max_us: int = 2500, freq: int = 50) -> int:
    """Convert a servo angle in degrees to PCA9685 tick counts.

    :param angle: Angle in degrees (0-180)
    :param min_us: Pulse width for 0 degrees in microseconds
    :param max_us: Pulse width for 180 degrees in microseconds
    :param freq: PWM frequency in Hz
    :return: Tick count (0-4095)
    """
    pulse_len = 1000000 / freq
    pulse = min_us + (max_us - min_us) * angle / 180
    ticks = int(pulse * 4096 / pulse_len)
    return ticks
