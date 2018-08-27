import sys
import heapq


class MyPriorityQueue(object):
    def __init__(self):
        self.priority_queue = []

    def add(self, priority, element):
        heapq.heappush(self.priority_queue, (priority, element))

    def get(self):
        priority, element = heapq.heappop(self.priority_queue)
        return priority, element

    def size(self):
        return len(self.priority_queue)


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


def find_shortest_path(file, source, destination):
    graph = reader(file)

    if source not in graph.keys() or destination not in graph.keys():
        print("Source/destination does not exit")
        return
    elif source == destination:
        return 0

    to_consider = MyPriorityQueue()
    to_consider.add(0, source)

    considered = MyPriorityQueue()
    distance_results = {}
    distance_results[source] = 0

    path = {}

    # for i in graph.keys():
    #     distance_results[i] = sys.maxsize

    while (to_consider.size() != 0):
        priority, current_node = to_consider.get()
        considered.add(priority, current_node)

        for neighbor, distance in graph[current_node]:
            # print(graph[current_node])
            if neighbor not in set([j for i, j in to_consider.priority_queue]) and \
                    neighbor not in set([j for i, j in considered.priority_queue]):
                distance_results[neighbor] = distance_results[current_node] + distance
                to_consider.add(distance, neighbor)
                path[neighbor] = current_node
            else:
                if distance_results[current_node] + distance < distance_results[neighbor]:
                    distance_results[neighbor] = distance_results[current_node] + distance
                    path[neighbor] = current_node

    return distance_results[destination],path


if __name__ == '__main__':
    k = reader('testdata.txt')
    source = 1
    sink = 4
    shortest_dist,path = find_shortest_path('testdata.txt', source, sink)
    print(shortest_dist)

    path_taken = [sink]

    while(sink in path.keys()):
        path_taken.append(path[sink])
        sink = path[sink]

    a = [str(i) for i in path_taken[::-1]]
    print('->'.join(a))
