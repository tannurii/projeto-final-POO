from datetime import datetime,timedelta
from time import sleep
from Models.tratador import Tratador
from Models.animal import Animal
from Models.recinto import Recinto
from Models.cronograma import Cronograma
from Data.json_storage import carregar, salvar
class Relogio():
  def __init__(self):
    self.horario = "08:00"
    self.horario = datetime.strptime(self.horario, "%H:%M")
    self.horario_maximo = "13:00"
    self.horario_maximo = datetime.strptime(self.horario_maximo, "%H:%M")

  def passar_hora(self):
    self.horario += timedelta(minutes=1)


  def loop_diario(self):
    tratador = Tratador()
    cronograma = carregar(local="Data/cronograma.json")
    while self.horario <= self.horario_maximo:
      print(f"\rHorário: {self.horario.strftime('%H:%M')}", end="  ")
      sleep(0.1)
      horario_atual = self.horario.strftime("%H:%M")
      tarefa = tratador.verificar_tarefa(horario=horario_atual)
      if tarefa:
              print(tratador.executar_tarefa(tarefa=tarefa))
              for t in cronograma:
                 if t["id"] == tarefa.id:
                    t["executada"] = True
              
      self.passar_hora()
    
    print(f"Dia finalizado!")
    
       
    
