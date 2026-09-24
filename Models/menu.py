def mostrar_menu():
  print("1 - Cadastrar Espécie\n" \
  "2 - Cadastrar animal\n" \
  "3 - Criar recinto\n" \
  "4 - Alocar animal\n" \
  "5 - Criar tarefa\n" \
  "6 - Executar tarefa\n" \
  "7 - Consultar lista de tarefas\n" \
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
  if not lista_de_tarefas:
    return "Não há tarefas agendadas."
  print("TAREFAS CADASTRADAS")
  for tarefa in lista_de_tarefas:
    print(
    f"{tarefa['horario']} | "
    f"{tarefa['tipo']}"
    )
