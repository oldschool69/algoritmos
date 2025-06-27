# Utilização de algoritmo guloso utilizando set 
# para encontrar o conjunto de estações de rádio
# que abrangem todos os estados  

estacoes = {}

def popular_estacoes():
    estacoes["kum"] = set(["id", "nv", "ut"])
    estacoes["kdois"] = set(["wa", "id", "mt"])
    estacoes["ktres"] = set(["or", "nv", "ca"])
    estacoes["kquatro"] = set(["nv", "ut"])
    estacoes["kcinco"] = set(["ca", "az"])
    
    
def localizar_melhores_estacoes():
    popular_estacoes()
    estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    estacoes_finais = set() # no set vc remove entradas duplicadas
    
    while estados_abranger:
        melhor_estacao = None
        estados_cobertos = set()
        
        for estacao, estados in estacoes.items():
            # usando o operador & retorna a intersecção de valores comuns
            # entre 2 sets 
            cobertos = estados_abranger & estados 
            if(len(cobertos) > len(estados_cobertos)):
                melhor_estacao = estacao
                estados_cobertos = cobertos
        
        # atualiza o set de estados a abranger removendo os estados ja cobertos                
        estados_abranger -= estados_cobertos
        
        # armazena a melhor estacao encontrada
        estacoes_finais.add(melhor_estacao)
    
    print("estacoes finais ", estacoes_finais)
            
            
