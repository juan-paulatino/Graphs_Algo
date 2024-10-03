import sys

# Búsqueda en profundidad (DFS) para explorar todos los vértices en un componente
def dfs(adj, visited, v):
    visited[v] = True  # Marcar el vértice actual como visitado
    for neighbor in adj[v]:  # Visitar todos los vecinos no visitados
        if not visited[neighbor]:
            dfs(adj, visited, neighbor)

# Función para contar el número de componentes conectados
def number_of_components(adj):
    result = 0  # Inicializar el número de componentes conectados
    visited = [False] * len(adj)  # Para rastrear los vértices visitados
    
    # Recorrer todos los vértices
    for v in range(len(adj)):
        if not visited[v]:  # Si un vértice no ha sido visitado, es un nuevo componente
            dfs(adj, visited, v)  # Realizar DFS para este componente
            result += 1  # Incrementar el contador de componentes resultantes
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()  # Leer la entrada completa usando sys.stdin.read()
    
    data = list(map(int, input.split()))
    n, m = data[0:2]  # Número de vértices y aristas
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))  # Lista de aristas detectadas
    adj = [[] for _ in range(n)]  # Inicializar la lista de adyacencia
    
    # Construir la lista de adyacencia para un grafo no dirigido
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # Agregar b como vecino de a (indexado en 0)
        adj[b - 1].append(a - 1)  # Agregar a como vecino de b (indexado en 0)
    
    # Imprimir el número de componentes conectados
    print(number_of_components(adj))


