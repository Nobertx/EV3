#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick  # Importa a classe EV3Brick do módulo pybricks.hubs
from pybricks.ev3devices import Motor  # Importa a classe Motor do módulo pybricks.ev3devices
from pybricks.parameters import Port  # Importa a classe Port do módulo pybricks.parameters
from pybricks.robotics import DriveBase  # Importa a classe DriveBase do módulo pybricks.robotics
import time
import math  # Importa o módulo math para operações matemáticas

ev3 = EV3Brick()  # Cria uma instância da classe EV3Brick para interagir com o bloco EV3

left_motor = Motor(Port.A)  # Cria uma instância da classe Motor para o motor esquerdo
right_motor = Motor(Port.D)  # Cria uma instância da classe Motor para o motor direito

# Configure as medidas da roda
wheel_diameter = 43.2  # Diâmetro da roda em milímetros
axle_track = 104  # Distância entre as rodas em milímetros

# Cria uma instância da classe DriveBase para controlar o movimento do robô
robot = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track)

ev3.speaker.beep()  # Emite um som para indicar o início do programa
robot.straight(1000)  # Move o robô para frente por 1000mm

# Obter as distâncias percorridas pelos motores
left_motor_distance = left_motor.angle() * math.pi * wheel_diameter / 360  # Calcula a distância percorrida pelo motor esquerdo em milímetros
right_motor_distance = right_motor.angle() * math.pi * wheel_diameter / 360  # Calcula a distância percorrida pelo motor direito em milímetros

# Calcular a posição aproximada do robô
distance_center = (left_motor_distance + right_motor_distance) / 2  # Calcula a média das distâncias percorridas pelos motores em milímetros
angle_rad = math.radians(robot.angle())  # Converte o ângulo do robô de graus para radianos
x = distance_center * math.cos(angle_rad)  # Calcula a coordenada X da posição em milímetros

ev3.speaker.beep()  # Emite um som para indicar o final do movimento para frente
robot.turn(90)
robot.straight(1000)  # Move o robô para trás por 1000mm

# Obter as distâncias percorridas pelos motores
left_motor_distance = left_motor.angle() * math.pi * wheel_diameter / 360  # Calcula a distância percorrida pelo motor esquerdo em milímetros
right_motor_distance = right_motor.angle() * math.pi * wheel_diameter / 360  # Calcula a distância percorrida pelo motor direito em milímetros

# Calcular a posição aproximada do robô
distance_center = (left_motor_distance + right_motor_distance) / 2  # Calcula a média das distâncias percorridas pelos motores em milímetros
angle_rad = math.radians(robot.angle())  # Converte o ângulo do robô de graus para radianos
y = distance_center * math.sin(angle_rad)  # Calcula a coordenada Y da posição em milímetros

x = round(x, 2)
y = round(y, 2)

# Imprimir a posição atual do robô
print("Posição atual do robô:")
print("X: {} mm".format(x))
print("Y: {} mm".format(y))
ev3.screen.print("X: {} mm".format(x))
time.sleep(5)
ev3.screen.print("Y: {} mm".format(y))
time.sleep(5)

# Parar os motores
robot.stop()
