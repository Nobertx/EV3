#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import time

# Inicialização do EV3 Brick
ev3 = EV3Brick()

# Inicialização do motor no Porta B
motor = Motor(Port.A)

# Ler a posição atual do encoder
encoder_pos = motor.angle()

# Exibir a posição atual do encoder
ev3.screen.clear()
ev3.screen.print(str(encoder_pos))

# Esperar por algum tempo (opcional)
ev3.speaker.beep()
time.sleep(2)

# Configuração das velocidades dos motores (em graus por segundo)
velocidade = 300
velocidade_rotacao = 150

# Definição das durações dos movimentos (em milissegundos)
duracao_rotacao = 1500

motor.run_time(velocidade, duracao_rotacao)

# Ler a nova posição do encoder
new_encoder_pos = motor.angle()

# Exibir a nova posição do encoder
ev3.screen.clear()
ev3.screen.print(str(new_encoder_pos))

ev3.speaker.beep()
time.sleep(5)
# Parar o motor
motor.stop()
