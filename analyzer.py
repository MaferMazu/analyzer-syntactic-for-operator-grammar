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

    def topological_order(self):
        """
        Topological order
        :return:
        """
        visited = [False for i in range(len(self.graph))]
        f = [0 for i in range(len(self.graph))]
        counter = len(self.graph) + 1
        for i in range(len(self.graph)):
            if not visited[i]:
                new_counter = self._recursive_dfs(visited, f, counter, i)
                counter = new_counter
        return f

    def _recursive_dfs(self, visited, f, counter, index):
        visited[index] = True
        adjs = self.graph[index][1]
        for elem in adjs:
            name = elem
            elem_index = self._get_index_by_name(name)
            if not visited[elem_index]:
                self._recursive_dfs(visited, f, counter, elem_index)
        new_counter = counter - 1
        f[index] = new_counter
        return new_counter

def _verify_not_double_no_terminal(rest):
    """
    Verify not double no terminal
    :param rest:
    :return:
    """
    prev_no_terminal = False
    for elem in rest:
        if elem.isupper() and not prev_no_terminal:
            prev_no_terminal = True
        elif not elem.isupper():
            prev_no_terminal = False
        else:
            return False
    return True


class Analyzer:
    """
    Analyzer syntactic for operator grammar
    """

    def __init__(self):
        """Init"""
        self.graph = Graph()
        self.rules = []
        self.init = None
        self.f={}
        self.g={}

    def add_rule(self, array):
        """
        Add rule
        :param array:
        :return: T success, F error
        """
        no_terminal_base = array[0]
        rest = array[1:]
        if no_terminal_base.isupper():
            expression = " ".join(rest)
            if _verify_not_double_no_terminal(rest):
                self.rules.append([no_terminal_base, expression])
                print(
                    f'Regla "{no_terminal_base} -> {expression}" agregada a la gramática')
            else:
                print(
                    f'ERROR: Regla "{no_terminal_base} -> {expression}" no corresponde a una gramática de operadores')

    def add_precedence(self, array):
        """
        Add precedence
        :param array:
        :return:
        """
        a = array[0]
        b = array[2]
        if array[1] == "<":
            self.graph.add_adj(name=f"g_{b}", adj=f"f_{a}")
            print(f'"{a}" tiene menor precedencia que "{b}"')
        elif array[1] == ">":
            self.graph.add_adj(name=f"f_{a}", adj=f"g_{b}")
            print(f'"{a}" tiene mayor precedencia que "{b}"')
        elif array[1] == "=":
            self.graph.add_adj(name=f"g_{b}", adj=f"f_{a}")
            self.graph.add_adj(name=f"f_{a}", adj=f"g_{b}")
            print(f'"{a}" tiene igual precedencia que "{b}"')

    def set_init(self, simbol):
        """
        Set init
        """
        if simbol.isupper():
            if self._is_no_terminal_in_productions(simbol):
                self.init = simbol
                print(
                    f'"{simbol}" es ahora el símbolo inicial de la gramática')
                return
        print(f'ERROR: "{simbol}" no es un símbolo no-terminal')

    def _is_no_terminal_in_productions(self, no_terminal):
        for elem in self.rules:
            if elem[0] == no_terminal:
                return True
        return False

    def _search_production(self, simbol):
        for elem in self.rules:
            base = elem[0]
            expression = elem[1]
            if simbol in expression:
                return base, expression
        return None, None

    def build(self):
        """
        Build
        :return:
        """
        self._set_functions_by_topological_order()
        print("Analizador sintáctico construido con orden topológico.")

        print("Valores para f:")
        for key, value in self.f.items():
            print("    ", key, ":", value)

        print("Valores para g:")
        for key, value in self.g.items():
            print("    ", key, ":", value)

    def _set_functions_by_topological_order(self):
        for elem in self.graph.graph:
            simbol = elem[0][2:]
            self.g[simbol] = 0
            self.f[simbol] = 0
        order = self.graph.topological_order()
        counter = len(self.graph)
        for elem in order:
            name = self.graph.graph[elem - 1][0]
            if name[0] == 'f':
                self.f[name[2:]] = counter
                new_counter = counter - 1
                counter = new_counter

            else:
                self.g[name[2:]] = counter
                new_counter = counter - 1
                counter = new_counter
