import uuid
from Data.json_storage import carregar, salvar
from especies import Especie

class Animal():
    arquivo = None
    if not arquivo:
      raise ValueError("Classe Animal não pode ser utilizada diretamente.")
          

    
    def cadastrar_animal(self, idade, sexo, nome_especie, apelido=None):
        lista_de_animais = carregar(self.arquivo) or []
        especie_service = Especie()
        especie = especie_service.verificar_especie(nome=nome_especie)
        
        if especie:
            print("Espécie já cadastrada! Buscando no banco de dados...")

            novo_animal = {
                "id": str(uuid.uuid4()),
                "id_especie": especie["id"],
                "nome_especie": especie["nome"],
                "apelido": apelido,
                "idade": idade,
                "sexo": sexo,
                "saciado": False
            }

            lista_de_animais.append(novo_animal)
            salvar(dado=lista_de_animais, local=self.arquivo, identacao=7)

        else:
            print(f"Espécie não encontrada. Vamos realizar o cadastro...")
            tratamento = str(input("Digite o tratamento adequado da espécie: ").strip().lower())
            alimentacao = str(input("Qual é o tipo de orientação alimentar:").strip().lower())
            banho_de_sol = False if input("Toma banho de sol[S/N]: ").strip().lower() == "n" else True
            especie_service.cadastrar_especie(nome=nome_especie, tratamento=tratamento, alimentacao=alimentacao, banho_de_sol=banho_de_sol)
            self.cadastrar_animal(idade=idade, sexo=sexo, nome_especie=nome_especie, apelido=apelido)
           

class Anfibios(Animal):
    arquivo = "Data/classes_animais/anfibios.json"
class Aves(Animal):
    arquivo = "Data/classes_animais/aves.json"
class Mamiferos(Animal):
    arquivo = "Data/classes_animais/mamiferos.json"
class Peixes(Animal):
    arquivo = "Data/classes_animais/peixes.json"
class Repteis(Animal):
    arquivo = "Data/classes_animais/repteis.json"
    
            

