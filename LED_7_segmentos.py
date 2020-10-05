# -*- coding: utf-8 -*-

'''
 Classe responsável por criar a representação de cada algarismo
 no formato LED de 7 segmentos e com o tamanho solicitado pelo usuário
'''

class LED:
  

  '''
  O método a seguir é responsável por criar uma lista de strings
  contendo linha a linha os caracteres que formam o algarismo
  no formato LED de 7 segmentos e com o tamanho solicitado pelo usuário
  '''
  def geraLED(self, altura, tamanho):
    #Display de 7 segmentos de tamanho 1
    if tamanho == 1:
      if self.numero == 0:
        self.strings = [' __ ', '|  |', '|__|']
      elif self.numero == 1:
        self.strings = ['    ', '   |', '   |']
      elif self.numero == 2:
        self.strings = [' __ ', ' __|', '|__ ']
      elif self.numero == 3:
        self.strings = [' __ ', ' __|', ' __|']
      elif self.numero == 4:
        self.strings = ['    ', '|__|', '   |']
      elif self.numero == 5:
        self.strings = [' __ ', '|__ ', ' __|']
      elif self.numero == 6:
        self.strings = [' __ ', '|__ ', '|__|']
      elif self.numero == 7:
        self.strings = [' __ ', '   |', '   |']
      elif self.numero == 8:
        self.strings = [' __ ', '|__|', '|__|']
      elif self.numero == 9:
        self.strings = [' __ ', '|__|', '   |']
    #Display de 7 segmentos de tamanho 2
    elif tamanho == 2:
      if self.numero == 0:
        self.strings = [' ____ ', '|    |','|    |', '|    |', '|____|']
      elif self.numero == 1:
        self.strings = ['      ', '     |', '     |', '     |', '     |']
      elif self.numero == 2:
        self.strings = [' ____ ', '     |', ' ____|', '|     ', '|____ ']
      elif self.numero == 3:
        self.strings = [' ____ ', '     |', ' ____|', '     |', ' ____|']
      elif self.numero == 4:
        self.strings = ['      ', '|    |', '|____|', '     |', '     |']
      elif self.numero == 5:
        self.strings = [' ____ ', '|     ', '|____ ', '     |', ' ____|']
      elif self.numero == 6:
        self.strings = [' ____ ', '|     ', '|____ ', '|    |', '|____|']
      elif self.numero == 7:
        self.strings = [' ____ ', '     |', '     |', '     |', '     |']
      elif self.numero == 8:
        self.strings = [' ____ ', '|    |', '|____|', '|    |', '|____|']
      elif self.numero == 9:
        self.strings = [' ____ ', '|    |', '|____|', '     |', '     |']
    #Display de 7 segmentos de tamanho 3
    elif tamanho == 3:
      if self.numero == 0:
        self.strings = [' ______ ', '|      |', '|      |', '|      |', '|      |', '|      |', '|______|']
      elif self.numero == 1:
        self.strings = ['        ', '       |', '       |', '       |', '       |', '       |', '       |']
      elif self.numero == 2:
        self.strings = [' ______ ', '       |', '       |', ' ______|', '|       ', '|       ', '|______ ']
      elif self.numero == 3:
        self.strings = [' ______ ', '       |', '       |', ' ______|', '       |', '       |', ' ______|']
      elif self.numero == 4:
        self.strings = ['        ', '|      |', '|      |', '|______|', '       |', '       |', '       |']
      elif self.numero == 5:
        self.strings = [' ______ ', '|       ', '|       ', '|______ ', '       |', '       |', ' ______|']
      elif self.numero == 6:
        self.strings = [' ______ ', '|       ', '|       ', '|______ ', '|      |', '|      |', '|______|']
      elif self.numero == 7:
        self.strings = [' ______ ', '       |', '       |', '       |', '       |', '       |', '       |']
      elif self.numero == 8:
        self.strings = [' ______ ', '|      |', '|      |', '|______|', '|      |', '|      |', '|______|']
      elif self.numero == 9:
        self.strings = [' ______ ', '|      |', '|      |', '|______|', '       |', '       |', '       |']
    #Display de 7 segmentos de tamanho 4
    elif tamanho == 4:
      if self.numero == 0:
        self.strings = [' ________ ', '|        |', '|        |', '|        |', '|        |', '|        |', '|        |', '|        |', '|________|']
      elif self.numero == 1:
        self.strings = ['          ', '         |', '         |', '         |', '         |', '         |', '         |', '         |', '         |']
      elif self.numero == 2:
        self.strings = [' ________ ', '         |', '         |', '         |', ' ________|', '|         ','|         ', '|         ', '|________ ']
      elif self.numero == 3:
        self.strings = [' ________ ', '         |', '         |', '         |', ' ________|', '         |', '         |', '         |', ' ________|']
      elif self.numero == 4:
        self.strings = ['          ', '|        |', '|        |', '|        |', '|________|', '         |', '         |', '         |', '         |']
      elif self.numero == 5:
        self.strings = [' ________ ', '|         ', '|         ', '|         ', '|________ ', '         |', '         |', '         |', ' ________|']
      elif self.numero == 6:
        self.strings = [' ________ ', '|         ', '|         ', '|         ', '|________ ', '|        |','|        |', '|        |', '|________|']
      elif self.numero == 7:
        self.strings = [' ________ ', '         |', '         |', '         |', '         |', '         |', '         |', '         |', '         |']
      elif self.numero == 8:
        self.strings = [' ________ ', '|        |', '|        |', '|        |', '|________|', '|        |', '|        |', '|        |', '|________|']
      elif self.numero == 9:
        self.strings = [' ________ ', '|        |', '|        |', '|        |', '|________|', '         |', '         |', '         |', '         |']
    #Display de 7 segmentos de tamanho 5
    elif tamanho == 5:
      if self.numero == 0:
        self.strings = [' __________ ', '|          |', '|          |', '|          |', '|          |', '|          |', '|          |', '|          |', '|          |', '|          |', '|__________|']
      elif self.numero == 1:
        self.strings = ['            ', '           |', '           |', '           |', '           |', '           |', '           |', '           |', '           |', '           |', '           |']
      elif self.numero == 2:
        self.strings = [' __________ ', '           |', '           |', '           |', '           |', ' __________|', '|           ', '|           ', '|           ', '|           ', '|__________ ']
      elif self.numero == 3:
        self.strings = [' __________ ', '           |', '           |', '           |', '           |', ' __________|', '           |', '           |', '           |', '           |', ' __________|']
      elif self.numero == 4:
        self.strings = ['            ', '|          |', '|          |', '|          |', '|          |', '|__________|', '           |', '           |', '           |', '           |', '           |']
      elif self.numero == 5:
        self.strings = [' __________ ', '|           ', '|           ', '|           ', '|           ', '|__________ ', '           |', '           |', '           |', '           |', ' __________|']
      elif self.numero == 6:
        self.strings = [' __________ ', '|           ', '|           ', '|           ', '|           ', '|__________ ', '|          |', '|          |', '|          |', '|          |', '|__________|']
      elif self.numero == 7:
        self.strings = [' __________ ', '           |', '           |', '           |', '           |', '           |', '           |', '           |', '           |', '           |', '           |']
      elif self.numero == 8:
        self.strings = [' __________ ', '|          |', '|          |', '|          |', '|          |', '|__________|', '|          |', '|          |', '|          |', '|          |', '|__________|']
      elif self.numero == 9:
        self.strings = [' __________ ', '|          |', '|          |', '|          |', '|          |', '|__________|', '           |', '           |', '           |', '           |', '           |']
