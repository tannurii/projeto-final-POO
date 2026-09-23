#Importacoes
from cronograma import Cronograma
from tarefa import TipoTarefa

class Tratador():
  def __init__(self, nome):
    self.nome = nome
    self.cronograma = Cronograma()


  def tratar_animal(self, id_animal):
    pass


  def alimentar_animal(self, id_animal):
    pass


  def limpar_recinto(self, id_recinto):
    pass


  def banho_de_sol(self, id_animal):
    pass


  def executar_tarefa(self, tarefa):
    match tarefa.tipo:
          
          case TipoTarefa.TRATAR:
            self.tratar_animal(tarefa.id_animal)
            
    
          
          case TipoTarefa.ALIMENTAR:
            self.alimentar_animal(tarefa.id_animal)
            
    
          case TipoTarefa.LIMPAR:
            self.limpar_recinto(tarefa.id_recinto)
            
    
    
          case TipoTarefa.BANHO:
            self.banho_de_sol(tarefa.id_animal)
          

          case _:
            return "Tarefa Inválida"

      
  def verificar_tarefa(self, horario):
    return self.cronograma.buscar_tarefa(horario)