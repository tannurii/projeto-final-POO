from Models.especies import *
from Models.animal import *
from Models.recinto import *
from Models.tarefa import Tarefa, TipoTarefa
from Models.cronograma import *
from Models.tratador import *
from datetime import datetime
from Models.menu import *

def cadastrar_especie():
  especie = Especie()

  nome = input("nome: ").strip().lower()
  tratamento = input("tratamento: ").strip().lower()
  alimentacao = input("Alimentação: ").strip().lower()
  banho_de_sol = input("Toma banho de sol[S/N]: ").strip().lower()
  print(especie.cadastrar_especie(nome=nome, tratamento=tratamento, alimentacao=alimentacao,banho_de_sol= banho_de_sol))
  return nome

def cadastrar_animal():
  mostrar_classes_de_animais()
  try:
    operador = int(input("Digite a classe deste animal: ").strip().lower())


  except ValueError:
    print("Valor inválido. Digite apenas números!")
    return

  else:
    match operador:
      case 1:
        animal = Anfibios()
      case 2:
        animal = Aves()
      case 3:
        animal = Mamiferos()
      case 4:
        animal = Peixes()
      case 5:
        animal = Repteis()

    try:
      nome_especie = str(input("Nome da espécie: ").strip().lower())
      apelido = str(input("Apelido[Para não colocar apelido, basta ENTER]: ").strip().lower())
      idade = int(input("Idade: "))
      sexo = "masculino" if str(input("Sexo[M/F]: ").strip().lower()) in "masculino" else "feminino"
      
    except ValueError:
      print("Valor inválido. Retornando...")
      return
    else:
      animal.cadastrar_animal(nome_especie=nome_especie, apelido=apelido, idade=idade, sexo=sexo)
      return nome_especie


def criar_recinto():
  mostrar_classes_de_animais()
  try:
    operador = int(input("Para qual classe será criado: ").strip().lower())

  except ValueError:
    print("Valor inválido. Digite apenas números!")
    return
  
  else:
    match operador:

      case 1:
        recinto = RecintoAnfibios()
      case 2:
        recinto = RecintoAves()
      case 3:
        recinto = RecintoMamiferos()
      case 4:
        recinto = RecintoPeixes()
      case 5:
        recinto = RecintoRepteis()

    print(recinto.criar_recinto())


def alocar_animal():
  
  id_animal = str(input("Digite o id do animal que deseja alocar: ").strip().lower())
  animal, classe = Animal.buscar_animal_por_id(id_animal=id_animal)

  if not animal:
    return"Animal não encontrado."
  
  match classe:
    case Anfibios():
      recinto = RecintoAnfibios()
    case Aves():
      recinto = RecintoAves()
    case Mamiferos():
      recinto = RecintoMamiferos()
    case Peixes():
      recinto = RecintoPeixes()
    case Repteis():
      recinto = RecintoRepteis()

  recinto.cadastrar_animal_no_recinto(animal=animal)


def criar_tarefa():
  try:
    mostrar_tarefas_possiveis()
    tipo = int(input("Escolha uma tarefa: "))
  except ValueError:
      print("Valor inválido. Digite apenas números!")
      return
  else:
    match tipo:
            case 1:
                tipo = TipoTarefa.TRATAR

            case 2:
                tipo = TipoTarefa.ALIMENTAR
    
            case 3:
                tipo = TipoTarefa.LIMPAR
    
            case 4:
                tipo = TipoTarefa.BANHO
    
            case _:
                print("Opção inválida.")
                return

  horario = input("Digite o horário (HH:MM): ").strip()

  try:
      horario = datetime.strptime(horario, "%H:%M").strftime("%H:%M")
  except ValueError:
      print("Horário inválido.")
      return

  id_referencia = str(input("Digite o id do animal/recinto: ").strip().lower())
  if tipo == TipoTarefa.LIMPAR:
     tarefa = Tarefa(horario=horario, tipo=tipo, id_animal=None, id_recinto=id_referencia)
  else:
     tarefa = Tarefa(horario=horario, tipo=tipo, id_animal=id_referencia, id_recinto=None)

  cronograma = Cronograma()
  print(cronograma.adicionar_tarefa(tarefa=tarefa))


def executar_tarefa(horario):
  tratador = Tratador()
  tarefa = tratador.verificar_tarefa(horario=horario)
  if not tarefa:
     return "Tarefa não encontrada."
  print(tratador.executar_tarefa(tarefa=tarefa))


def consultar_tarefas():
   listar_todas_as_tarefas()
   return


  

    