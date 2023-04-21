#TESTES

def formata_cpf(num):
    parte_01 = num[0:3]
    parte_02 = num[3:6]
    parte_03 = num[6:9]
    parte_04 = num[9:12]

    return f'{parte_01}.{parte_02}.{parte_03}-{parte_04}'



def valida_cpf(cpf):
    if len(set(cpf)) == 1:
        return 'NÃO'

    num = cpf[0:9]
    soma = 0
    peso = 10
    for i in range(0, 9):
        soma += int(num[i]) * peso
        peso -= 1
    soma *= 10
    digito_01 = soma % 11 
    if digito_01 > 9:
        digito_01 = 0

    num_com_1_digito = f'{num}{digito_01}'
    soma_2 = 0
    peso_2 = 11
    for i in range (0, 10):
        soma_2 += int(num_com_1_digito[i]) * peso_2
        peso_2 -= 1
    soma_2 *= 10 
    digito_02 = (soma_2 % 11)
    if digito_02 > 9:
        digito_02 = 0

    cpf_valido = f'{num}{digito_01}{digito_02}'
    if cpf == cpf_valido:
        return 'SIM'
    else: 
        return 'NÃO'

def formata_cnpj(cnpj):
    parte_01 = cnpj[0:2]
    parte_02 = cnpj[2:5]
    parte_03 = cnpj[5:8]
    parte_04 = cnpj[8:12]
    parte_05 = cnpj[12:15]

    return f'{parte_01}.{parte_02}.{parte_03}/{parte_04}-{parte_05}'



def valida_cnpj(cnpj):
    if len(set(cnpj)) == 1:
        return 'CNPJ INVÁLIDO'
    peso = '543298765432'
    base = cnpj[0:12]
    soma = 0
    i = 0
    for numero in base:
        soma += int(numero) * int(peso[i])
        i += 1
    digito_01 = 11 - (soma % 11)

    if digito_01 >= 10:
        digito_01 = 0

    peso_2 = '6543298765432'
    base_2 = (f'{cnpj[0:12]}{digito_01}')
    soma_2 = 0
    i_2 = 0
    for numero in base_2:
        soma_2 += int(numero) * int(peso_2[i_2])
        i_2 += 1

    digito_02 = 11 - (soma_2 % 11)

    if digito_02 >= 10:
        digito_02 = 0

    cnpj_valido = (f'{base_2}{digito_02}')
    if cnpj == cnpj_valido:
        return 'CNPJ É VÁLIDO'
    else:
        return 'CNPJ É INVÁLIDO'

print(valida_cnpj('1111111111111'))