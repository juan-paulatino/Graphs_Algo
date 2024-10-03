import sys
import queue

# Función para calcular los caminos más cortos y detectar ciclos negativos
def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0
    reachable[s] = 1
    
    # Algoritmo de Bellman-Ford para relajar aristas hasta n-1 veces
    for _ in range(n - 1):
        for u in range(n):
            if reachable[u]:  # Procesar solo los nodos alcanzables de la red
                for i, v in enumerate(adj[u]):
                    if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][i]:
                        distance[v] = distance[u] + cost[u][i]
                        reachable[v] = 1

    # Después de n-1 relajaciones, verificar si hay ciclos negativos intentando una relajación más
    for u in range(n):
        if reachable[u]:
            for i, v in enumerate(adj[u]):
                if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][i]:
                    distance[v] = distance[u] + cost[u][i]
                    reachable[v] = 1
                    shortest[v] = 0  # Marcar que el vértice `v` es parte o alcanzable desde un ciclo negativo

    # Propagar el efecto de los ciclos negativos
    for _ in range(n):
        for u in range(n):
            if reachable[u] and shortest[u] == 0:
                for v in adj[u]:
                    shortest[v] = 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    
    s = data[0] - 1
    distance = [10**19] * n  # Inicializar la distancia a "infinito"
    reachable = [0] * n  # Inicialmente, ningún vértice es alcanzable
    shortest = [1] * n  # Inicialmente, todos los vértices tienen caminos más cortos bien definidos

    # Calcular los caminos más cortos desde la fuente `s`
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    
    # Imprimir el resultado para cada vértice
    for x in range(n):
        if reachable[x] == 0:
            print('*')  # El vértice no es alcanzable
        elif shortest[x] == 0:
            print('-')  # El vértice es parte o alcanzable desde un ciclo negativo
        else:
            print(distance[x])  # Imprimir la distancia del camino más corto
