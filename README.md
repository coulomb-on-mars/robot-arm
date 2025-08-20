# Robot Arm

This project provides MicroPython code for controlling a four-servo robotic arm with a Raspberry Pi Pico. The Pico communicates with a PCA9685 16-channel PWM driver to move the servos. A three-axis joystick with a push button directs the arm.

## Hardware

- Raspberry Pi Pico running MicroPython
- PCA9685 16-channel 12-bit PWM driver
- Four hobby servos connected to channels 0–3
- Three-axis analog joystick with one push button

## Project Structure

```
main.py              # Entry point for the Pico
arm/
  __init__.py
  joystick.py        # Reads joystick axes and button
  pca9685.py         # Minimal driver for the PCA9685
  servo_controller.py# Helper for setting servo angles
  robot_arm.py       # High level coordination
tests/
  test_angles.py     # Unit tests for angle conversions
```

## Usage

1. Copy `main.py` and the `arm` package to the Pico.
2. Connect the joystick axes to ADC pins and the button to a GPIO pin.
3. Wire the PCA9685 to the I2C pins of the Pico and connect servos to channels 0–3.
4. On reset the script will continually read the joystick and move the servos.

## Development

Run basic checks with:

```
python -m py_compile $(git ls-files '*.py')
python -m pytest
```

