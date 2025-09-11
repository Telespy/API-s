from requests import get
import json
from random import randint

def pokemon(nome):
    url=f"https://pokeapi.co/api/v2/pokemon/{nome}"
    resposta=get(url)

    d=resposta.json()
    return d

nome=input("Digite o nome de um Pokemon: ")
dados=pokemon(nome)

print("=== Tipagem ===")
print(f"Primeira tipagem > {dados["types"][0]["type"]["name"].title()}")
try:
    print(f"Primeira tipagem > {dados["types"][1]["type"]["name"].title()}")
except:
    pass

print("\n=== Status ===")
for c in range(0,6):
    print(f"{dados["stats"][c]["stat"]["name"].title()} > {dados["stats"][c]["base_stat"]}")

print("\n=== Habilidades ===")
for c in range(0,4,2):
    print(f"{dados["moves"][randint(0,len(dados["stats"]))]["move"]["name"].title()} | {dados["moves"][randint(0,len(dados["stats"]))+1]["move"]["name"].title()}")
