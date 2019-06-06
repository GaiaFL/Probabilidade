#O seguinte programa calcula a proporção amostral de uma população de 10 mil pessoas em um grupo de 7 mil pessoas

import random#Importa biblioteca de aleatoridade
for m in range(2000):#Loop para 2000 resultados
  A = 0 #Grupo que apresenta a característa de votante de A
  for n in range(7000):#Tamanho da amostra
   i = random.randint(1,10001)#Sorteia um número entre 1 e 10 mil
   if(i < 3001):#Caso o número sorteado for o de uma pessoa eleitora de A 
    A += 1 #Incrementa o tamanho do grupo 
  p = A/n #Calcula proporção amostral
  print(p)
