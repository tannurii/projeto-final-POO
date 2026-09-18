def salvar(dado, local, identacao):
  import json
  with open(f"{local}", "w") as file:
    json.dump(dado, file, indent=identacao)


def carregar(local):
  import json
  with open(f"{local}", "r") as file:
    return json.load(file)