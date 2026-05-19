'''
Define o grafo usando uma lista de adjacências.
Cada entrada representa um nó e suas conexões (nó, distância).
'''
mapa = {
    'Arad': [
        ('Zerind', 75),
        ('Sibiu', 140),
        ('Timisoara', 118)
        ],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
}


# def busca_dfs(grafo, inicio, objetivo):
#     # TODO: Implemente a lógica da Busca em Profundidade aqui:
#     # 1. Inicialize uma Pilha (LIFO) com o nó inicial, o caminho percorrido e o custo acumulado.
#     # 2. Crie um conjunto (set) para rastrear os nós já visitados.
#     # 3. Enquanto a pilha não estiver vazia:
#     #    a. Remova o último elemento da pilha.
#     #    b. Se o nó for o objetivo, retorne o caminho e o custo.
#     #    c. Se o nó não foi visitado:
#     #       i. Marque-o como visitado.
#     #       ii. Adicione seus vizinhos não visitados à pilha (mantenha o controle do caminho e custo).
#     return None, 0 # Caminho, Custo


def busca_dfs(grafo,inicio,objetivo):
    caminho_percorrido = [inicio]
    visitados = set()
    custo_acumulado=0
    pilha = [(inicio, caminho_percorrido, custo_acumulado)]

    while pilha:
        cidade, caminho, custo = pilha.pop()
        if cidade == objetivo:
            return caminho, custo 
        if cidade not in visitados:
            visitados.add(cidade)
            for vizinho, distancia in grafo[cidade]:
                somacusto = custo + distancia
                pilha.append((vizinho,[*caminho, vizinho], somacusto))
    return caminho, custo
    
    
# Teste da DFS
caminho_dfs, custo_dfs = busca_dfs(mapa, 'Arad', 'Bucharest')
print("--- DFS ---")
print(f"Caminho: {' -> '.join(caminho_dfs)}" if caminho_dfs else "Caminho não encontrado")
print(f"Custo Total: {custo_dfs}")