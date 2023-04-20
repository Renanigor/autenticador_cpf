from autenticador import app
from flask import render_template, request, redirect, url_for
from testes import formata_cpf, valida_cpf

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    cpf = request.form.get('cpf')
    if cpf is not None:
        cpf_formatado = formata_cpf(cpf)
        cpf_validado = valida_cpf(cpf)
        return render_template('template.html', cpf_formatado=cpf_formatado, cpf_validado=cpf_validado)
    else:
        return redirect(url_for('index'))
