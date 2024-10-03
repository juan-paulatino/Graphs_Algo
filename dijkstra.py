import sys
import queue

def distance(adj, cost, s, t):
    # Inicializar el array de distancias con infinito
    dist = [float('inf')] * len(adj)
    dist[s] = 0  # La distancia al origen es 0
    
    # Crear una cola de prioridad
    pq = queue.PriorityQueue()
    pq.put((0, s))  # (distancia, vértice)
    
    # Mientras la cola de prioridad no esté vacía
    while not pq.empty():
        current_dist, u = pq.get()
        
        # Si llegamos al destino, devolver la distancia
        if u == t:
            return current_dist
        
        # Si la distancia es mayor que la distancia registrada más corta, omitir
        if current_dist > dist[u]:
            continue
        
        # Verificar todos los vecinos de u
        for i, neighbor in enumerate(adj[u]):
            weight = cost[u][i]
            new_dist = current_dist + weight
            
            # Si se encuentra un camino más corto al vecino
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                pq.put((new_dist, neighbor))
    
    # Si no se encontró un camino al destino, devolver -1
    return -1 if dist[t] == float('inf') else dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    
    # Crear lista de adyacencia y lista de costos
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)  # Convertir a índice basado en cero
        cost[a - 1].append(w)     # Agregar el peso
    
    s, t = data[0] - 1, data[1] - 1  # Convertir a índice basado en cero
    print(distance(adj, cost, s, t))
