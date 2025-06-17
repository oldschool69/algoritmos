from collections import deque

grafo = {}

def dfs(nome):
    popula_grafo()
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]["friends"]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            balance = grafo[pessoa]['balance']
            if pessoa_e_milionaria(balance):
                print(pessoa + " é um milhionario!, saldo de " + str(balance))
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]["friends"]
                verificadas.append(pessoa)
    
    return False
     

def popula_grafo():
    grafo["voce"] = { "friends": ["alice", "bob", "claire"],  "balance": 15000 }
    grafo["bob"] = { "friends": ["anuj", "peggy"], "balance": 256000 }
    grafo["alice"] = { "friends": ["peggy"], "balance": 178598 }
    grafo["claire"] = { "friends": ["thom", "jonny"], "balance": 54699 }
    grafo["anuj"] = {  "friends": [],  "balance": 789 }
    grafo["peggy"] = {  "friends": [], "balance": 18456 }
    grafo["thom"] = { "friends": [], "balance": 879966 }
    grafo["jonny"] = {"friends": [], "balance": 2000000 }


def pessoa_e_milionaria(balance):
    return balance >= 1000000