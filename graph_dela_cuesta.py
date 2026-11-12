from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        # Undirected graph: add the connection in both directions
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = set()
        result = []

        def visit(vertex):
            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return result


# Graph based on the distinct letters in DELA CUESTA
graph = Graph()

for letter in ["D", "E", "L", "A", "C", "U", "S", "T"]:
    graph.add_vertex(letter)

# Connections between vertices
edges = [
    ("D", "E"),
    ("D", "L"),
    ("E", "A"),
    ("E", "C"),
    ("L", "U"),
    ("L", "T"),
    ("A", "S"),
    ("A", "T"),
    ("C", "S"),
    ("U", "T"),
    ("S", "T"),
]

for source, destination in edges:
    graph.add_edge(source, destination)


print("GRAPH - DELA CUESTA")
print("BFS:", " - ".join(graph.bfs("D")))
print("DFS:", " - ".join(graph.dfs("D")))
