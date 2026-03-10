from flask import Flask, render_template, request, redirect
from urllib.parse import quote
import os

app = Flask(__name__,template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/servico", methods=["POST"])
def servico():

    servico = request.form.get("servico")
    problema = request.form.get("mensagem", "").strip()
    nome = request.form.get("nome", "").strip()
    endereco = request.form.get("endereco", "").strip()

    # print("FORM RECEBIDO:", request.form)

    if not servico:
        return redirect("/")
    
    numero = "5561992049123"
    
    if problema:
        texto = f"Olá, me chamo {nome} e preciso de um serviço de {servico}.\n\nProblema: {problema}. Este é o meu endereço {endereco}."
    else:
        texto = f"Olá, me chamo {nome} e preciso de um serviço de {servico}. Este é o meu endereço {endereco}."
    
    mensagem = quote(texto)

    url = f"https://wa.me/{numero}?text={mensagem}"

    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True)