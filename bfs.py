import sys
import queue # nueva libreria 

def distance(adj, s, t):
    # Inicializar una lista de distancias con -1 (representa "no visitado")
    dist = [-1] * len(adj)
    dist[s] = 0  # La distancia desde el nodo fuente a sí mismo es 0
    q = queue.Queue() # en cola
    q.put(s)
    
    # BFS
    while not q.empty():
        u = q.get()  # Extraemos el siguiente nodo de la cola
        for neighbor in adj[u]:
            if dist[neighbor] == -1:  # Si el vecino no ha sido visitado
                q.put(neighbor)  # Lo añadimos a la cola para procesarlo más tarde
                dist[neighbor] = dist[u] + 1  # Actualizamos la distancia mínima
                if neighbor == t:  # Si hemos alcanzado el destino
                    return dist[neighbor]  # Devolver la distancia
    
    return -1  # Si no se encuentra un camino, devolvemos -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # Convertir a indexación basada en 0
        adj[b - 1].append(a - 1)  # Grafo no dirigido, añadir ambas direcciones
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t)) #se imprime el resultado
