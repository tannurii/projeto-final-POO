from Data.json_storage import salvar, carregar
from Models.tarefa import Tarefa, TipoTarefa
import uuid

class Cronograma():
  

  def __init__(self):
    self.cronograma = carregar("Data/cronograma.json") or []
    tarefas_concluidas = []

  def adicionar_tarefa(self, tarefa):
    for t in self.cronograma:
      if t["horario"] == tarefa.horario:
        return "Horário já ocupado."

    nova_tarefa = {
      "id": str(uuid.uuid4()),
      "horario": tarefa.horario,
      "tipo": tarefa.tipo.value,
      "id_animal": tarefa.id_animal,
      "id_recinto": tarefa.id_recinto,
      "executada": tarefa.executada
    }

    self.cronograma.append(nova_tarefa)
    salvar(dado=self.cronograma, local="Data/cronograma.json", identacao=6)
    return "Tarefa adicionada com sucesso."


  def buscar_tarefa(self, horario):
    for t in self.cronograma:
      if t["horario"] == horario:
        return Tarefa(id_tarefa=t["id"],horario=t["horario"], tipo=TipoTarefa(t["tipo"]), id_animal=t["id_animal"], id_recinto=t["id_recinto"], executada=False)


  def todas_as_tarefas(self):
    return self.cronograma


  def eliminar_tarefa(self):
   lista_de_tarefas = self.cronograma
   for indice, tarefa in enumerate(lista_de_tarefas):
     if tarefa["executada"] == True:
       lista_de_tarefas.pop(indice)
       salvar(dado=lista_de_tarefas, local="Data/cronograma.json", identacao=6)
    





    