from functions import *
import os
import time
if __name__ == "__main__":

    while True:
        os.system("cls")
        print("""
            Qual o exercicio que deseja ver?
                    1- Exercicio 1.a
                    2- Exercicio 1.b
                    3- Exercicio 1.c
                    4- Exercicio 1.d
                    5- Exercicio 1.e
                    6- Exercicio 1.f
                    7- Exercicio 1.g
                    8- Exercicio 2
                    9- Nenhum
            """)
        
        opcao_1 = int(input("Insira a opção: "))
######################## Exercicio 1.a #########################

        os.system("cls")
        if opcao_1 == 1:
            lista_1 = [1, 2, 3]
            lista_2 = ["a", 1, 2]
            resultado = exercicio_1a(lista_1, lista_2)
            if resultado == True:
                print(f"Resultado: A lista {lista_1} e {lista_2} têm o mesmo tamanho")
            else:
                print(f"Resultado: A lista {lista_1} e {lista_2} não tem o mesmo tamanho")

            print(""" 
            Deseja ver outro exercicio?
                    1. Sim
                    2. Não
            """)
        
            opcao_2 = int(input("Introduza a sua opção: "))
            if opcao_2 == 1:
                continue
            elif opcao_2 == 2:
                break
            else: 
                print("Opção Inválida")

######################### Exercicio 1.b #########################
        
        elif opcao_1 == 2:
            os.system("cls")
            lista_temp = [] #lista temporária
            lista_1 = [1, 2, 2, 4, 1, 5, 5]
            resultado = exercicio_1b(lista_1, lista_temp)   # O porque de dar None
            print(f"Resultado: A lista é: {lista_temp}")

            print(""" 
            Deseja ver outro exercicio?
                    1. Sim
                    2. Não
            """)
        
            opcao_2 = int(input("Introduza a sua opção: "))
            if opcao_2 == 1:
                continue
            elif opcao_2 == 2:
                break
            else: 
                print("Opção Inválida")

######################### Exercicio 1.c #########################
        
        elif opcao_1 == 3:
            os.system("cls")
            lista_1 = [1, 3, "a", 2.0]
            resultado = exercicio_1c(lista_1)
            print(f"Resultado: A soma de {lista_1[0]} com {lista_1[-1]} é: {resultado}")

            print(""" 
            Deseja ver outro exercicio?
                    1. Sim
                    2. Não
            """)
        
            opcao_2 = int(input("Introduza a sua opção: "))
            if opcao_2 == 1:
                continue
            elif opcao_2 == 2:
                break
            else: 
                print("Opção Inválida")

######################### Exercicio 1.d #########################
       
        elif opcao_1 == 4:
            os.system("cls")
            lista_1 = [1, 2.0, 3, 5, 10.1, 11, 12]
            lista_2 = [2, 3, 4.3, 5, 6]
            lista_temp = []
            resultado = exercicio_1d(lista_1, lista_2, lista_temp)
            print(f"Resultado: A lista é: {lista_temp}")

            print(""" 
            Deseja ver outro exercicio?
                    1. Sim
                    2. Não
            """)
        
            opcao_2 = int(input("Introduza a sua opção: "))
            if opcao_2 == 1:
                continue
            elif opcao_2 == 2:
                break
            else: 
                print("Opção Inválida")

######################### Exercicio 1.e #########################
        
        elif opcao_1 == 5:
            os.system("cls")
            lista_1 = [1, "a", 2, 3, 5, "b"]
            lista_temp = []
            resultado = exercicio_1e(lista_1, lista_temp)
            print(f"Resultado: A lista é: {lista_temp}")

            print(""" 
            Deseja ver outro exercicio?
                    1. Sim
                    2. Não
            """)
        
            opcao_2 = int(input("Introduza a sua opção: "))
            if opcao_2 == 1:
                continue
            elif opcao_2 == 2:
                break
            else: 
                print("Opção Inválida")

######################### Exercicio 1.f #########################
        
        elif opcao_1 == 6:
            os.system("cls")
            lista_1 = [1, 2, 2.0, 3, 5.0, 6, 9]
            lista_temp = []
            resultado = exercicio_1f(lista_1, lista_temp)
            resultado_arredondado = int(resultado)
            print(f"Resultado: A média de todos os valores inteiros da lista é: {resultado}, se for arredondado é: {resultado_arredondado}")

            print(""" 
            Deseja ver outro exercicio?
                    1. Sim
                    2. Não
            """)
        
            opcao_2 = int(input("Introduza a sua opção: "))
            if opcao_2 == 1:
                continue
            elif opcao_2 == 2:
                break
            else: 
                print("Opção Inválida")

######################### Exercicio 1.g #########################
        
        elif opcao_1 == 7:
            os.system("cls")
            lista_1 = [1.0, 2.7, 3, 4, 5.6, 7, 8.0]
            lista_temp = []
            resultado = exercicio_1g(lista_1, lista_temp)
            print(f"Resultado: A lista é: {lista_temp}")
        
            print(""" 
            Deseja ver outro exercicio?
                    1. Sim
                    2. Não
            """)
        
            opcao_2 = int(input("Introduza a sua opção: "))
            if opcao_2 == 1:
                continue
            elif opcao_2 == 2:
                break
            else: 
                print("Opção Inválida")

