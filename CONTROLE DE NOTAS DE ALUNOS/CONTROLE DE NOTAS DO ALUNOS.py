#CONTROLE DE NOTAS DO ALUNOS
from modulo1 import Alunos as A
import json

def add_aluno():
    nome = input("\nDigite o nome completo do aluno: ")
    M1 = float(input("Digite a Média do primeiro trimestre: "))
    M2 = float(input("Digite a Média do segundo trimestre: "))
    M3 = float(input("Digite a Média do terceiro trimestre: "))
    A(nome, M1, M2, M3)

def encontrar_aluno():
    nome = input("Digite o nome do aluno: ")
    with open("mini_pauta.json", "r", encoding="utf-8") as arquivo:
        pauta = json.load(arquivo)
            
        for lista in pauta:   
            if lista.get("Nome").strip().lower() == nome.strip().lower():
                print(lista)
                b = True
                break
            else:
                b = False
        if b == True:
            pass
        elif b == False:
            print("Nome não encontrado")   

def expor_pauta():
    with open("mini_pauta.json", "r", encoding="utf-8") as arquivo:
        pauta = json.load(arquivo)
        for lista in pauta:   
            print(lista)
    

while True:
    try:
        print("\n SISTEMA DE CONTROLE DE NOTAS DO ALUNOS\n 1-Adicionar alunos\n 2-proucurar aluno\n 3-Exportar dados\n 4-Sair\n")
        opcao = int(input("Selecione uma das opções acima para continuar: "))
        
        if opcao == 1:
            add_aluno()
        elif opcao == 2:
            encontrar_aluno()
        elif opcao == 3:
            expor_pauta()
        elif opcao == 4:
            break
        else:
            print("Opção Invalida!")
    except (TypeError, ValueError, FileNotFoundError, SyntaxError):
        print("Erro, Opção invalida!")