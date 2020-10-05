# -*- coding: utf-8 -*-

'''
 Autor:     Matheus Kraisfeld Benevides de Lima
 Projeto:   Prova prática do processo seletivo do Studio Sol
            Relógio de tamanho variável com LED de 7 segmentos

'''

import time
import os
import platform
from threading import Thread
from time import strftime
from LED_7_segmentos import LED

global altura, tamanho, paraLoop
paraLoop = False
altura = 2
tamanho = 1

'''
O método readTamanho() é responsável por receber a entrada do usuário
e verificar se o valor é um número válido para atribuir ao tamanho,
se é uma entrada irrelevante ou se é uma entrada para sair do programa
'''
def readTamanho():
  global tamanho, altura, paraLoop
  while True:
    verificaEntrada = True
    while verificaEntrada:
      try:
        temp = input()
        if int(temp) >= 1 and int(temp) <= 5:
          verificaEntrada = False
          tamanho = temp
          altura = tamanho * 2
          break
        else:
          paraLoop = True
          break
      except:
        pass
    if paraLoop:
      break

'''
No método main, é criada uma thread e atribuída a ela a função de ler
o tamanho para que a execução do relógio não seja interrompida 
enquanto uma entrada é esperada. Além disso, é captado do sistema 
o horário e é gerada a exibição na forma do display de led de 7 segmentos
'''
def main():
  global tamanho, altura, paraLoop
  
  our_thread = Thread(target=readTamanho, args=())
  our_thread.start()
  
  while True: 
    if(tamanho > 5 or tamanho < 1 or paraLoop == True):
      break
    '''
    O bloco a seguir altera o comando de limpar o console de clear
    para cls, caso executado em Windows
    '''
    if(platform.system() == 'Windows'):
      os.system('cls') or None
    else:
      os.system('clear') or None
    
    #Atribuindo horário a uma string no formato HH:MM:SS
    rel = strftime('%H:%M:%S')
    #Atribuindo cada algarismo do horário para uma variável
    horas_1 = int(rel[0], 10)
    horas_2 = int(rel[1], 10)
    minutos_1 = int(rel[3], 10)
    minutos_2 = int(rel[4], 10)
    segundos_1 = int(rel[6], 10)
    segundos_2 = int(rel[7], 10)

    '''
    Criar objeto LED, gerar representação em formato LED e armazenar
    list de strings que compõe o algarismo
    '''
    #horas algarismo 1
    led_horas_1 = LED(horas_1, tamanho, altura)
    led_horas_1.geraLED(altura, tamanho)
    led_horas_1.geraSeparador(tamanho)
    led_1 = led_horas_1.getStrings()
    #horas algarismo 2
    led_horas_2 = LED(horas_2, tamanho, altura)
    led_horas_2.geraLED(altura, tamanho)
    led_2 = led_horas_2.getStrings()
    #minutos algarismo 1
    led_minutos_1 = LED(minutos_1, tamanho, altura)
    led_minutos_1.geraLED(altura, tamanho)
    led_3 = led_minutos_1.getStrings()
    #minutos algarismo 2
    led_minutos_2 = LED(minutos_2, tamanho, altura)
    led_minutos_2.geraLED(altura, tamanho)
    led_4 = led_minutos_2.getStrings()
    #segundos algarismo 1
    led_segundos_1 = LED(segundos_1, tamanho, altura)
    led_segundos_1.geraLED(altura, tamanho)
    led_5 = led_segundos_1.getStrings()
    #segundos algarismo 2
    led_segundos_2 = LED(segundos_2, tamanho, altura)
    led_segundos_2.geraLED(altura, tamanho)
    led_6 = led_segundos_2.getStrings()
    #separador (os dois pontos do relógio)
    separador1 = led_horas_1.getSeparador()
    separador2 = led_horas_1.getSeparador()

    '''
    Laço responsável por concatenar a impressão da linha de mesmo
    índice em cada lista de strings
    '''
    #h = hora
    #sep = separador
    #m = minuto
    #s = segundo
    bg = '\033[32m'
    end = '\033[0;0m'
    for h1, h2, sep1, m1, m2, sep2, s1, s2 in zip(led_1, led_2, separador1, led_3, led_4, separador2, led_5, led_6):
      '''print(h1),'''
      h1 = bg + h1 + end
      h2 = bg + h2 + end
      sep1 = bg + sep1 + end
      m1 = bg + m1 + end
      m2 = bg + m2 + end
      sep2 = bg + sep2 + end
      s1 = bg + s1 + end
      s2 = bg + s2 + end
      print(h1),
      print(h2),
      print(sep1),
      print(m1),
      print(m2),
      print(sep2),
      print(s1),
      print(s2) 
    print ('\nDigite um número de 1 a 5 para exibir o relógio ou outro número para sair:')
    #espera 1 segundo 
    time.sleep(1)

if __name__ == '__main__':
  print('Digite um número de 1 a 5 para exibir o relógio ou outro número para sair:')
  main()
