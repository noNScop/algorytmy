graph = {}
graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"meta": 1}
graph["b"] = {"a": 3, "meta": 5}
graph["meta"] = {}

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