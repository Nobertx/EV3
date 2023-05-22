#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Inicialização dos motores
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

# Configuração das velocidades dos motores (em graus por segundo)
velocidade = 300
velocidade_rotacao = 150

# Definição das durações dos movimentos (em milissegundos)
duracao_reta = 2000
duracao_rotacao = 1500

# Função para mover o EV3 em linha reta
def mover_em_reta():
    motor_esquerdo.run_time(velocidade, duracao_reta)
    motor_direito.run_time(velocidade, duracao_reta)

# Função para fazer o EV3 girar
def girar():
    motor_esquerdo.run_time(velocidade_rotacao, duracao_rotacao)
    motor_direito.run_time(-velocidade_rotacao, duracao_rotacao)

# Movendo em linha reta
mover_em_reta()
wait(duracao_reta)

# Girando à esquerda
girar()
wait(duracao_rotacao)

# Movendo em linha reta novamente
mover_em_reta()
wait(duracao_reta)

# Girando à direita
girar()
wait(duracao_rotacao)

# Movendo em linha reta pela última vez
mover_em_reta()
wait(duracao_reta)

# Parando os motores
motor_esquerdo.stop()
motor_direito.stop()
