from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')
  
@app.route('/<data>')
def calcula_signo(data):
    lista_perso = [
        'Arthur Shelby Jr.', 'Michael Gray', 'Oswald Mosley', 'Lizzie Shelby ', 'John Shelby', 'Linda Shelby',
        'Thomas Shelby', 'Ada Shelby', 'Polly Gray', 'Finn Shelby', 'Isiah', 'Grace Shelby',
        'Arthur Shelby Jr.'
    ]

    lista_datas = [
        120, 219, 321, 421, 521, 621, 723, 823, 923, 1023, 1122, 1222, 1231
    ]

    periodo = int(data[3:5] + data[:2])

    for i in lista_datas:
        if i > periodo:
            persos = lista_perso[lista_datas.index(i)]
            break
    return jsonify({'Voce e': persos})


app.run(host='0.0.0.0')