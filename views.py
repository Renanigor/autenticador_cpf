from autenticador import app
from flask import render_template, request, redirect, url_for
from testes import formata_cpf, valida_cpf, formata_cnpj, valida_cnpj

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    cpf = request.form.get('cpf')
    cnpj = request.form.get('cnpj')
    
    if cpf or cnpj:
        cpf_formatado = formata_cpf(cpf) if cpf else None
        cpf_validado = valida_cpf(cpf) if cpf else None
        
        cnpj_formatado = formata_cnpj(cnpj) if cnpj else None
        cnpj_validado = valida_cnpj(cnpj) if cnpj else None


        return render_template('template.html', cpf_formatado=cpf_formatado, cpf_validado=cpf_validado, cnpj_formatado=cnpj_formatado, cnpj_validado=cnpj_validado)
    else:
        return redirect(url_for('index'))

