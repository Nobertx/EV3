#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick  # Importa a classe EV3Brick do módulo pybricks.hubs
from pybricks.ev3devices import Motor  # Importa a classe Motor do módulo pybricks.ev3devices
from pybricks.parameters import Port  # Importa a classe Port do módulo pybricks.parameters
from pybricks.robotics import DriveBase  # Importa a classe DriveBase do módulo pybricks.robotics
import math  # Importa o módulo math para operações matemáticas

ev3 = EV3Brick()  # Cria uma instância da classe EV3Brick para interagir com o bloco EV3

left_motor = Motor(Port.A)  # Cria uma instância da classe Motor para o motor esquerdo
right_motor = Motor(Port.D)  # Cria uma instância da classe Motor para o motor direito

# Configure as medidas da roda
wheel_diameter = 43.2  # Diâmetro da roda em milímetros
entre_eixos = 143 # Distância entre as rodas em milímetros

# Cria uma instância da classe DriveBase para controlar o movimento do robô
robot = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=entre_eixos)

ev3.speaker.beep()  # Emite um som para indicar o início do programa
X = []
Y= []
teta = []

raio = wheel_diameter/2
posicao_atual = 0
distancia_alvo = 500
Nd = 0 #pulsos roda direita
Ne = 0 #pulsos roda esquerda
Pd = 0 #total de pulsos roda direita
Pe = 0 #total de pulsos roda esquerda
distancia = 0

def move(alvo):
  cont = 0
  global Pe, Pd, Ne, Nd
  while cont < alvo:
    if not X and not Y:
      X.append(0)
      Y.append(0)
      teta.append(0)
    else:
      robot.straight(100) #Robô anda 100mm
      Pe = Pe + Ne #Calcula total de rotações da roda esquerda
      Pd = Pd + Nd #Calcula total de rotações da roda direita
      Ne = left_motor.angle() - Pe #calcula a última rotação da roda esquerda
      Nd = right_motor.angle() - Pd #calcula a última rotação da roda direita
      teta.append(teta[-1] + (2*math.pi * ((Ne * raio) - (Nd * raio))/(360*entre_eixos))) #cálculo de teta
      X.append(X[-1] + (math.pi * ((Ne * raio) + (Nd * raio))/360  * math.cos(teta[-1]))) #cálculo de X
      Y.append(Y[-1] + (math.pi * ((Ne * raio) + (Nd * raio))/360  * math.sin(teta[-1]))) #cálculo de Y
      cont += 1

    print("X: ",X[-1])
    print("Y: ",Y[-1])
    print("teta: ",teta[-1], "\n")

move(20)
#robot.turn(90)
#move(10)
print("X: [{}]".format(", ".join("{:.4f}".format(x) for x in X)))
print("Y: [{}]".format(", ".join("{:.4f}".format(y) for y in Y)))
print("Teta: [{}]".format(", ".join("{:.4f}".format(x) for x in teta)))

ev3.speaker.beep()  # Emite um som para indicar o final do movimento para frente
robot.stop()
