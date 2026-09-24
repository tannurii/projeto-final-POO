class Tarefa():
  def __init__(self, horario,tipo, id_animal=None, id_recinto=None):
    self.horario = horario
    self.tipo = tipo
    self.id_animal = id_animal
    self.id_recinto = id_recinto
    self.tratador = None
    self.executada = False
    

from enum import Enum
class TipoTarefa(Enum):
  TRATAR = "Tratar"
  ALIMENTAR = "Alimentar"
  LIMPAR = "Limpar" 
  BANHO = "Banho"