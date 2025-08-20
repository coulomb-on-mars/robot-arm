"""Entry point for controlling the robotic arm."""

from machine import I2C, Pin

from arm.joystick import Joystick
from arm.servo_controller import ServoController
from arm.robot_arm import RobotArm


def main():
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)
    joystick = Joystick()
    servo = ServoController(i2c)
    arm = RobotArm(servo, joystick)
    arm.loop()


if __name__ == "__main__":
    main()
