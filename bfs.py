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

from collections import deque

def busca_bfs(grafo,inicio,objetivo):
    caminho_percorrido = [inicio]
    visitados = {inicio}
    custo_acumulado=0
    fila = deque([(inicio, caminho_percorrido, custo_acumulado)])

    while fila:
        cidade, caminho, custo = fila.popleft()
        if cidade == objetivo:
            return caminho, custo 
        for vizinho, distancia in grafo[cidade]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                somacusto = custo + distancia
                fila.append((vizinho,[*caminho, vizinho], somacusto))
    return caminho, custo

    
# Teste da BFS
caminho_bfs, custo_bfs = busca_bfs(mapa, 'Arad', 'Bucharest')
print("--- BFS ---")
print(f"Caminho: {' -> '.join(caminho_bfs)}" if caminho_bfs else "Caminho não encontrado")
print(f"Custo Total: {custo_bfs}")