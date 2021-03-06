#######
# Lab 07 – Exercicio 09
# @author: IComp / UFAM
# AVENTURAS COM MOEDAS E ZUMBIS

from numpy import *

# Leitura do tabuleiro
tabuleiro = array(eval(input("Tabuleiro: ")))

# Sequencia de movimentos do personagem
mov = input("Movimentos: ")

# Posicao inicial do personagem
xtab = 0
ytab = 0

# Contadores de atributos do personagem
moeda = 0
life = 100

# Analise da jogada
for x in mov:
    # Move personagem para ESQUERDA
		if x == 'A':
			xtab = xtab-1 
		elif x == 'D':
			xtab+=1 
		elif x == 'W':
			ytab -= 1
		elif x == 'S':
			ytab +=1 

    # Trata evento
    # Moeda
		if tabuleiro[ytab,xtab] == 11:
			moeda +=1 
			tabuleiro[ytab,xtab] = 0
		elif tabuleiro[ytab,xtab] == 22:
			life -= 5

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
