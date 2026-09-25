def mostrar_menu():
  print()
  print("1 - Cadastrar Espécie\n" \
  "2 - Cadastrar animal\n" \
  "3 - Criar recinto\n" \
  "4 - Alocar animal\n" \
  "5 - Criar tarefa\n" \
  "6 - Consultar lista de tarefas\n" \
  "7 - Mostrar todos os animais\n" \
  "8 - Iniciar simulação do dia\n" \
  "0 - Sair")
  print()

def mostrar_classes_de_animais():
  print("1 - Anfíbios\n" \
  "2 - Aves\n" \
  "3 - Mamíferos\n" \
  "4 - Peixes\n" \
  "5 - Répteis")
  print()

def mostrar_tarefas_possiveis():
  print("1 - Tratar")
  print("2 - Alimentar")
  print("3 - Limpar")
  print("4 - Banho")

def listar_todas_as_tarefas():
  from Models.cronograma import Cronograma
  cronograma = Cronograma()
  lista_de_tarefas = cronograma.todas_as_tarefas()
  if len(lista_de_tarefas) == 0:
    return "Não há tarefas agendadas."
  lista_ordenada = sorted(lista_de_tarefas, key=lambda tarefa: tarefa["horario"])
  
  print("TAREFAS CADASTRADAS")
  for tarefa in lista_ordenada:
      print(
      f"{tarefa['horario']} | "
      f"{tarefa['tipo']}"
      )