######################### Exercicio 2 #########################        
            
        elif opcao_1 == 8:
            os.system("cls")
            
            print("""
                Bem vindo ao Portal de Candidaturas da Empresa SemNome!
                                
                                    Deseja continuar?
                                        1- Sim
                                        2- Não
                """)
            
            #loop que só é quebrado quando o utilizador escolher a opção 2
            while True:
                opcao_2 = int(input("Introduza a sua opção: "))
                if opcao_2 == 1:
                    os.system("cls")
                    print("""
                        Muito bem! Agora iremos fazer algumas perguntas acerca de si, para verificarmos se está ou não apto para se candidatar à vaga na nossa empresa.
                                                                    Para continuar, digite no terminal a palavra "CV".
                        """)
                    
                    #loop que só é quebrado quando o utilizador escrever a palavra "cv"
                    while True:
                        opcao_3 = input("Introduza a palavra ""CV"": ").lower()
                        if opcao_3 == "cv":
                            break
                        else:
                            print("A palavra introduzida não está correta!")
                            continue

                    os.system("cls")
                    print("""
                        Primeira Pergunta: Qual a sua idade?
                        """)    

                    pergunta_1 = int(input("Introduza a sua idade: "))
                    
                    os.system("cls")
                    print("""
                        Segunda Pergunta: Qual é o seu grau de conhecimento em Inglês? 

                                            A1 - Iniciante
                                            A2 - Iniciante Avançado
                                            B1 - Intermédio
                                            B2 - Intermédio Avançado
                                            C1 - Avançado
                                            C2 - Fluente
                    """)

                    #loop que só e quebrado quando o utilizador escrever um dos graus de ingles
                    while True:
                        pergunta_2 = input("Introduza o seu grau em Inglês: ").lower()
                        if pergunta_2 == "a1" or pergunta_2 == "a2" or pergunta_2 == "b1" or pergunta_2 == "b2" or pergunta_2 == "c1" or pergunta_2 == "c2":
                            break
                        else:
                            print("O grau introduzido está incorreto!")
                            continue
                    
                    os.system("cls")
                    print("""
                        Terceira Pergunta: Apresenta um grau Intermédio de conhecimento em Python?
                                                        
                                                    1- Sim
                                                    2- Não
                        """)
                    
                    #loop que só é quebrado quando o utilizador escolher a opção 1 ou 2
                    while True:
                        pergunta_3 = int(input("Introduza a opção: "))
                        if pergunta_3 == 1 or pergunta_3 == 2:
                            break
                        else:
                            print("A opção introduzida está incorreta!")
                            continue

                    #três condições que servem para verificar se o utilizador está apto para se candidatar a vaga do em,prego
                    #apenas está apto se ele satisfazer as três condições
                    if 25 <= pergunta_1 <= 45:
                        if pergunta_2 == "b1" or pergunta_2 == "b2" or pergunta_2 == "c1" or pergunta_2 == "c2":
                            if pergunta_3 == 1 or pergunta_3 == 2:
                                os.system("cls")
                                print("""
                                    Iremos processar o seu resultado.
                                    """)
                                for i in range(0, 101, 10):
                                    print(f"""
                                                    {i}%
                                    """)
                                    time.sleep(0.5)
                                print("""
                                        Pode candidatar-se à vaga.
                                          Obrigado, volte sempre!
                                    """)
                                break
                            else:
                                os.system("cls")
                                print("""
                                    Iremos processar o seu resultado.
                                    """)
                                for i in range(0, 101, 10):
                                    print(f"""
                                                    {i}%
                                    """)
                                    time.sleep(0.5)
                                print("""
                                        Não possui os requisitos necessários
                                            para se candidatar a esta vaga.
                                                Obrigado, volte sempre!
                                    """)
                                break
                        else:
                            os.system("cls")
                            #mini processamento usando um loop e a função time para abrandar o print
                            print("""
                                Iremos processar o seu resultado.
                                """)
                            for i in range(0, 101, 10):
                                print(f"""
                                                {i}%
                                """)
                                time.sleep(0.5)
                            print("""
                                    Não possui os requisitos necessários
                                        para se candidatar a esta vaga.
                                            Obrigado, volte sempre!
                                """)
                            break
                    else:
                        os.system("cls")
                        print("""
                            Iremos processar o seu resultado.
                            """)
                        for i in range(0, 101, 10):
                            print(f"""
                                            {i}%
                            """)
                            time.sleep(0.5)
                        print("""
                                Não possui os requisitos necessários
                                    para se candidatar a esta vaga.
                                        Obrigado, volte sempre!
                            """)
                        break
                
                elif opcao_2 == 2:
                    break
                else: 
                    print("Opção Inválida")
                    continue

            print(""" 
                Deseja ver outro exercicio?
                        1. Sim
                        2. Não
                """)
        
            opcao_4 = int(input("Introduza a sua opção: "))
            if opcao_4 == 1:
                continue
            elif opcao_4 == 2:
                break
            else: 
                print("Opção Inválida")

        elif opcao_1 == 9:
            break
        else:
            print("Opção inválida")   


   




        

