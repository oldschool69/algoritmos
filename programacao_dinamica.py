import numpy as np


def problema_da_mochila():
    capacidade_mochila = 4
    num_items = 4
    pesos = [1, 4, 2, 1]
    precos = [1500, 3000, 2000, 2000]
    
    tabela = np.zeros((num_items + 1, capacidade_mochila + 1))
    
    for i in range(1, num_items + 1):
        for j in range(0, capacidade_mochila + 1):
            maximo_anterior = tabela[i - 1][j]
            valor_item_atual = precos[i - 1]
            valor_espaco_restante = tabela[i - 1][j - pesos[i - 1]]

            if pesos[i - 1] <= j:
                tabela[i][j] = max(maximo_anterior, valor_item_atual + valor_espaco_restante)
            else:
                tabela[i][j] = tabela[i - 1][j]
                
            
    print("resultado: ", tabela[num_items][capacidade_mochila])
            

def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP table: (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(0, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]