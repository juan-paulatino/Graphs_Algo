import sys
sys.setrecursionlimit(200000)  # To handle large recursion depth due to high constraints

def dfs(adj, used, order, x):
    used[x] = 1  # Marcar el nodo como visitado
    for neighbor in adj[x]:
        if not used[neighbor]:
            dfs(adj, used, order, neighbor)
    order.append(x)  # Agregar el nodo al orden una vez procesados todos sus vecinos

def toposort(adj):
    n = len(adj)
    used = [0] * n  # Inicializar todos los nodos como no visitados
    order = []  # Esta lista almacenará el orden topológico en orden inverso
    for i in range(n):
        if not used[i]:  # Si el nodo no ha sido visitado, realizar DFS
            dfs(adj, used, order, i)
    return order[::-1]  # Invertir el orden para obtener el orden topológico correcto

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # Convertir a indexación basada en 0
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')  # Imprimir la ordenación topológica con indexación basada en 1
