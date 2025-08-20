"""Robotic arm coordination logic."""

import utime

class RobotArm:
    """Tie joystick input to servo outputs."""

    def __init__(self, servo_controller, joystick):
        self.servo = servo_controller
        self.joystick = joystick
        self.grip_open = False
        self._last_button = False

    def update(self):
        x, y, z, button = self.joystick.read()
        self.servo.set_angle(0, x * 180 / 65535)
        self.servo.set_angle(1, y * 180 / 65535)
        self.servo.set_angle(2, z * 180 / 65535)

        if button and not self._last_button:
            self.grip_open = not self.grip_open
            angle = 90 if self.grip_open else 0
            self.servo.set_angle(3, angle)
        self._last_button = button

    def loop(self, delay_ms: int = 50):
        """Continuously update the arm based on joystick input."""
        while True:
            self.update()
            utime.sleep_ms(delay_ms)
