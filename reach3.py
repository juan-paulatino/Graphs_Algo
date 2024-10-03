import sys

def dfs(adj, x, visited):
    visited[x] = True  # Marcar el nodo actual como visitado
    for neighbor in adj[x]:
        if not visited[neighbor]:
            dfs(adj, neighbor, visited)

def reach(adj, x, y):
    visited = [False] * len(adj)  # Inicializar el arreglo de visitados para todos los vértices
    dfs(adj, x, visited)  # Comenzar la búsqueda en profundidad (DFS) desde el vértice `x`
    return 1 if visited[y] else 0  # Verificar si `y` es alcanzable desde `x`

if __name__ == '__main__':
    # Reemplaza sys.stdin.read() con tu cadena de entrada para pruebas, paso opcinal
    input = sys.stdin.read()
    
    data = list(map(int, input.split()))
    n, m = data[0:2]  # Número de vértices y aristas
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))  # Lista de aristas
    x, y = data[2 * m:]  # Los dos vértices a verificar
    adj = [[] for _ in range(n)]  # Representación de la lista de adyacencia del grafo
    x, y = x - 1, y - 1  # Convertir a indexación basada en 0

    # Construir la lista de adyacencia para un grafo no dirigido
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # Índice basado en 0
        adj[b - 1].append(a - 1)  # Índice basado en 0

    # Imprimir el resultado: 1 si existe un camino, 0 en caso contrario
    print(reach(adj, x, y))
