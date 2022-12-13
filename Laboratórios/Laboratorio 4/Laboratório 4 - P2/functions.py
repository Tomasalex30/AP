#função para registar os jogadores num dicionário
def registo_jvj (d_pve, nome_j1, nome_j2):
    d_pve.update({"Jogador": nome_j1, "Jogador 2": nome_j2})

#função que adiciona rondas 
def determinar_ronda (ronda):
    ronda += 1
    return ronda

#função que determina os vencedores
def determinar_vencedor (jogada_1, jogada_2):
    if (jogada_1 == "papel" and jogada_2 == "pedra") or (jogada_1 == "pedra" and jogada_2 == "tesoura") or (jogada_1 == "tesoura" and jogada_2 == "papel"):
        return 1 #vencedor: jogador1
    elif (jogada_1 == "pedra" and jogada_2 == "papel") or (jogada_1 == "tesoura" and jogada_2 == "pedra") or (jogada_1 == "papel" and jogada_2 == "tesoura"):
        return 2 #vencedor: jogador2
    elif (jogada_1 == "papel" and jogada_2 == "papel") or (jogada_1 == "pedra" and jogada_2 == "pedra") or (jogada_1 == "tesoura" and jogada_2 == "tesoura"):
        return 3 #vencedor: empate
    else:
        return False

#função que atribui os pontos e armazena-os, e posteriormente adiciona num dicionário
def atribuir_pontos (jogada_1, jogada_2, d_pontos, nome_j1, nome_j2, pontos_j1, pontos_j2):
    if (jogada_1 == "papel" and jogada_2 == "pedra") or (jogada_1 == "pedra" and jogada_2 == "tesoura") or (jogada_1 == "tesoura" and jogada_2 == "papel"):
        pontos_j1 += 5
        d_pontos.update({f"Jogador 1 / {nome_j1}": pontos_j1, f"Jogador 2 / {nome_j2}": pontos_j2})
        return pontos_j1
    elif (jogada_1 == "pedra" and jogada_2 == "papel") or (jogada_1 == "tesoura" and jogada_2 == "pedra") or (jogada_1 == "papel" and jogada_2 == "tesoura"):
        pontos_j2 += 5
        d_pontos.update({f"Jogador 1 / {nome_j1}": pontos_j1, f"Jogador 2 / {nome_j2}": pontos_j2})
        return pontos_j2
    elif (jogada_1 == "papel" and jogada_2 == "papel") or (jogada_1 == "pedra" and jogada_2 == "pedra") or (jogada_1 == "tesoura" and jogada_2 == "tesoura"):
        pontos_j1 += 1
        pontos_j2 += 1
        d_pontos.update({f"Jogador 1 / {nome_j1}": pontos_j1, f"Jogador 2 / {nome_j2}": pontos_j2}) 
        return pontos_j1, pontos_j2
    else:
        return False




        
    
        