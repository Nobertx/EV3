#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick  # Importa a classe EV3Brick do módulo pybricks.hubs
from pybricks.ev3devices import Motor  # Importa a classe Motor do módulo pybricks.ev3devices
from pybricks.parameters import Port  # Importa a classe Port do módulo pybricks.parameters
from pybricks.robotics import DriveBase  # Importa a classe DriveBase do módulo pybricks.robotics
import math  # Importa o módulo math para operações matemáticas
import time

ev3 = EV3Brick()  # Cria uma instância da classe EV3Brick para interagir com o bloco EV3

left_motor = Motor(Port.A)  # Cria uma instância da classe Motor para o motor esquerdo
right_motor = Motor(Port.D)  # Cria uma instância da classe Motor para o motor direito

# Configure as medidas da roda
wheel_diameter = 43.2  # Diâmetro da roda em milímetros
entre_eixos = 143  # Distância entre as rodas em milímetros

# Cria uma instância da classe DriveBase para controlar o movimento do robô
robot = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=entre_eixos)

raio = wheel_diameter / 2

Nd = 0  # pulsos roda direita
Ne = 0  # pulsos roda esquerda
Pd = 0  # total de pulsos roda direita
Pe = 0  # total de pulsos roda esquerda.
X = []
Y = []
X.append(0)
Y.append(0)
teta = []
teta.append(0)


def move(alvo):
    cont = 0
    erro = alvo
    global Pe, Pd, Ne, Nd
    while erro > 2:
        robot.straight(100)  # Robô anda 100mm
        Pe = Pe + Ne  # Calcula total de rotações da roda esquerda
        Pd = Pd + Nd  # Calcula total de rotações da roda direita
        Ne = left_motor.angle() - Pe  # calcula a última rotação da roda esquerda
        Nd = right_motor.angle() - Pd  # calcula a última rotação da roda direita
        teta.append(teta[-1] + (2 * math.pi * ((Ne * raio) - (Nd * raio)) / (360 * entre_eixos)))  # cálculo de teta
        X.append(X[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.cos(teta[-1])))  # cálculo de X
        Y.append(Y[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.sin(teta[-1])))  # cálculo de Y
        erro = alvo - abs(X[-1])

    robot.turn(90)
    erro = alvo
    time.sleep(3)

    while erro > 2:
        
        robot.straight(100)  # Robô anda 100mm
        Pe = Pe + Ne  # Calcula total de rotações da roda esquerda
        Pd = Pd + Nd  # Calcula total de rotações da roda direita
        Ne = left_motor.angle() - Pe  # calcula a última rotação da roda esquerda
        Nd = right_motor.angle() - Pd  # calcula a última rotação da roda direita
        teta.append(teta[-1] + (2 * math.pi * ((Ne * raio) - (Nd * raio)) / (360 * entre_eixos)))  # cálculo de teta
        X.append(X[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.cos(teta[-1])))  # cálculo de X
        Y.append(Y[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.sin(teta[-1])))  # cálculo de Y
        erro = alvo - abs(Y[-1])
        
    robot.turn(90)
    erro = alvo * -1
    time.sleep(3)

    while erro < -2:
        
        robot.straight(100)  # Robô anda 100mm
        Pe = Pe + Ne  # Calcula total de rotações da roda esquerda
        Pd = Pd + Nd  # Calcula total de rotações da roda direita
        Ne = left_motor.angle() - Pe  # calcula a última rotação da roda esquerda
        Nd = right_motor.angle() - Pd  # calcula a última rotação da roda direita
        teta.append(teta[-1] + (2 * math.pi * ((Ne * raio) - (Nd * raio)) / (360 * entre_eixos)))  # cálculo de teta
        X.append(X[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.cos(teta[-1])))  # cálculo de X
        Y.append(Y[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.sin(teta[-1])))  # cálculo de Y
        erro = 0 - abs(X[-1])

    robot.turn(90)
    erro = alvo * -1
    time.sleep(3)

    while erro < -2:
        
        robot.straight(100)  # Robô anda 100mm
        Pe = Pe + Ne  # Calcula total de rotações da roda esquerda
        Pd = Pd + Nd  # Calcula total de rotações da roda direita
        Ne = left_motor.angle() - Pe  # calcula a última rotação da roda esquerda
        Nd = right_motor.angle() - Pd  # calcula a última rotação da roda direita
        teta.append(teta[-1] + (2 * math.pi * ((Ne * raio) - (Nd * raio)) / (360 * entre_eixos)))  # cálculo de teta
        X.append(X[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.cos(teta[-1])))  # cálculo de X
        Y.append(Y[-1] + (math.pi * ((Ne * raio) + (Nd * raio)) / 360 * math.sin(teta[-1])))  # cálculo de Y
        erro = 0 - abs(Y[-1])


print("Rota fechada")
move(1000)
print("X: [{}]".format(", ".join("{:.4f}".format(x) for x in X)))
print("Y: [{}]".format(", ".join("{:.4f}".format(y) for y in Y)))
print("Teta: [{}]".format(", ".join("{:.4f}".format(x) for x in teta)))

ev3.speaker.beep()  # Emite um som para indicar o final do movimento para frente
robot.stop()
