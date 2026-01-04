from requests import get,exceptions
import json

def local(end):
    """
    Busca um endereço a partir do CEP
    """
    url=f"https://viacep.com.br/ws/{end}/json/"

    print(f"Buscando dados do endereço em > {url}")

    try:
        resposta=get(url)
        resposta.raise_for_status()

        dados=resposta.json()

        if dados.get("erro")=="true":
            print("\nEsse CEP é inválido")
            quit()
        else:
            return dados
    except exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
        print("\nThere was likely an error in your API key. Please try another one.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        return None

loc=local("60030970")
endereco=loc.get("logradouro")
bairro=loc.get("bairro")
cidade=loc.get("localidade")
estado=loc.get("estado")
ddd=loc.get("ddd")

if endereco:
    print(f"\nEndereço > {endereco}")
if bairro:
    print(f"Bairro > {bairro}")
if cidade:
    print(f"Cidade > {cidade}")
if estado:
    print(f"Estado > {estado}")
if ddd:
    print(f"DDD > {ddd}")
