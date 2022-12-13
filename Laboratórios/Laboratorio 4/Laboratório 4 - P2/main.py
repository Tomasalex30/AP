from functions import*
import os
import random
if __name__ == "__main__":

    ############## Menu do Jogo Inicial ##############
    while True:
        
        #Variáveis temporárias
        d_pve = {} 
        d_pontos_pve = {}
        d_pvp = {}
        d_pontos_pvp = {}
        nome_j2_pve = "Computador"
        pontos_j1 = 0
        pontos_j2 = 0    
        ronda = 0

        os.system("cls")
        print("""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                   
                                                                   
                                                                   
                                                                   
                             Pedra, Papel ou Tesoura                
                                                                   
                                   1. Jogar                         
                                   2. Regras                        
                                   3. Sair                          
                                                            
                                                                   
                                                                   
                                                                   
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
           """)
        opcao_1 = int(input("Introduza a sua opção: "))

        ################# Menu Jogar #################
        
        if opcao_1 == 1:    
            os.system("cls")
            print("""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                                                    
                                                                
                                                                    
                                                                
                            1. Jogador vs Computador               
                            2. Jogador vs Jogador                  
                            3. Voltar ao Menu                      
                                                                
                                                                
                                                                
                                                                
                                                                
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            """)

            
            opcao_jogar = int(input("Introduza a sua opção: "))
            
            ############# Jogador vs Computador #############
            if opcao_jogar == 1:    

                os.system("cls")
                print("""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                            
                                                                
                                                                
                                                                
                                                                
                            Inroduza o seu nome...                
                                                            
                            ___________ vs Computador               
                                                                
                                                                
                                                                
                                                                
                                                                
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

        
                nome_j1_pve = str(input("O seu nome: "))
                
                #função que serve para fazer o registo do jogador1 no dicionário d_pve
                registo_jvj(d_pve, nome_j1_pve, nome_j2_pve)     

                os.system("cls")
                print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                                                
                                                            
                                    Boa sorte!                  
                            E que ganhe o mais forte!              
                                                        
                                                                
                            Jogador 1. {nome_j1_pve}
                                                                
                            Jogador 2. {nome_j2_pve}                        
                        
                                                        
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

                enter = input("Clique enter para continuar...")
                
                #loop para podermos sempre que quisermos jogar novamente
                while True:

                    #função que serve para determinar n+1 rondas
                    ronda = determinar_ronda(ronda)

                    os.system("cls") 
                    print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                                                
                                                            
                                                
                                    Ronda {ronda}
                                                        
                            Jogada de {nome_j1_pve}: __________
                                                                
                            Jogada de {nome_j2_pve}: __________                                  
                                                
                        
                                                        
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)
                    
                    #loop que só é quebrado quando o jogador jogar: pedra, papel ou tesoura
                    while True: 
                        jogada_1_pve = input(f"{nome_j1_pve} introdza a sua jogada: ").lower()

                        if (jogada_1_pve == "pedra") or (jogada_1_pve == "papel") or (jogada_1_pve == "tesoura"):   
                            break
                        else:
                            print("Opção inválida...")
                            continue
                    
                    #jogada do computador, aleatoria usando a função randint
                    jogada_2_pve = random.randint(1,4) 
                    if jogada_2_pve == 1:
                        jogada_pc = str("pedra")
                    elif jogada_2_pve == 2:
                        jogada_pc = str("papel")
                    else: 
                        jogada_pc = str("tesoura")
                    
                    #função que serve para determinar o vencedor
                    resultado_pve = determinar_vencedor(jogada_1_pve,jogada_pc) 
                    
                    #função de atribuição de pontos e posterior adição dentro do d_pontos
                    if (jogada_1_pve == "papel" and jogada_pc == "pedra") or (jogada_1_pve == "pedra" and jogada_pc == "tesoura") or (jogada_1_pve == "tesoura" and jogada_pc == "papel"):
                        pontos_j1 = atribuir_pontos(jogada_1_pve, jogada_pc, d_pontos_pve, nome_j1_pve, nome_j2_pve, pontos_j1, pontos_j2)
                    elif (jogada_1_pve == "pedra" and jogada_pc == "papel") or (jogada_1_pve == "tesoura" and jogada_pc == "pedra") or (jogada_1_pve == "papel" and jogada_pc == "tesoura"):
                        pontos_j2 = atribuir_pontos(jogada_1_pve, jogada_pc, d_pontos_pve, nome_j1_pve, nome_j2_pve, pontos_j1, pontos_j2)        
                    elif (jogada_1_pve == "papel" and jogada_pc == "papel") or (jogada_1_pve == "pedra" and jogada_pc == "pedra") or (jogada_1_pve == "tesoura" and jogada_pc == "tesoura"):
                        pontos_j1, pontos_j2 = atribuir_pontos(jogada_1_pve, jogada_pc, d_pontos_pve, nome_j1_pve, nome_j2_pve, pontos_j1, pontos_j2)                   
                    else:
                        print("Inválido")

                    #caso o jogador 1 vença
                    if resultado_pve == 1:
                        os.system("cls")
                        print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                    Ronda {ronda}
                                                        
                        Jogada de {nome_j1_pve}: {jogada_1_pve}
                                                                
                        Jogada de {nome_j2_pve}: {jogada_pc}                                  
                                                
        
                                    Parabéns!                                 
                               O vencedor é {nome_j1_pve}           
                                    
            1. Jogar Outravez      2. Voltar ao Menu     3. Pontuação                              
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

                        #loop que só é quebrado quando o jogador escolher a opcao 1 ou 2
                        while True:
                            opcao_pve = int(input("Introduza a sua opcão: "))
                            if opcao_pve == 1:
                                break
                            elif opcao_pve == 2:
                                break
                            elif opcao_pve == 3:
                                print(f"A pontuação no momento está: {d_pontos_pve}")
                            else:
                                print("Opção Inválida")

                        #segundo break para quando o jogador escolher a opcao "Voltar ao menu" quebrar o 2 loops e voltar ao menu no jogo inicial
                        if opcao_pve == 2:
                            break
                        else:
                            continue

                    #caso o computador vença
                    elif resultado_pve == 2:
                        os.system("cls")
                        print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                    Ronda {ronda}
                                                        
                        Jogada de {nome_j1_pve}: {jogada_1_pve}
                                                                
                        Jogada de {nome_j2_pve}: {jogada_pc}                                  
                                                
                                                
                                    Parabéns!                  
                               O vencedor é o Computador!           
                                    
            1. Jogar Outravez      2. Voltar ao Menu     3. Pontuação                  
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)
                            
                        #loop que só é quebrado quando o jogador escolher a opcao 1 ou 2
                        while True:      
                            opcao_pve = int(input("Introduza a sua opcão: "))
                            if opcao_pve == 1:
                                break
                            elif opcao_pve == 2:
                                break
                            elif opcao_pve == 3:
                                print(f"A pontuação no momento esta: {d_pontos_pve}")
                            else:
                                print("Opção Inválida")

                        #segundo break para quando o jogador escolher a opcao "Voltar ao menu" quebrar o 2 loops e voltar ao menu do jogo inicial
                        if opcao_pve == 2:
                            break
                        else:
                            continue
                            
                    #caso haja empate
                    elif resultado_pve == 3:
                        os.system("cls")
                        print (f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                    Ronda {ronda}
                                                        
                        Jogada de {nome_j1_pve}: {jogada_1_pve}
                                                                
                        Jogada de {nome_j2_pve}: {jogada_pc}                                  
                                                
                                                
                                Não há Vencedor! 
                                    Empate...                           
                                                    
            1. Jogar Outravez      2. Voltar ao Menu     3. Pontuação             
                                                                                                                
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

                        #loop que só é quebrado quando o jogador escolher a opcao 1 ou 2  
                        while True:
                            opcao_pve = int(input("Introduza a sua opcão: "))
                            if opcao_pve == 1:
                                break
                            elif opcao_pve == 2:
                                break
                            elif opcao_pve == 3:
                                print(f"A pontuação no momento esta: {d_pontos_pve}")
                            else:
                                print("Opção Inválida")

                        #segundo break para quando o jogador escolher a opcao "Voltar ao menu" quebrar o 2 loops e voltar ao menu do jogo incial
                        if opcao_pve == 2:
                            break
                        else:
                            continue
                        
                    else:
                        print("Inválido")

                    
            ############# Jogador vs Jogador #############
            elif opcao_jogar == 2:
                os.system("cls")
                print("""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                            
                                                                
                                                                
                                                                
                                                                
                            Inroduzam os vossos nomes...                
                                                            
                            ___________ vs ___________               
                                                                
                                                                
                                                                
                                                                
                                                                
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)
                
                nome_j1_pvp = str(input("Introduza o nome do Jogador 1: "))
                nome_j2_pvp = str(input("Introduza o nome do jogador 2: "))

                #função que serve para fazer o registo dos jogadores no dicionário d_pvp
                registo_jvj(d_pvp, nome_j1_pvp, nome_j2_pvp)

                os.system("cls")
                print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                                                
                                                            
                                    Boa sorte!                  
                            E que ganhe o mais forte!              
                                                        
                                                                
                            Jogador 1. {nome_j1_pvp}
                                                                
                            Jogador 2. {nome_j2_pvp}                        
                        
                                                        
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

                enter = input("Clique no enter para continuar...")

                
                #loop para podermos sempre que quisermos jogar novamente
                while True:
                    
                    #função que serve para determinar n+1 rondas
                    ronda = determinar_ronda(ronda)

                    os.system("cls") 
                    print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                                                
                                                            
                                                
                                    Ronda {ronda}
                                                        
                        Jogada de {nome_j1_pvp}: __________
                                                                
                        Jogada de {nome_j2_pvp}: __________                                  
                                                
                        
                                                        
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)
                
                    
                    #loop que só é quebrado quando o jogador jogar: pedra, papel ou tesoura
                    while True: 
                        jogada_1_pvp = input(f"{nome_j1_pvp} introdza a sua jogada: ").lower()
                        if (jogada_1_pvp == "pedra") or (jogada_1_pvp == "papel") or (jogada_1_pvp == "tesoura"):   
                            break
                        else:
                            print("Opção inválida...")
                            continue
                    
                    #loop que só é quebrado quando o jogador jogar: pedra, papel ou tesoura
                    while True: 
                        jogada_2_pvp = input(f"{nome_j2_pvp} introdza a sua jogada: ").lower()
                        if (jogada_2_pvp == "pedra") or (jogada_2_pvp == "papel") or (jogada_2_pvp == "tesoura"):   
                            break
                        else:
                            print("Opção inválida...")
                            continue
                    
                    #função que serve para determinar o vencedor
                    resultado_pvp = determinar_vencedor(jogada_1_pvp,jogada_2_pvp)

                    #função de atribuição de pontos e posterior adição dentro do d_pontos
                    if (jogada_1_pvp == "papel" and jogada_2_pvp == "pedra") or (jogada_1_pvp == "pedra" and jogada_2_pvp == "tesoura") or (jogada_1_pvp == "tesoura" and jogada_2_pvp == "papel"):
                        pontos_j1 = atribuir_pontos(jogada_1_pvp, jogada_2_pvp, d_pontos_pvp, nome_j1_pvp, nome_j2_pvp, pontos_j1, pontos_j2)
                    elif (jogada_1_pvp == "pedra" and jogada_2_pvp == "papel") or (jogada_1_pvp == "tesoura" and jogada_2_pvp == "pedra") or (jogada_1_pvp == "papel" and jogada_2_pvp == "tesoura"):
                        pontos_j2 = atribuir_pontos(jogada_1_pvp, jogada_2_pvp, d_pontos_pvp, nome_j1_pvp, nome_j2_pvp, pontos_j1, pontos_j2)        
                    elif (jogada_1_pvp == "papel" and jogada_2_pvp == "papel") or (jogada_1_pvp == "pedra" and jogada_2_pvp == "pedra") or (jogada_1_pvp == "tesoura" and jogada_2_pvp == "tesoura"):
                        pontos_j1, pontos_j2 = atribuir_pontos(jogada_1_pvp, jogada_2_pvp, d_pontos_pvp, nome_j1_pvp, nome_j2_pvp, pontos_j1, pontos_j2)                   
                    else:
                        print("Inválido")
                    
                    #se o jogador1 vencer
                    if resultado_pvp == 1:
                        os.system("cls")
                        print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                    Ronda {ronda}
                                                        
                            Jogada de {nome_j1_pvp}: {jogada_1_pvp}
                                                                
                            Jogada de {nome_j2_pvp}: {jogada_2_pvp}                                  
                                                
        
                                    Parabéns!                                 
                            O vencedor é {nome_j1_pvp}           
                                    
            1. Jogar Outravez      2. Voltar ao Menu     3. Pontuação                              
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

                        #loop que só é quebrado quando o jogador escolher a opcao 1 ou 2
                        while True:      
                            opcao_pvp = int(input("Introduza a sua opcão: "))
                            if opcao_pvp == 1:
                                break
                            elif opcao_pvp == 2:
                                break
                            elif opcao_pvp == 3:
                                print(f"A pontuação no momento esta: {d_pontos_pvp}")
                            else:
                                print("Opção Inválida")

                        #segundo break para quando o jogador escolher a opcao "Voltar ao menu" quebrar o 2 loops e voltar ao menu do jogo inicial
                        if opcao_pvp == 2:
                            break
                        else:
                            continue
                    
                    #se o jogador2 vencer
                    elif resultado_pvp == 2:
                        os.system("cls")
                        print(f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                    Ronda {ronda}
                                                        
                            Jogada de {nome_j1_pvp}: {jogada_1_pvp}
                                                                
                            Jogada de {nome_j2_pvp}: {jogada_2_pvp}                                  
                                                
                                                
                                    Parabéns!                  
                            O vencedor é {nome_j2_pvp}!           
                                    
            1. Jogar Outravez      2. Voltar ao Menu     3. Pontuação                  
                                                                                                    
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

                        #loop que só é quebrado quando o jogador escolher a opcao 1 ou 2
                        while True:      
                            opcao_pvp = int(input("Introduza a sua opcão: "))
                            if opcao_pvp == 1:
                                break
                            elif opcao_pvp == 2:
                                break
                            elif opcao_pvp == 3:
                                print(f"A pontuação no momento esta: {d_pontos_pvp}")
                            else:
                                print("Opção Inválida")

                        #segundo break para quando o jogador escolher a opcao "Voltar ao menu" quebrar o 2 loops e voltar ao menu do jogo inicial
                        if opcao_pvp == 2:
                            break
                        else:
                            continue
                    
                    #se houver um empate
                    elif resultado_pvp == 3:
                        os.system("cls")
                        print (f"""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                
                                    Ronda {ronda}
                                                        
                            Jogada de {nome_j1_pvp}: {jogada_1_pvp}
                                                                
                            Jogada de {nome_j2_pvp}: {jogada_2_pvp}                                  
                                                
                                                
                                Não há Vencedor! 
                                    Empate...                           
                                                    
            1. Jogar Outravez      2. Voltar ao Menu     3. Pontuação             
                                                                                                                
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        """)

                        #loop que só é quebrado quando o jogador escolher a opcao 1 ou 2
                        while True:      
                            opcao_pvp = int(input("Introduza a sua opcão: "))
                            if opcao_pvp == 1:
                                break
                            elif opcao_pvp == 2:
                                break
                            elif opcao_pvp == 3:
                                print(f"A pontuação no momento esta: {d_pontos_pvp}")
                            else:
                                print("Opção Inválida")

                        #segundo break para quando o jogador escolher a opcao "Voltar ao menu" quebrar o 2 loops e voltar ao menu do jogo inicial
                        if opcao_pvp == 2:
                            break
                        else:
                            continue
                    
                    else: 
                        print("Inválido!")

            #serve para voltar ao menu inicial do jogo
            elif opcao_jogar == 3:
                pass
            else:
                print("Opção inválida!")


            #ver as regras
        elif opcao_1 == 2:
            os.system("cls")
            print("""
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                                    
                O jogo "Pedra, Papel ou Tesoura", consiste em uma   
            batalha de várias rondas usando grandezas: a Pedra,  
            o Papel, e a Tesoura.                                
                Em cada ronda, cada jogador deverá escolher uma das 
            três grandezas e ganha a que for mais forte:         
                                                                
                Pedra > Tesoura (Pedra destroi a Tesoura)       
                Tesoura > Papel (Tesoura corta o Papel)         
                Papel > Pedra (Papel embrulha a Pedra)          
                                                                
                            1. Voltar ao Menu                    
                                                            
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            """)

            #loop que só é quebrado quando o jogador escrever 1
            while True:
                opcao_regras = int(input("Introduza a sua opção: "))
                if opcao_regras == 1:
                    break
                else:
                    print("Opção Inválida!")
                    continue
        
        #serve para sair do jogo
        elif opcao_1 == 3:
            break
        else:
            print("Opção inválida!")

