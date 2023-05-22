#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Inicialização do EV3 Brick
ev3 = EV3Brick()

# Inicialização dos motores
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Inicialização do DriveBase
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Definição da distância em milímetros
distancia = 200

# Configuração das velocidades dos motores (em graus por segundo)
velocidade = 500

# Configuração da aceleração dos motores (em graus por segundo ao quadrado)
aceleracao = 1000

# Configuração da velocidade de rotação (em graus por segundo)
velocidade_rotacao = 200

# Configuração da aceleração de rotação (em graus por segundo ao quadrado)
aceleracao_rotacao = 500

# Configuração do tempo de espera para cada movimento (em milissegundos)
tempo_espera = 1000

# Configuração do tempo de espera para as rotações (em milissegundos)
tempo_espera_rotacao = 500

# Configuração da frenagem suave
robot.settings(velocidade, aceleracao, velocidade_rotacao, aceleracao_rotacao)

# Andar em linha reta
robot.straight(distancia)
ev3.speaker.beep()

# Virar para a direita
robot.turn(90)
ev3.speaker.beep()

# Percorrer a mesma distância
robot.straight(distancia)
ev3.speaker.beep()

# Dar meia volta
robot.turn(180)
ev3.speaker.beep()

# Andar o dobro da distância anterior
robot.straight(distancia * 2)
ev3.speaker.beep()

robot.turn(180)
ev3.speaker.beep()

robot.straight(distancia)
ev3.speaker.beep()
# Parar os motores
robot.stop()
