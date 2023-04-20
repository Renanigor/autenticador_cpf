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

