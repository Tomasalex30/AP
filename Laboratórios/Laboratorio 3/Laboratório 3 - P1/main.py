import re
from functions import *

if __name__ == '__main__':

    while True:
        print("""
            Qual o exercicio que deseja ver?
            1- Exercicio 1
            2- Exercicio 2
            3- Exercicio 3
            4- Exercicio 4
            5- Nenhum
            """)
        
        opcao = int(input("Insira a opção: "))

        ################Exercicio 1#####################
        if opcao == 1:
            numero_aleatorio = comparacao_numero()
            if numero_aleatorio == True:
                print(f"O númmero é maior que 10 ")
            else:
                print(f"O número é menor ou igual a 10")

            print(""" 
            Deseja ver outro exercicio?
            1. Sim
            2. Não
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")

        ###############################################
        ################Exercicio 2#####################
        elif opcao == 2:
            palavra_substituir = input("Digite uma palavra: ").lower()
            resultado_substituicao = substituir_letras(palavra_substituir)
            print(f"A palavra substituida é {resultado_substituicao}")
        
            print(""" 
            Deseja ver outro exercicio?
            1. Sim
            2. Não
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")

        ###############################################
        ################Exercicio 3#####################
        elif opcao == 3:
            numero1 = 1
            resultado1 = arredondar_numero(numero1)
            print(f"O resultado é: {resultado1}")
                                                    
            numero2 = 2.5
            resultado2 = arredondar_numero(numero2)
            print(f"O resultado é: {(resultado2)}")

            print(""" 
            Deseja ver outro exercicio?
            1. Sim
            2. Não
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")
        
        ###############################################
        ################Exercicio 4#####################
        elif opcao == 4:
            palavra = input("Insira a palavra mágica: ").lower()
            resultado_emoji = devolver_codigo_emoji(palavra)
            if type(resultado_emoji) == str:                        
                print(f"O jeremias está: {resultado_emoji}")

            print(""" 
            Deseja ver outro exercicio?
            1. Sim
            2. Não
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")

        ###############################################
        elif opcao == 5:
            break
        else:
            print("Opção inválida")