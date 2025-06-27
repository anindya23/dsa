import collections

class Solutions:

    def __init__(self):
        self.visited = set()

    # Using stack
    def dfs1(self, graph, node):
        stack = []
        stack.append(node)
        while stack:
            node = stack.pop(-1)
            print(node, end=' ')
            for neighbor in graph[node]:
                stack.append(neighbor)

    # Using recursion
    def dfs2(self, graph, node):
        if node not in self.visited:
            print(node, end=' ')
            self.visited.add(node)
            for neighbor in graph[node]:
                self.dfs2(graph, neighbor)


    # Using stack as queue
    def bfs1(self, graph, source):
        queue = [source]
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbor in graph[node]:
                queue.append(neighbor)

    # Using queue
    # def bfs2(self, graph, root):
    #     visited = set()
    #     dq = collections.deque([root])
    #     while dq:
    #         node = dq.popleft()
    #         visited.add(node)
    #         for neighbor in graph[node]:
    #             if neighbor not in visited:
    #                 dq.append(neighbor)
    #     print(visited)

    def bfs2(self, graph, node):
        visited = set()
        dq = collections.deque([node])
        while dq:
            node = dq.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dq.append(neighbor)


if __name__ == '__main__':
    graph1 = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['D', 'E'],
        'D': [],
        'E': []
    }

    graph2 = {
        0: [2, 1, 3],
        1: [0, 2],
        2: [0, 1, 4],
        3: [0],
        4: [2]
    }

    obj = Solutions()

    # obj.dfs1(graph1, "A")
    # obj.dfs2(graph1, "A")
    # obj.bfs1(graph1, "A")
    obj.bfs2(graph1, 'A')