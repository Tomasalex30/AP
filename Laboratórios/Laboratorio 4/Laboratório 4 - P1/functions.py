######################### Exercicio 1.a #########################

def exercicio_1a (lista_1, lista_2):
    if len(lista_1) == len(lista_2):
        return True
    else:
        return False

######################### Exercicio 1.b #########################

def exercicio_1b (lista_1, lista_temp): 
    for i in range(len(lista_1)):
        if lista_1.count(lista_1[i]) > 1 and lista_1[i] not in lista_temp:
            lista_temp.append(lista_1[i])
    return lista_temp

######################### Exercicio 1.c #########################

def exercicio_1c (lista_1):
    soma = lista_1[0] + lista_1[-1] 
    return soma          

######################### Exercicio 1.d ######################### 
        
def exercicio_1d (lista_1, lista_2, lista_temp):
    if len(lista_1) <= len(lista_2):
        for i in range(0, len(lista_1)):
            lista_temp.append(lista_1[i] + lista_2[i])
    else:
        for i in range(0, len(lista_2)):
            lista_temp.append(lista_1[i] + lista_2[i])
    return lista_temp
    
######################### Exercicio 1.e #########################

def exercicio_1e (lista_1, lista_temp):
    for i in range(len(lista_1)):
        if type(lista_1[i]) == str:
            lista_temp.append(lista_1[i])
    return lista_temp

######################### Exercicio 1.f #########################

def exercicio_1f (lista_1, lista_temp):
    a = 0
    for i in range(len(lista_1)):
        if type(lista_1[i]) == int:
            lista_temp.append(lista_1[i])
            a += lista_1[i]
    media = (a/len(lista_temp))
    return media

######################### Exercicio 1.g #########################

def exercicio_1g (lista_1, lista_temp):
    for i in range(len(lista_1)):
        if type(lista_1[i]) == float:
            lista_1[i] = round(lista_1[i])
            lista_temp.append(lista_1[i])
    return lista_temp

    
      
            


