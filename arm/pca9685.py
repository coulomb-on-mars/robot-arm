"""Minimal PCA9685 driver for MicroPython."""

from machine import I2C
import utime

_MODE1 = 0x00
_PRESCALE = 0xFE
_LED0_ON_L = 0x06

class PCA9685:
    """Driver for the PCA9685 16-channel PWM controller."""

    def __init__(self, i2c: I2C, address: int = 0x40):
        self.i2c = i2c
        self.address = address

    def _write(self, reg: int, value: int):
        self.i2c.writeto_mem(self.address, reg, bytes([value & 0xFF]))

    def set_freq(self, freq: int):
        """Set PWM frequency in Hz."""
        prescale = int(25000000 / (4096 * freq) - 1)
        self._write(_MODE1, 0x10)  # sleep
        self._write(_PRESCALE, prescale)
        self._write(_MODE1, 0x80)  # restart
        utime.sleep_ms(5)

    def set_pwm(self, channel: int, on: int, off: int):
        """Set on/off tick counts for a channel."""
        data = bytearray([on & 0xFF, on >> 8, off & 0xFF, off >> 8])
        self.i2c.writeto_mem(self.address, _LED0_ON_L + 4 * channel, data)
