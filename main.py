#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
# Initialize the EV3 brick.
ev3 = EV3Brick()
def teste1():
  # Initialize a motor at port B.
  test_motor_a = Motor(Port.A)
  test_motor_d = Motor(Port.D)
  # Play a sound.
  ev3.speaker.beep()
  # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
  test_motor_a.run_target(500, 720)
  #test_motor_d.run_target(500, 720)
  # Play another beep sound.
  ev3.speaker.beep(1000, 500)

def teste2():
    # Initialize the motors.
  left_motor = Motor(Port.A)
  right_motor = Motor(Port.D)

  # Initialize the drive base.
  robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

  # Go forward and backwards for one meter.
  robot.straight(1000)
  ev3.speaker.beep()

  robot.straight(-1000)
  ev3.speaker.beep()

  # Turn clockwise by 360 degrees and back again.
  robot.turn(360)
  ev3.speaker.beep()

  robot.turn(-360)
  ev3.speaker.beep()

#teste1()
teste2()