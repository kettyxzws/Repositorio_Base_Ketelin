from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "testando flask"

@app.route('/soma/<int:n1>/<int:n2>')
def calculadora(n1,n2):
    resultado = n1+n2
    return f'resultado da soma é´: {resultado}'

@app.route('/bemvindo/<name>')
def bemvindo(name):















@app.route('/bemvindo/<nome>')
def bemvindo(nome):
    return f"Bem-vindo, {nome}"






if __name__ == "__main__":
    app.run(debug=True)