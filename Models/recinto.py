import uuid
from Data.json_storage import carregar, salvar

class Recinto():
  local = None
  def __init__(self):
    self.capacidade_total = 5
    self.quantidade_atual = 0
    self.limpeza = False

  def criar_recinto(self):
    lista_de_recintos = carregar(local=self.local) or []
    novo_recinto = {
      "id": str(uuid.uuid4()),
      "capacidade": self.capacidade_total,
      "lotacao": 0,
      "limpeza": False,
      "id_animais": []
    }
    lista_de_recintos.append(novo_recinto)
    salvar(dado=lista_de_recintos, local=self.local, identacao=10)

  def cadastrar_animal_no_recinto(self, animal):
    
    print("Procurando vaga nos recintos...")
    lista_de_recintos = carregar(local=self.local) or []
    
    for recinto in lista_de_recintos:
      if animal["id"] in recinto["id_animais"]:
        return "Animal já cadastrado em um recinto."

    for recinto in lista_de_recintos:
      if recinto["lotacao"] < recinto["capacidade"]:
          recinto["lotacao"] += 1
          recinto["id_animais"].append(animal["id"])
          salvar(dado=lista_de_recintos, local=self.local, identacao=10)
          return "Animal cadastrado com sucesso."

    return "Nenhum recinto disponível"

    



  