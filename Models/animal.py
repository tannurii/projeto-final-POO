import uuid
from Data.json_storage import carregar, salvar
from Models.especies import Especie

class Animal():
    arquivo = None
        
    @staticmethod
    def buscar_animal_por_id(id_animal):

        classes_animais = [
            Mamiferos(),
            Aves(),
            Repteis(),
            Peixes(),
            Anfibios()
        ]

        for classe in classes_animais:

            animal = classe.buscar_animal(id_animal)

            if animal:
                return animal, classe

        return None, None

    
    def cadastrar_animal(self, idade, sexo, nome_especie, apelido=None):
        lista_de_animais = carregar(self.arquivo) or []
        especie_service = Especie()
        especie = especie_service.buscar_especie(nome=nome_especie)
        
        if especie:
            print("Espécie5 cadastrada! Buscando no banco de dados...")

            novo_animal = {
                "id": str(uuid.uuid4()),
                "id_especie": especie["id"],
                "nome_especie": especie["nome"],
                "apelido": apelido,
                "idade": idade,
                "sexo": sexo,
                "saciado": False,
                "tratado": False,
                "banho_de_sol_tomado": None if especie["banho_de_sol"] == None else False
            }

            lista_de_animais.append(novo_animal)
            salvar(dado=lista_de_animais, local=self.arquivo, identacao=8)
            print(f"Animal cadastrado com sucesso! Segue id: {novo_animal["id"]}")

        else:
            print(f"Espécie não encontrada. Vamos realizar o cadastro...")
            tratamento = str(input("Digite o tratamento adequado da espécie: ").strip().lower())
            alimentacao = str(input("Qual é o tipo de orientação alimentar:").strip().lower())
            banho_de_sol = False if input("Toma banho de sol[S/N]: ").strip().lower() == "n" else True
            especie_service.cadastrar_especie(nome=nome_especie, tratamento=tratamento, alimentacao=alimentacao, banho_de_sol=banho_de_sol)
            self.cadastrar_animal(idade=idade, sexo=sexo, nome_especie=nome_especie, apelido=apelido)
           
    def buscar_animal(self, id_animal):
        lista_de_animais = carregar(local=self.arquivo) or []
        for animal in lista_de_animais:
            if animal["id"] == id_animal:
                return animal

        return None

    def atualizar_animal(self, animal_atualizado):

        lista_de_animais = carregar(local=self.arquivo) or []

        for indice, animal in enumerate(lista_de_animais):

            if animal["id"] == animal_atualizado["id"]:
                lista_de_animais[indice] = animal_atualizado
                salvar(dado=lista_de_animais, local=self.arquivo, identacao=7)
                return True

        return False

class Anfibios(Animal):
    arquivo = "Data/animais/anfibios.json"
class Aves(Animal):
    arquivo = "Data/animais/aves.json"
class Mamiferos(Animal):
    arquivo = "Data/animais/mamiferos.json"
class Peixes(Animal):
    arquivo = "Data/animais/peixes.json"
class Repteis(Animal):
    arquivo = "Data/animais/repteis.json"
