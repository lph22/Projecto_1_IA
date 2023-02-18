

formed_graph = [
    [0,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0],
    [0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
names = [
    'Arad','Timisoara','Sibiu','Zerind','Lugoj','Rimnicu Vilcea','Fagaras','Oradea',
    'Mehadia','Craiova','Pitesti','Bucarest','Drobeta','Giurgiu','Urziceni','Hirsova',
    'Vaslui','Efoire','Iasi','Neamt'
]

def generate_states(graph, availabele_nodes_names):
    nodes_tuples =[]
    node_connection_wieghts = []
    for matrix_row_index in range(len(graph)):
        connections_and_weights = []

        for matrix_column_index in range(len(graph[0])):
            
            if graph[matrix_row_index][matrix_column_index] != 0:
                nodes_tuples.append((availabele_nodes_names[matrix_row_index], availabele_nodes_names[matrix_column_index]))
                connections_and_weights.append(( availabele_nodes_names[matrix_column_index], graph[matrix_row_index][matrix_column_index]))
        
        if len(connections_and_weights) != 0:
            node_connection_wieghts.append((availabele_nodes_names[matrix_row_index], connections_and_weights))

    return (nodes_tuples, node_connection_wieghts)


def dfs(graph, start, goal):
    if start == goal:
        return [start]
    paths = [[start]]
    while paths != []:
        # La diferencia más importante entre bfs y dfs es el hecho que en vez de tener un cola, como en bfs,
        # Lo que tenemos aqui es una pila, esto nos permite volver a expandir el mismo camino hasta que encontremos
        # un nodo sin más vecinos. El resto es identico a las ideas para bfs
        path = paths.pop()
        current_node = path[-1]
        children = [edge[1] for edge in graph if edge[0] == current_node]
        for child in children:
            if child == goal:
                path.append(child)
                return path
            extended_path = path.copy()
            extended_path.append(child)
            paths.append(extended_path)

def dfs_with_limit(graph, start, goal, limit, Printing = True):
    if start == goal:
        return [start]
    paths = [[start]]
    while paths != []:
        path = paths.pop()
        # Lo que cambia principalmente es que queremos asegurar que el camino que tomemos no pase el limite de longitud que aplicamos
        # asi que se checa para que antes de que se ejecute el resto del algoritmo. Este es identico a bfs de arriba 
        if len(path) > limit:
            continue
        current_node = path[-1]
        children = [edge[1] for edge in graph if edge[0] == current_node]
        for child in children:
            if child == goal:
                path.append(child)
                return (path, limit)
            extended_path = path.copy()
            extended_path.append(child)
            paths.append(extended_path)
    if Printing:
        print(f"No hay caminos desde {start} hacia {goal} con un limite de profundidad de {limit}")
    return []

def iterative_deepening(graph, start, goal):
    for limit in range(len(formed_graph)):
        path = dfs_with_limit(graph, start, goal, limit, False)
        if path != []:
            break
    print(path)

def validate_in(command) -> str:
    """Es una función que se asegura que el nombre ingresado este dentro de los nombres de las ciudades"""
    while True:
        city = input(command)
        if city in names:
            break
        print("El nombre de la ciudad ingresada es incorrecto.")
    return city

def validate_int() -> int:
    """Es una función que se asegura que se ingreso un número no negativo"""
    while True:
        try:
            limit = int(input("Ingrese el limite de profundidad de busqueda: "))
            if limit >= 0:
                break
            print("Ingrese un número no negativo")
        except:
            print("Ingrese un número")
    return limit

def main():
    tree = generate_states(formed_graph, names)[0]
    start = validate_in("Ingrese la ciudad de entrada: ")
    goal = validate_in("Ingrese la ciudad meta: ")
    limit = validate_int()
    dfs_with_limit(tree, start, goal, limit)
    iterative_deepening(tree, start, goal)

if __name__ == "__main__":
    main()