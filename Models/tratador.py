#Importacoes
from enum import Enum
from Data.json_storage import salvar, carregar


#Classe de estado
class TipoTarefa(Enum):
  TRATAR = "Tratar"
  ALIMENTAR = "Alimentar"
  LIMPAR = "Limpar" 
  BANHO = "Banho"


#--------------------------
#Classe Tarefa
class Tarefa():
  def __init__(self, horario,tipo, animal=None, recinto=None):
    self.horario = horario
    self.tipo = tipo
    self.animal = animal
    self.recinto = recinto

#Classe Cronograma
class Cronograma():
  

  def __init__(self):
    self.cronograma = carregar(r"Data\cronograma.json") or []


  def adicionar_tarefa(self, tarefa):
    for t in self.cronograma:
      if t["horario"] == tarefa.horario:
        return "Horário já ocupado."

    nova_tarefa = {
      "horario": tarefa.horario,
      "tipo": tarefa.tipo.value,
      "animal": tarefa.animal.nome if tarefa.animal else None,
      "recinto": tarefa.recinto.nome if tarefa.recinto else None
    }

    self.cronograma.append(nova_tarefa)
    salvar(dado=self.cronograma, local=r"Data\cronograma.json", identacao=4)


  def buscar_tarefa(self, horario):
    for t in self.cronograma:
      if t["horario"] == horario:
        return Tarefa(horario=t["horario"], tipo=TipoTarefa(t["tipo"]), animal=t["animal"], recinto=t["recinto"])

    
          

#--------------------------
#Classe Tratador
class Tratador():
  def __init__(self, nome):
    self.nome = nome
    self.cronograma = Cronograma()


  
  def tratar_animal(self, animal):
    pass


  def alimentar_animal(self, animal):
    pass


  def limpar_recinto(self, recinto):
    pass


  def banho_de_sol(self, animal):
    pass


  def executar_tarefa(self, tarefa):
    match tarefa.tipo:
          
          case TipoTarefa.TRATAR:
            self.tratar_animal(tarefa.animal)
            
    
          
          case TipoTarefa.ALIMENTAR:
            self.alimentar_animal(tarefa.animal)
            
    
          case TipoTarefa.LIMPAR:
            self.limpar_recinto(tarefa.recinto)
            
    
    
          case TipoTarefa.BANHO:
            self.banho_de_sol(tarefa.animal)
          

          case _:
            return "Tarefa Inválida"

      
  def verificar_tarefa(self, horario):
    return self.cronograma.buscar_tarefa(horario)