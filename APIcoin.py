from requests import get
import json
class conversor():
    def __init__(self,ft,sn,unidade):
        self.dados = None
        self.unidade=unidade
        self.ft=ft
        self.sn=sn
        self.url=f"https://economia.awesomeapi.com.br/last/{self.ft}-{self.sn}"

    def money(self):
        resposta=get(self.url)
        dados=resposta.json()
        self.dados=dados

        r = self.unidade * float(dados.get(f"{self.ft}{self.sn}").get("high"))
        return r
    def data(self):
        return self.dados.get(f"{self.ft}{self.sn}").get("create_date")

moeda1=input("Conversor de moedas, escolha a moeda atual (BRL, EUR, USD, BTC): ").upper()
valor=int(input("Qual é o valor que deve ser convertido: "))
moeda2=input("A outra moeda de conversão (BRL, EUR, USD, BTC): ").upper()
resultado = conversor(moeda1,moeda2,valor)
print(f"\nA conversão do {moeda1} para {moeda2} fica no valor de",end=' ')
if moeda2=="BRL":
    print(f"R$ {resultado.money():.2f}")
elif moeda2=="EUR":
    print(f"€$ {resultado.money():.2f}")
elif moeda2=="USD":
    print(f"$ {resultado.money():.2f}")
elif moeda2=="BTC":
    print(f"{resultado.money()} BTC")
print(f"Na data de {resultado.data()}")
