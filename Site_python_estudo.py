from flask import Flask

app = Flask(__name__)

#criar a primeira pagina
#route -> Estudos.com/
#função -> O que você quer exibir naquela página
@app.route("/")
def homepage():
    return "Esse é o meu primeiro site. Cassio vc vai ser progranmador python."

@app.route("/contatos")
def contatos():
    return "<p>Nosso contatos são:</p> <p>E-mail: pythonimpressionador@gmail.com</p> e <p>Telefone: (31)99999999</p>"

# colocar no ar
if __name__ == "__main__":
    app.run(debug=True)