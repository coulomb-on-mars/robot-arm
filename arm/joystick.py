"""Joystick input handling for Raspberry Pi Pico."""

from machine import ADC, Pin

class Joystick:
    """Read a three-axis joystick with a push button."""

    def __init__(self, x_pin=26, y_pin=27, z_pin=28, button_pin=16):
        self.x = ADC(x_pin)
        self.y = ADC(y_pin)
        self.z = ADC(z_pin)
        self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

    def read(self):
        """Return tuple of (x, y, z, button) values.

        Axes are 16-bit values from 0 to 65535. Button returns ``True`` when
        pressed.
        """
        x_val = self.x.read_u16()
        y_val = self.y.read_u16()
        z_val = self.z.read_u16()
        button_pressed = not self.button.value()
        return x_val, y_val, z_val, button_pressed
