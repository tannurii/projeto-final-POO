
class Tarefa():
  def __init__(self, id_tarefa, horario,tipo, executada, id_animal=None, id_recinto=None):
    self.id = id_tarefa
    self.horario = horario
    self.tipo = tipo
    self.id_animal = id_animal
    self.id_recinto = id_recinto
    self.executada = executada

    
    

from enum import Enum
class TipoTarefa(Enum):
  TRATAR = "Tratar"
  ALIMENTAR = "Alimentar"
  LIMPAR = "Limpar" 
  BANHO = "Banho"