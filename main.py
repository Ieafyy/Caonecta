from flask import Flask, render_template, request
import datetime
from dados import petshops
from funcs import formatar, comparar_petshops

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route('/dataget', methods = ['GET', 'POST'])
def data_sender():
    if request.method == 'POST':

        infos = formatar(request.get_data())

        a, m, d = infos['dt'].split('-')
        dsemana = datetime.date(int(a), int(m), int(d)).weekday()
        dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        
        ncg = int(infos['ncg'])
        ncp = int(infos['ncp'])

        if dsemana >= 5:
            for petshop in petshops:
                valor = (petshops[petshop]['fim_de_semana_pequeno'] * ncp + petshops[petshop]['fim_de_semana_grande'] * ncg)
                petshops[petshop]['valor_dia'] = valor
            
        else: 
            for petshop in petshops:
                valor = (petshops[petshop]['semana_pequeno'] * ncp + petshops[petshop]['semana_grande'] * ncg)
                petshops[petshop]['valor_dia'] = valor

        
        petshop_final = comparar_petshops(petshops)




        for petshop in petshops:
            if petshop == petshop_final:
                petshops[petshop]['escolhido'] = 'SIM'
                petshops[petshop]['dia_semana'] = dias[dsemana]
            else:
                petshops[petshop]['escolhido'] = 'NAO'

        return petshops

app.run()