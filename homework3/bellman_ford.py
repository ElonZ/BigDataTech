
def reader(file):
    with open(file) as f:
        content = f.readlines()
        keys = content[::2]
        values = content[1::2]

        keys = [int(i.strip()) for i in keys]
        values = [eval('[' + i.strip() + ']') for i in values]

        if len(keys) != len(values):
            print("Length does not match")
            return
    graph = dict(zip(keys, values))
    return graph


def initialize(graph, source):
    distance = {}
    ancestor = {}

    for node in graph.keys():
        distance[node] = float('Inf')
        ancestor[node] = None

    distance[source] = 0
    return distance, ancestor


def relax(node, neighbour, dist_value, distance, ancestor):
    if distance[neighbour] > distance[node] + dist_value:
        distance[neighbour] = distance[node] + dist_value
        ancestor[neighbour] = node


def bellman_ford(graph, source):
    distance, ancestor = initialize(graph, source)
    has_cycle = False
    for i in range(len(graph) - 1):
        for node in graph.keys():
            for neighbor, dist_value in graph[node]:
                relax(node, neighbor, dist_value, distance, ancestor)

    for node in graph.keys():
        # print(graph[node])
        for neighbor, dist_value in graph[node]:
            # print(neighbor, dist_value)
            if distance[node] > distance[neighbor] + dist_value:
                start_node = neighbor
                cycle = [neighbor]
                # print(start_node)
                neighbor = ancestor[neighbor]
                while (neighbor != start_node):
                    # print(neighbor)
                    cycle.append(neighbor)
                    neighbor = ancestor[neighbor]
                has_cycle = True

                return distance, ancestor, has_cycle, cycle[::-1]

    cycle = None
    return distance, ancestor, has_cycle, cycle


if __name__ == '__main__':
    graph = reader('cycletestdata.txt')

    distance, ancestor, has_cycle, cycle = bellman_ford(graph, 1)

    print(cycle)

