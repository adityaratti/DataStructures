from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def print(self):
        for key, value in self.graph.items():
            print("Adjacency of Node {}".format(key))
            print('->'.join(map(str, value)))

    def bfs(self, start):
        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)

        while queue:
            s = queue.popleft()
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    def dfs(self, start):
        visited = set()

        stack = deque()
        stack.append(start)
        visited.add(start)

        while stack:
            s = stack.pop()
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)

# for directed graph
    def isCyclic(self):
        visited = [False] * (len(self.graph) + 1)
        recStack = [False] * (len(self.graph) + 1)

        for node in self.graph:
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True

        recStack[v] = False
        return False


# for undirected graph
    def is_cyclic_undirected(self):
        visited = [False] * len(self.graph)

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util_undirected(node, visited, -1):
                    return True
        return False
    
    def is_cyclic_util_undirected(self, v, visited, parent):
        visited[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util_undirected(neighbour, visited, v):
                    return True
                elif parent != neighbour:
                    return True
        
        return False





v = 5
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 4)


graph.print()

print("BFS of graph")
graph.bfs(0)

print("\nDFS of graph")
graph.dfs(0)