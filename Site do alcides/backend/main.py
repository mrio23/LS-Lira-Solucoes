import webbrowser
from abc import ABC, abstractmethod
import os

os.system('cls')

class servico(ABC):

    def __init__ (self, nome):
        self.nome = nome


    @abstractmethod
    def executar(self):
        pass



class servicoReparos(servico):

    def executar(self):
        numero = "5561992049123"
        mensagem = "Olá, preciso de um serviço de reparos"
        url = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
        webbrowser.open(url)


class servicoReforma(servico):

    def executar (self):
        numero = "5561992049123"
        mensagem = "Olá, preciso de um serviço de reforma"
        url = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
        webbrowser.open(url)

class servicoHidraulica(servico):

    def executar (self):
        numero = "5561992049123"
        mensagem = "Olá, preciso de um serviço de hidráulica"
        url = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
        webbrowser.open(url)

class servicoManuntencao(servico):

    def executar (self):
        numero = "5561992049123"
        mensagem = "Olá, preciso de um serviço de manutenção"
        url = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
        webbrowser.open(url)

class servicoPintura(servico):

    def executar (self):
        numero = "5561992049123"
        mensagem = "Olá, preciso de um serviço de pintura"
        url = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
        webbrowser.open(url)

class servicoDecoracao(servico):

    def executar (self):
        numero = "5561992049123"
        mensagem = "Olá, preciso de um serviço de decoração"
        url = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
        webbrowser.open(url)

class servicoEletrica(servico):

    def executar (self):
        numero = "5561992049123"
        mensagem = "Olá, preciso de um serviço de elétrica"
        url = f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"
        webbrowser.open(url)

def main ():
    seletorDeOpcoes = input("Digite o serviço desejado: ").strip().lower()

    servicos = {
        "reparo": servicoReparos,
        "reforma": servicoReforma,
        "hidraulica": servicoHidraulica,
        "pintura": servicoPintura,
        "decoracao": servicoDecoracao,
        "manutencao": servicoManuntencao,
        "eletrica": servicoEletrica
    }

    if seletorDeOpcoes in servicos:
        print(f"Redirecionando ao chat... ({seletorDeOpcoes.capitalize()})")
        servico = servicos[seletorDeOpcoes](seletorDeOpcoes)
        servico.executar()

    else:
        print("Serviço inválido.")

if __name__ == "__main__":
    main()