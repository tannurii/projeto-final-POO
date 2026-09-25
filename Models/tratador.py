from Models.cronograma import Cronograma
from Models.tarefa import TipoTarefa
from Models.animal import *
from Models.recinto import *
from Models.especies import *



class Tratador():
  def __init__(self):
    self.cronograma = Cronograma()
    self.tarefas_concluidas = []

  def tratar_animal(self, id_animal):
    animal, service = Animal.buscar_animal_por_id(id_animal)
    id_especie = animal["id_especie"]
    lista_de_especies = carregar("Data/especies.json")
    for especie in lista_de_especies:
      if id_especie == especie["id"]:
        tratamento = especie["tratamento"]
    if not animal:
      return "Animal não encontrado."

    animal["tratado"] = True
    service.atualizar_animal(animal)
    return f"{animal["nome_especie"]} passou pelo tratamento: {tratamento}"


  def alimentar_animal(self, id_animal):
    animal, service = Animal.buscar_animal_por_id(id_animal=id_animal)
    if not animal:
      return "Animal não encontrado"
    
    animal["saciado"] = True
    service.atualizar_animal(animal)
    return f"{animal["nome_especie"]} alimentado com sucesso!"

  def limpar_recinto(self, id_recinto):
    recinto, service = Recinto.buscar_recinto_por_id(id_recinto=id_recinto)
    if not recinto:
      return "recinto não encontrado."

    recinto["limpeza"] = True
    service.atualizar_recinto(recinto)
    return f"Limpeza do recinto realizada com sucesso!"

  def banho_de_sol(self, id_animal):
    animal, service = Animal.buscar_animal_por_id(id_animal=id_animal)
    if not animal:
      return "Animal não encontrado."

    especie_service = Especie()
    especie = especie_service.buscar_especie(id_especie=animal["id_especie"])

    if especie["banho_de_sol"]:
      animal["banho_de_sol_tomado"] = True
      service.atualizar_animal(animal)
      return f"O animal {animal["nome_especie"]} tomou banho de sol!"

    return "Esta espécie não necessita de banho de sol."

  def executar_tarefa(self, tarefa):
    match tarefa.tipo:
          
          case TipoTarefa.TRATAR:
            
            return self.tratar_animal(tarefa.id_animal)
            
            
    
          
          case TipoTarefa.ALIMENTAR:
            
            return self.alimentar_animal(tarefa.id_animal)
            
    
          case TipoTarefa.LIMPAR:
            
            return self.limpar_recinto(tarefa.id_recinto)
            
    
    
          case TipoTarefa.BANHO:
            
            return self.banho_de_sol(tarefa.id_animal)
            

          case _:
            return "Tarefa Inválida"

      
  def verificar_tarefa(self, horario):
    return self.cronograma.buscar_tarefa(horario)