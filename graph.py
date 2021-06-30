class Graph:
    """
    Graph
    """

    def __init__(self, graph=[]):
        self.graph = graph

    def __len__(self):
        return len(self.graph)

    def add_vertex(self, name: str, adj=[]):
        """
        Add vertex
        :param name:
        :param adj:
        """
        self.graph.append([name, adj])

    def add_adj(self, name: str, adj: str):
        """
        Add Adj
        :param name:
        :param adj:
        :return:
        """
        index = self._get_index_by_name(name)
        adj_index = self._get_index_by_name(adj)
        if adj_index == -1:
            self.add_vertex(adj)
        if index == -1:
            self.add_vertex(name, [adj])
        else:
            self.graph[index][1].append(adj)

    def _get_index_by_name(self, name):
        for i in range(len(self.graph)):
            if self.graph[i][0] == name:
                return i
        return -1

    def longest_path(self):
        """
        Longest path
        :return:
        """
        f=[]
        for i in range(len(self.graph)):
            count = 0
            for vertex in self.graph[i][1]:
                count = 1
                visited = [False for i in range(len(self.graph))]
                visited[i] = True
                index = self._get_index_by_name(vertex)
                counter = self._recursive_dfs(visited, count, index)
                if counter > count:
                    count = counter
            f.append([self.graph[i][0], count])
        return f

    def _recursive_dfs(self, visited, counter, index):
        visited[index] = True
        adjs = self.graph[index][1]
        for elem in adjs:
            name = elem
            elem_index = self._get_index_by_name(name)
            if not visited[elem_index]:
                self._recursive_dfs(visited, counter+1, elem_index)
        return counter