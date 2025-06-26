# Considere o seguinte grafo com pesos positivos
#          (A)
#          ^^\
#       6 / | \ 1 
#        /  |  \
#       /   |   v 
# (inicio)  |3 (fim)
#       \   |   ^ 
#        \  |  /
#       2 \ | / 5          
#          v|/
#          (B) 
#
# Será utilizado Djikstra para encontrar o menor caminho
# que é (inicio) -> (B) -> (A) -> (fim), custo total 5 

grafo = {}
custos = {}
pais = {}
processados = []


def dijkstra():
    popula_grafo()
    popula_custos()
    popula_pais()
    processados.clear()
    
    node = achar_node_com_custo_mais_baixo(custos)
    
    while node is not None:
        custo = custos[node]
        vizinhos = grafo[node]
        for n in vizinhos.keys():
            novo_custo = custo + vizinhos[n]
            if custos[n] > novo_custo:
                custos[n] = novo_custo
                pais[n] = node
        processados.append(node)
        node = achar_node_com_custo_mais_baixo(custos)
    
    imprimir_caminho_e_custo_total()
        
    


def achar_node_com_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    node_com_custo_mais_baixo = None
    for node in custos: 
        custo = custos[node]
        if custo < custo_mais_baixo and node not in processados:
            custo_mais_baixo = custo
            node_com_custo_mais_baixo = node
    
    return node_com_custo_mais_baixo

def popula_grafo():
     grafo["inicio"] = {}
     grafo["inicio"]["a"] = 6
     grafo["inicio"]["b"] = 2
     
     grafo["a"] = {}
     grafo["a"]["fim"] = 1
     
     grafo["b"] = {}
     grafo["b"]["a"] = 3
     grafo["b"]["fim"] = 5
     
     grafo["fim"] = {}
     
def popula_custos():
    infinito = float("inf")
    custos["a"] = 6
    custos["b"] = 2
    custos["fim"] = infinito
    
def popula_pais():
    pais["a"] = "inicio"
    pais["b"] = "inicio"
    pais["fim"] = None
    
def imprimir_caminho_e_custo_total():
    pai = "inicio"
    caminho = pai + " -> "
    
    while pai != "fim":
        for key in pais.keys():
            if pais[key] == pai:
                filho = key
                pai = filho
                caminho += filho
                if filho != "fim":
                    caminho += " -> "        
    
    print("caminho ", caminho)        
    print("custo total ", custos["fim"])
    

    