import random 

############# Funções Exercício 1 #############
def funcao_1():
    for i in range(-10, 10, 2):
        if (i%2 == 0):
            return i

## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta: 
# Esta função é constituida por uma estrutura repetitiva com contador automático (for), com o auxilio da função range, criando um loop. E por uma estrutura condicional simples (if)
# Dentro da função range, o inicio da incrementação é o -10 e o fim da incrementação é o 10 e o respetivo "passo" é 2, ou seja vai andar de 2 em 2 nesse conjunto de valores.
# A estrutura condicional simples (if) com a condição "i%2 == 0" serve para verificar quais são os numeros que apresentam o resto 0 quando é feita a divisão por 2.
# Se a condição da estrutura condicional for satisfazivel/verdadeira, o corpo da estrutura condicional será executado e os valores serão retornados à variável i
# Se a condição da estrutura condicional não for satisfazivel/verdadeira, não é executado o corpo da estrutura condicional.
# O output desta função será todos os numeros pares de -10 até 9, que estão compreendidos dentro da função range.

#################################################
def funcao_2(numero):
    n = 0
    while n < numero:
        numero *= 2
    return numero

## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta: 
# A função tem como parametro de entrada a variável (numero)
# Inicialmente, é armazenado o valor 0 à variável n.
# Esta função é constituida por uma estrutura repetitiva condicional (while), criando um loop infinito até que esta seja Falsa.
# A condição da estrutura repetitiva "n < numero" serve para verificar se o parametro de entrada (numero) é menor que o valor da variável n.
# Dentro do corpo da estrutura repetitiva: O "*" é um operador aritmético de multiplicação que serve para multiplicar o parametro de entrada por 2, o uso do "=" serve para armazenar a operação aritmética dentro do parametro de entrada, por exemplo: a *= b -> a = a * b.
# Se a condição da estrutura repetitiva for satisfazivel/verdadeira, o corpo da estrutura repetitiva é executado, e o parametro de entrada é multiplicado infinitamente.
# Se a condição da estrutura repetitiva não for satisfazivel/verdadeira, o corpo da estrutura repetitiva não é executado e a função termina.
# Por fim é retornado o valor da operação dentro da variável (numero).
# O output desta função será um conjunto de numeros infinitos ou impossivel, dependendo da veracidade da condição.

#################################################
def funcao_3(palavra):
    for i in range(len(palavra)):
        if palavra[0] == 'a':
            palavra.replace('a', 'c')
        else:
            palavra.replace(palavra[0], 'x')
        
        return palavra

## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta: 
# A função tem como parametro de entrada a variável (numero)
# Esta função é constituida por uma estrutura repetitiva com contador automático (for), com o auxilio da função range, criando um loop. E uma estrutura condicional normmal (if, else)
# Na função range, dentro dos parametros de incrementação é inserida a função len(), ou seja é atribuido o comprimento do valor da variável palavra.
# A palavra reservada "if" da estrutura condicional normal, com a condição (palavra[0] == 'a':) serve para verificar se a primeira letra da variável é um "a".
# Dentro do corpo da palavra reservada "if" está presente uma função (replace()) que serve para substituir todos os caracteres "a" pelos caracteres "c" 
# Se a condição da palavra reservada "if" for satisfazivel/verdadeira é executado o corpo da função.
# Se a condição da palavra reservada "if" não for satizfazivel/verdadeira é executada a palavra reservada "else" da estrutura condicional normal.
# A palavra reservada "else" não apresenta condição pois é tudo exceto a condição da palavra reservada "if".
# Dentro do corpo da palavra reservada "else" está presente a função (replace()) que serve para substituir a primeira letra da "palavra" armazenada na variável palavra pela letra x
# No final é retornado o valor à variável palavra 
# O output irá depender de qual a condição o valor da variável palavra satisfazer dentro da estrutura condicional normal.


#################################################

def funcao_4():
    for i in range(10, 20, -1):
        return i
## Indique o quais as operações realizadas pela função e o respetivo é o resultado.
#Resposta: 
# Esta função é constituida por uma estrutura repetitiva com contador automático (for), com o auxilio da função range, criando um loop.
# Na função range, o inicio da incrementação é o 10 e o fim da incrementação é o 20, com um "passo" de -1, ou seja vai andar de um em um para trás nesse conjunto de valores.
# Como o inicio da incrementação é 10, o "passo" começa a andar para trás a partir desse valor. Porém não há valores definidos menores que 10 pois o fim da incrementação é 20.
# Não existindo valores menores que 10 ao realizar a primeira operação a função abrangeria todos os valores de ]-infinito, 9] aos quais não estão definidos na função range.
# Concluimos que o output desta função é impossivel de ser obtido. 

#################################################

############# Funções Exercício 2 #############

def somar_numeros(numero_1, numero_2):
    return numero_1 + numero_2

def multiplicar_numeros(numero_1, numero_2):
    return numero_1 * numero_2

def comparar_numeros(numero_1, numero_2):
    if numero_1 > numero_2:
        return 1
    elif numero_1 < numero_2:
        return 2
    else:
        return 3

def verificar_igualdade(numero_1, numero_2):
    if numero_1 == numero_2:
        return numero_1
    else:
        return False

def retornar_maior_de_dois(numero_1, numero_2):
    if numero_1 == numero_2:
        return False
    elif numero_1 > numero_2:
        return numero_1
    else:
        return numero_2
    

def retornar_menor_de_dois(numero_1, numero_2):
    if numero_1 == numero_2:
        return False
    elif numero_1 < numero_2:
        return numero_1
    else:
        return numero_2
    
def super_jogo(numero_1, numero_2):
    if numero_1 == numero_2:
        return 1
    else:
        return 2

    

