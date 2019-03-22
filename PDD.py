#O seguinte programa visa calcular a probabilidade de um jogador ganhar no programa 'Porta dos Desesperados'
#Contam-se somente os casos onde há vitória, sendo esta separada em dois tipos: manter a estratégia inicial ou optar pela segunda escolha

import random #Importa aleatoridade
from decimal import Decimal, ROUND_HALF_UP #Importa casa decimal
trocou_ganhou = 0
ficou_ganhou = 0
venceu = 0

for n in range(1,100000): #Loop para contagem
    portas = ["cabra1", "cabra2", "carro"]#Portas
    porta_escolhida = random.choice(portas) #Escolhe a primeira porta aleatoriamente
    if porta_escolhida == 'cabra1': #Se a primeira porta for falsa
        del portas[1]#Apresentador mostra a outra porta falsa
        porta_escolhida2 = random.choice(portas)#Escolhe a segunda porta aleatoriamente
        if porta_escolhida2 == 'carro':#Se trocar pela porta do prêmio
            trocou_ganhou += 1 #Incrementa probabilidade de ganho
            venceu += 1 #Incrementa variável de vitória
    elif porta_escolhida == 'cabra2':#Se a primeira porta for falsa
        del portas[0] #Apresentador mostra a outra porta falsa
        porta_escolhida2 = random.choice(portas)#Escolhe segunda porta
        if porta_escolhida2 == 'carro':#Se trocar pela porta do prêmio
            trocou_ganhou += 1
            venceu += 1
    else:#Se a primeira porta for a do prêmio
        del portas[0]#Apresentador mostra outra porta falsa
        porta_escolhida2 = random.choice(portas)#Escolhe segunda porta
        if porta_escolhida2 == 'carro':#Se manter a escolha
            ficou_ganhou += 1
            venceu += 1

trocou_ganhou = Decimal((trocou_ganhou/venceu)*100)#Tranforma em porcentagem
trocou_ganhou = Decimal(trocou_ganhou.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
print("Ganhou pois trocou: ", trocou_ganhou)#Printa porcentagem
ficou_ganhou = Decimal((ficou_ganhou/venceu)*100)
ficou_ganhou = Decimal(ficou_ganhou.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
print("Ganhou pois ficou: ", ficou_ganhou)
