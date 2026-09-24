import uuid
from Data.json_storage import carregar, salvar
class Especie():

  def cadastrar_especie(self, nome, tratamento, alimentacao, banho_de_sol=None):
      lista_de_especies = carregar("Data/especies.json") or []
      especie = self.buscar_especie(nome=nome)

      if especie:
        print(f"Espécie {especie['nome']} já catalogada!")
        return

      else:
        nova_especie = {
          "id": str(uuid.uuid4()),
          "nome": nome.strip().lower(),
          "tratamento": tratamento,
          "alimentacao": alimentacao,
          "banho_de_sol": banho_de_sol
        }
        lista_de_especies.append(nova_especie)
        salvar(dado=lista_de_especies, local="Data/especies.json", identacao=5)
        return "Espécie cadastrada com suceso!"

  def buscar_especie(self, nome=None, id_especie=None):
    if nome is None and id_especie is None:
      raise ValueError("Informe nome ou id_especie.")

    lista_de_especies = carregar("Data/especies.json") or []
    if nome:
      for especie in lista_de_especies:
        if especie["nome"].strip().lower() == nome.lower():
          return especie
    if id_especie:
      for especie in lista_de_especies:
              if especie["id"] == id_especie:
                return especie


    return None
  
    