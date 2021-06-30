from graph import Graph

_SUCCESS = 0
_ERROR = 1


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
            if self._verify_not_double_no_terminal(rest):
                self.rules.append([no_terminal_base, expression])
                print(
                    f'Regla "{no_terminal_base} -> {expression}" agregada a la gramática')
                return _SUCCESS
            else:
                print(
                    f'ERROR: Regla "{no_terminal_base} -> {expression}" no corresponde a una gramática de operadores')
                return _ERROR
        else:
            print(
                f'ERROR: "{no_terminal_base}" no corresponde a un no-terminal')
            return _ERROR

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
                return _SUCCESS
        print(f'ERROR: "{simbol}" no es un símbolo no-terminal')
        return _ERROR

    def _is_no_terminal_in_productions(self, no_terminal):
        for elem in self.rules:
            if elem[0] == no_terminal:
                return True
        return False

    def _search_production(self, result):
        for elem in self.rules:
            base = elem[0]
            expression = elem[1]
            if result in expression:
                return base, expression
        return None, None

    def build(self):
        """
        Build
        :return:
        """
        self._set_f_and_g()
        print("Analizador sintáctico construido.")

        print("Valores para f:")
        for key, value in self.f.items():
            print("    ", key, ":", value)

        print("Valores para g:")
        for key, value in self.g.items():
            print("    ", key, ":", value)

    def _set_f_and_g(self):
        for vertex in self.graph.graph:
            self.f[vertex[0][2:]] = 0
            self.g[vertex[0][2:]] = 0
        f = self.graph.longest_path()
        for elem in f:
            name = elem[0]
            if name[0] == "f":
                self.f[name[2:]] = elem[1]
            else:
                self.g[name[2:]] = elem[1]

    def parse(self, array):
        if self.f and self.g:
            heap = []
            entry = []
            action = []
            expressions = []
            array.insert(0, '$')
            array.append('$')
            expression = self._add_exp_with_precedence(array).split(" ")
            while len(array) > 2:
                p = array.pop(0)
                entry.append(p)
                e = array[0]
                if self.f[p] <= self.g[e]:
                    heap.append(e)
                else:
                    result=""
                    while True:
                        x = heap.pop()
                        if self.f[heap[0]] < self.g[x]:
                            break
                        result = result + x + " "
                    transformation = self._convert(result)
                    if transformation:
                        heap.append(transformation)
                        print(heap)
                        print(entry)
                        print(expression)
        else:
            print("ERROR: Aún no se ha construido el analizador sintáctico")

    def _convert(self, result):
        base, expression = self._search_production(result)
        return base

    def _add_exp_with_precedence(self, array):
        expression = ""
        for i in range(len(array) - 1):
            a = array[i]
            b = array[i + 1]
            if self.f[a] <= self.g[b]:
                expression = expression + a + " < "
            else:
                expression = expression + a + " > "
        expression = expression + array[-1]
        return expression

    def _verify_not_double_no_terminal(self, rest):
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
