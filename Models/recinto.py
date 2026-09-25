import uuid
from Data.json_storage import carregar, salvar

class Recinto():
  local = None
  def __init__(self):
    self.capacidade_total = 5
    self.quantidade_atual = 0
    self.limpeza = False


  @staticmethod
  def buscar_recinto_por_id(id_recinto):
    recintos = [
    RecintoMamiferos(),
    RecintoAves(),
    RecintoRepteis(),
    RecintoPeixes(),
    RecintoAnfibios()
    ]
    for r in recintos:
      recinto = r.buscar_recinto(id_recinto)

      if recinto:
        return recinto, r
      
    return None, None
    
  def criar_recinto(self):
    try:
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
    except:
      return "não foi possível criar o recinto."

    return "recinto criado com sucesso!"

  def cadastrar_animal_no_recinto(self, animal):
    
    print("Procurando vaga nos recintos...")
    lista_de_recintos = carregar(local=self.local) or []
    if len(lista_de_recintos) == 0:
      return "Primeiro crie um recinto da espécie do animal que deseja alocar!"
    
    for recinto in lista_de_recintos:
      if animal["id"] in recinto["id_animais"]:
        return "Animal já cadastrado em um recinto."

    for recinto in lista_de_recintos:
      if recinto["lotacao"] < recinto["capacidade"]:
          recinto["lotacao"] += 1
          recinto["id_animais"].append(animal["id"])
          salvar(dado=lista_de_recintos, local=self.local, identacao=10)
          return "Animal cadastrado com sucesso."

    return "Nenhum recinto disponível."



  def buscar_recinto(self, id_recinto):
    lista_de_recintos = carregar(local=self.local) or []
    for recinto in lista_de_recintos:
      if recinto["id"] == id_recinto:
        return recinto


  def atualizar_recinto(self, recinto_atualizado):

    lista_de_recintos = carregar(local=self.local) or []

    for indice, recinto in enumerate(lista_de_recintos):

        if recinto["id"] == recinto_atualizado["id"]:

            lista_de_recintos[indice] = recinto_atualizado

            salvar(dado=lista_de_recintos, local=self.local, identacao=10)

            return True

    return False

   

class RecintoAnfibios(Recinto):
  local = "Data/recintos/recinto_anfibios.json"

class RecintoAves(Recinto):
  local = "Data/recintos/recinto_aves.json"

class RecintoMamiferos(Recinto):
  local = "Data/recintos/recinto_mamiferos.json"

class RecintoPeixes(Recinto):
  local = "Data/recintos/recinto_peixes.json"

class RecintoRepteis(Recinto):
  local = "Data/recintos/recinto_repteis.json"

