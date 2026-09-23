from Data.json_storage import salvar, carregar
from tarefa import Tarefa, TipoTarefa


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
      "id_animal": tarefa.id_animal,
      "id_recinto": tarefa.id_recinto
    }

    self.cronograma.append(nova_tarefa)
    salvar(dado=self.cronograma, local=r"Data\cronograma.json", identacao=4)


  def buscar_tarefa(self, horario):
    for t in self.cronograma:
      if t["horario"] == horario:
        return Tarefa(horario=t["horario"], tipo=TipoTarefa(t["tipo"]), id_animal=t["id_animal"], id_recinto=t["id_recinto"])



    