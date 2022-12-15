from controller import *
import os
import time

#variáveis temporárias
lista_presentes = []
numero_presente = 0
    
#While True inicial
while True:  #loop que só e quebrado quando é escolhida a opção 1 ou 2
    os.system("cls")
    print("""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


        Bem vindo ao casamento de Tomás e Jeremias!
            Por favor, selecione o seu estatuto

            1. Noivo/a          2. Convidado/a

                         3. Sair

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """)

    opcao_casamento = int(input("Introduza a sua opção: "))
    
    ############# MENU DE NOIVOS #############

    if opcao_casamento == 1:
        while True:  #loop que só e quebrado quando é escrito as palavras "clc", "elc" e "v"
            os.system("cls")
            print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

                Menu de Noivos
        
    [CLC] - Criar lista de casamento
    [VLC] - Ver lista de casamento
    [ELC] - Eliminar elemento da lista de casamento
    [V] - Voltar atrás
                

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-        
    """)
            opcao_noivos = str(input("Digite a sua opção: ")).lower()
            
            if opcao_noivos == "clc": #criar lista de casamento
                if len(lista_presentes) == 0:  #caso a lista estiver vazia [], continuar
                    tamanho_lista = int(input("Introduza o numero de presentes a colocar na lista: "))
                    for i in range(tamanho_lista):  #iteração ate o numero de presentes a adicionar a lista
                        numero_presente = numeracao_presente(numero_presente)
                        
                        while True:  #loop que só é quebrado caso o presente nao estiver dentro da lista de presentes
                            presentes_adicionar = str(input(f"Introduza o presente nº{numero_presente}: "))
                            if presentes_adicionar not in lista_presentes:  #se o presente não estiver na lista de casamento
                                lista_presentes_final = criar_lista_presentes(presentes_adicionar, lista_presentes)
                                break
                            else:
                                print("Este presente já se encontra dentro da lista!")
                else:  #caso a lista estiver com presentes, nao permite que se crie uma nova lista  
                    print("Já existe uma lista de presentes criada!")
                    opcao_lista_criada = input("Clique Enter para retroceder...")

            elif opcao_noivos == "vlc":  #visualizar lista de casamento
                print(f"Esta é a lista de presentes: {lista_presentes}")
                opcao_ver_lista = input("Clique Enter para retroceder...")
            
            elif opcao_noivos == "elc":  #eliminar elemento da lista de casamento
                while True:  #loop que só é quebrado quando o presente a eliminar está presente na lista
                    presente_eliminar = str(input("Introduza o presente que deseja eliminar: "))
                    if presente_eliminar in lista_presentes:   # se o presente estiver na lista de casamento
                        lista_presente_eliminado = eliminar_presente(presente_eliminar, lista_presentes)
                        print(f"Presente eliminado com sucesso!, a lista de presentes atualizada é: {lista_presentes}")

                        while True:  #loop que só é quebrado quando são escolhidas as opçoes 1 ou 2
                            print("Deseja eliminar outro presente?\n1. Sim    2. Não")
                            opcao_eliminar = int(input("Introduza a sua opção: "))
                            if opcao_eliminar == 1:
                                break
                            elif opcao_eliminar == 2:
                                break
                            else:
                                print("Opção inválida!")
                        
                        if opcao_eliminar == 2:  #segundo break para voltar ao menu de noivos
                            break
                        else:
                            continue
                    else:
                        print("O presente não se encontra na lista!")
                        input("Clique Enter para eliminar outro presente...")
                        
            elif opcao_noivos == "v":
                break
            else:
                print("Opção inválida!")
                
    ############# MENU DE CONVIDADOS #############

    elif opcao_casamento == 2:
        while True:  #loop que só e quebrado quando é escrito as palavras "vlc", "sp" e "v"
            os.system("cls")
            print("""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


                    Menu de Convidados
            
        [VLC] - Ver lista de presentes de casamento
        [SP] - Seleção do presente a comprar
        [V] - Voltar atrás


    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-        
        """)
            opcao_convidados = str(input("Digite a sua opção: ")).lower()

            if opcao_convidados == "vlc": #visualizar lista de casamento
                print(f"Esta é a lista de presentes: {lista_presentes}")
                opcao_ver_lista = input("Clique Enter para retroceder...")
            
            elif opcao_convidados == "sp": #seleção do presente a comprar
                numero_presente = 0 #voltar a definir a variavel para nao usar o valor armazenado da criação da lista de casamento
                
                if len(lista_presentes) != 0:  #se a lista conter presentes, continuar
                    while True:  #loop que é quebrado quando o numero de presentes a comprar são menores ou iguais ao numero de presentes dentro da lista  
                        numero_presentes_comprar = int(input("Introduza o numero de presentes que deseja comprar: "))
                        if numero_presentes_comprar <= len(lista_presentes): #se o numero de presentes a comprar são menores que o numero de presentes dentro da lista
                            for i in range(numero_presentes_comprar): #iterar o numero de presentes, para perguntar quais sao
                                numero_presente = numeracao_presente(numero_presente)
                                
                                while True: #loop que so é quebrado quando o presente a comprar esta na lista de presentes
                                    presente_comprar = str(input(f"Introduza o presente nº{numero_presente}: "))
                                    if presente_comprar in lista_presentes: #se o presente esta dentro da lista de presentes
                                        resultado_presentes_comprar = eliminar_presente(presente_comprar, lista_presentes)
                                        break
                                    else:
                                        print("Este presente não se encontra dentro da lista!")
                            
                            print(f"Presente/s comprado/s com sucesso!, a lista de presentes atualizada é: {lista_presentes}")
                            opcao_comprar = input("Clique Enter para retroceder...")
                            break
                        else:
                            print("O número de presentes que deseja comprar é maior que os número de presentes dentro da lista")
                else:
                    print("Não existem presente para comprar")
                    opcao_lista_criada = input("Clique Enter para retroceder...")
                    
            elif opcao_convidados == "v": #break do menu de convidados
                break
    
    elif opcao_casamento == 3: #sair totalmente
        break
    else:
        print("Opção Inválida!")
        


