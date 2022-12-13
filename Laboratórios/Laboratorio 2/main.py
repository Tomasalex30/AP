from functions import *

if __name__ == '__main__':
    #########Exercício 1##############
    
    palavra = input("Digite uma palavra: ")
    print (f"A sua palavra tem {len(palavra)} caracteres.")
    
    ######################################
    #########Exercício 2##################

    palavra = input("Digite uma palavra: ")
    palavra_minuscula = palavra.lower()
    print(f"A sua palavra em minusculas é: {palavra_minuscula}")

    ######################################
    #########Exercício 3##################

    nome1 = "Porto" 
    nome2 = "Lisboa"
    resultado = juntar_nomes(nome1, nome2)
    print(f"A junção das palavras é: {resultado}")

    ######################################
    #########Exercício 4##################

    palavra = "Programar"
    resultado = juntar_tudo(palavra)
    print(f"A junção da palavra em maiuscula e o seu número de caracteres é: {resultado}")


    ######################################
    #########Exercício 5##################

    salario = input("Qual é o seu salario? ")
    comissoes = input("Quantas comissoes fez este mês? ")
    resultado_total = calcular_salario_total(salario, comissoes)
    print(f"O seu salário total é: {resultado_total}")

    ######################################