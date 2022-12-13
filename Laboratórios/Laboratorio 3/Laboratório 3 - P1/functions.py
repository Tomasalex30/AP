import random
import emoji

def comparacao_numero():
    numero = random.randint(1, 101)
    if numero > 10:
        return True
    else:
        return False

def substituir_letras(palavra):
    palavra_substituir = palavra.replace("a", "x")
    return palavra_substituir

def arredondar_numero(numero):
    if type(numero) == float:
        numero_arredondado = round(numero)
        return numero_arredondado
    else:
        return False

def devolver_codigo_emoji (palavra):
    if palavra == "feliz":
        return "\U0001F600"
    else:
        return "\U0001F610"