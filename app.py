from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_ENDPOINT = "http://ip-api.com/json/{query}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    query = request.form.get("query", "").strip()

    if not query:
        return render_template("index.html", erro="Você precisa informar um IP ou Domínio!")

    # Faz a requisição para a API corretamente
    response = requests.get(API_ENDPOINT.format(query=query))

    if response.status_code == 200:
        dados = response.json()
        
        # Verifica se a API retornou sucesso
        if dados.get("status") == "fail":
            return render_template("index.html", erro="Consulta inválida! Verifique o IP ou Domínio.")

        return render_template("index.html", query=query, dados=dados)

    return render_template("index.html", erro="Erro ao conectar com a API!")

if __name__ == "__main__":
    app.run(debug=True)