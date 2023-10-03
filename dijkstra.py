def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node
        
    return lowest_node


def print_path(parents, path):
    if parents:
        path.append(parents.pop(path[-1]))
        return print_path(parents, path)
    else:
        for i in range(len(path)):
            print(f"{i + 1}. {path.pop()}")


graph = {}
choice = 0
while True:
    print("WYBIERZ OPCJĘ SPOŚRÓD DOSTĘPNYCH PONIŻEJ")
    print("1. Dodaj NODE")
    print("2. Dodaj metę i zakończ")
    print()
    while choice not in range(1, 3):
        choice = int(input("Opcja: "))
    
    if choice == 1:
        node = input("Podaj nazwę NODE'a: ")
        graph[node] = {}
        while True:
            print("Zakończ dodwanie krawędzi przypisując jej ujemną wartość")
            value = int(input("Podaj wartość krawędzi: "))
            if value < 0:
                break
            
            edge = input("Podaj nazwę krawędzi: ")
            graph[node][edge] = value
    else:
        graph["meta"] = {}
        break

    choice = 0

infinity = float("inf")
costs = {"a": 6, "b": 2, "meta": infinity}

parents = {"a": "start", "b": "start", "meta": None}

processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
            
    processed.append(node)
    node = find_lowest_cost_node(costs)

print()
print(f"Waga najkrótszej drogi: {costs['meta']}")
print("Droga:")
print_path(parents, ["meta"])