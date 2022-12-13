from functions import *
if __name__ == '__main__':
 
    while True:
        print("""
            1. Somar dois números
            2. Multiplicar dois números
            3. Comparar números
            4. Verificar igualdade
            5. Retornar o maior de dois números
            6. Retornar o menor de dois números
            7. Super jogo 
            8. Sair
            """)        

        opcao = int(input("Introduza a sua opção? "))
       
        if opcao == 1:
            a = float(input("Introduza o primeiro numero: "))
            b = float(input("Introduza o segundo numero: "))    
            resultado = somar_numeros(a,b)
            print(f"O resultado da soma de {a} com {b} é: {resultado}")
        
            print(""" 
            Continuar?
            1. Voltar ao Menu
            2. Sair da Calculadora
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida") 


        elif opcao == 2:
            a = float(input("Introduza o primeiro numero: "))
            b = float(input("Introduza o segundo numero: "))    
            resultado = multiplicar_numeros(a,b)
            print(f"O resultado da multiplicação de {a} com {b} é: {resultado}")

            print(""" 
            Continuar?
            1. Voltar ao Menu
            2. Sair da Calculadora
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")

        elif opcao == 3:
            a = float(input("Introduza o primeiro numero: "))
            b = float(input("Introduza o segundo numero: "))    
            resultado = comparar_numeros(a,b)

            if resultado == 1:
                print(f"O número {a} é maior que o número {b}")
            elif resultado == 2:
                print(f"O número {a} é menor que o número {b}")
            else:
                print(f"O número {a} é igual ao número {b}")

            print(""" 
            Continuar?
            1. Voltar ao Menu
            2. Sair da Calculadora
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")           
    
        elif opcao == 4:
            a = float(input("Introduza o primeiro numero: "))
            b = float(input("Introduza o segundo numero: "))    
            resultado = verificar_igualdade(a,b)
            
            if resultado == False:
                print("Incorreto! os números são diferentes!")
            else:
                print(f"Os números {a} e {b} são iguais")

            print(""" 
            Continuar?
            1. Voltar ao Menu
            2. Sair da Calculadora
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")

        elif opcao == 5:
            a = float(input("Introduza o primeiro numero: "))
            b = float(input("Introduza o segundo numero: "))    
            resultado = retornar_maior_de_dois(a,b)
            
            if resultado == False:
                print("Incorreto! os números são iguais!")
            else:
                print(f"O maior número é: {resultado}")

            
            print(""" 
            Continuar?
            1. Voltar ao Menu
            2. Sair da Calculadora
            """)
        
            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")

        elif opcao == 6:
            a = float(input("Introduza o primeiro numero: "))
            b = float(input("Introduza o segundo numero: "))    
            resultado = retornar_menor_de_dois(a,b)
        
            if resultado == False:
                print("Incorreto! os números são iguais!")
            else:
                print(f"O menor número é: {resultado}")
            
            print(""" 
            Continuar?
            1. Voltar ao Menu
            2. Sair da Calculadora
            """)

            opcao2 = int(input("Introduza a sua opção: "))

            if opcao2 == 1:
                continue
            elif opcao2 == 2:
                break
            else: 
                print("Opção Inválida")

        elif opcao == 7:
            print ("""
            Bem vindo ao super jogo!
            O jogo consiste em uma disputa de números com o computador.
            O jogador tem que digitar um número de 0 a 5 e o computador vai gerar um número aleatório entre 0 e 5.
            Se o número digitado pelo jogador for em relação ao número gerado pelo computador:
                Igual: Vitória
                Diferente: Derrota

            Selecione uma opção:
            1. Jogar
            2. Voltar ao menu
            """)

            opcao2 = int(input("Introduza a sua opção: "))
            if opcao2 == 1:
                while True:
                    a = int(input("Introduza o seu número de 0 a 5: "))
                    b = random.randint(0,5)

                    if a > 5:
                        print("""
                        Numero Inválido!

                        Tentar novamente?
                        1. Sim
                        2. Voltar ao menu 
                        """)

                        opcao3 = int(input("Introduza a sua opção: "))
                        if opcao3 == 1:
                            continue
                        elif opcao3 == 2:
                            break
                        else: 
                            print("Opção Inválida")

                    resultado = super_jogo(a,b)
                    if resultado == 1:
                        print(f"Vitória! O número do computador era {b}")
                    else:
                        print(f"Derrota! O número do computador era {b}")
                    
                    print("""
                    Queres jogar denovo?
                    1. Sim
                    2. Voltar ao menu
                    """)

                    opcao4 = int(input("Selecione a sua opção: ")) 
                    if opcao4 == 1:
                        continue
                    elif opcao4 == 2:
                        break
                    else: 
                        print("Opção Inválida")
 
            elif opcao2 == 2:
                continue
            else:
                print("Opção Inválida")
             
        elif opcao == 8:
            print("Obrigado por usar a super calculadora!")
            break
        else:
            print("Opção inválida!")