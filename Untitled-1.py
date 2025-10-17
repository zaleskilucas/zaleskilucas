import os
import sys #importa biblioteca para limpeza do terminal

def leitura_dados(): #funçao destinada a criaçao de variaveis e leitura de dados no console
    print("*** Mini Questionário ***\n")
    nome = input("Qual seu nome?\n")
    idade = input("Qual a sua idade?\n")
    genero = input("Você é homem ou mulher?\n")
    endereco = input("Qual o seu endereço?\n")

    return nome, idade, genero, endereco #retorno de variáveis para outras funções

def impressao_dados(nome, idade, genero, endereco): #funçao destinada a impressão de dados no console
    print("*** Mini Questionário ***\n")
    print("Olá, ", nome, "\n")
    print("Idade:", idade, "\n")
    print("Gênero:", genero, "\n")
    print("Endereço:", endereco, "\n")

def iniciar_dados(): #função criada para iniciar a aplicaçâo chamado outras funções existentes
    leitura_dados() #chamando função de leitura de dados
    os.system('cls') #chamando função para limpeza de console
    impresao_dados() #chamando função de impressão de dados

    iniciar_app()