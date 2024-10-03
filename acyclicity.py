import sys
sys.setrecursionlimit(2000) # Para manejar una gran profundidad de recursión debido a las altas restricciones.

def acyclic(adj):
    n = len(adj)
    visited = [0] * n  # 0 -> no visitado, 1 -> visitando, 2 -> visitado
    
    def dfs(v):
        visited[v] = 1  # Marcar el nodo actual como en proceso de visita
        for neighbor in adj[v]:
            if visited[neighbor] == 0:  # Si el vecino no ha sido visitado
                if dfs(neighbor):  # Si encontramos un ciclo en la llamada DFS
                    return True
            elif visited[neighbor] == 1:  # Encontramos un nodo en la pila de recursión actual
                return True
        visited[v] = 2  # Marcar el nodo como completamente procesado
        return False
    
    for i in range(n):
        if visited[i] == 0:  # Iniciar un DFS desde cada nodo no visitado
            if dfs(i):
                return 1  # Encontrado un ciclo
    return 0  # No se encontró ningún ciclo

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # Convertir a indexación basada en 0
    print(acyclic(adj))
