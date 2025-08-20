"""High level servo control using the PCA9685."""

from .pca9685 import PCA9685
from .angles import angle_to_ticks

class ServoController:
    """Control servos connected to a PCA9685."""

    def __init__(self, i2c, address: int = 0x40, freq: int = 50,
                 min_us: int = 500, max_us: int = 2500):
        self.pca = PCA9685(i2c, address)
        self.pca.set_freq(freq)
        self.min_us = min_us
        self.max_us = max_us
        self.freq = freq

    def set_angle(self, channel: int, angle: float):
        """Set the angle of a servo on a specific channel."""
        ticks = angle_to_ticks(angle, self.min_us, self.max_us, self.freq)
        self.pca.set_pwm(channel, 0, ticks)
