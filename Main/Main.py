import sys
import os

sys.path.append(
os.path.dirname(
os.path.dirname(os.path.abspath(__file__))
)
)


from Models.menu import *
from Models.operacoes import *

while True:
  mostrar_menu()
  try:
    operador = int(input("Escolha uma opção: "))

  except ValueError:
    print("Valor inválido. Digite apenas números!")
    pass

  else:
    match operador:

      case 1:
        cadastrar_especie()

      case 2:
        cadastrar_animal()

      case 3:
        criar_recinto()

      case 4:
        alocar_animal()

      case 5:
        criar_tarefa()

      case 6:
        pass

      case 7:
        consultar_tarefas()

      case 0:
        print("Finalizando o programa")
        break