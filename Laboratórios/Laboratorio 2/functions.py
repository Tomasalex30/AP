def juntar_nomes (nome1, nome2):
    juntar = (nome1 + nome2)
    return juntar

def juntar_tudo (palavra):
    resultado = palavra.upper() + str(len(palavra))     #dar o valor de string, pois len é considerado como um número inteiro  
    return resultado

def calcular_salario_total (salario, comissoes):
    resultado_total = int(salario) + (int(comissoes)*500) 
    return resultado_total