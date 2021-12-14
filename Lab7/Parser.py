from Grammar import Grammar
import copy


class LRParser:

    def __init__(self, grammar: Grammar):
        self.gramatica_imbogatita = grammar

        new_start_symbol = "start"
        self.gramatica_imbogatita.nonterminals.append(new_start_symbol)
        self.gramatica_imbogatita.productions[new_start_symbol,] = [[self.gramatica_imbogatita.starting_symbol]]
        self.initial_starting_symbol = grammar.starting_symbol
        self.gramatica_imbogatita.starting_symbol = new_start_symbol

        self.states = []
        self.table = []

    def closure(self, I):
        C = copy.deepcopy(I)
        changed = True
        while changed:
            changed = False
            for elem in C:
                # A = elem[0]
                result = elem[1]
                if '.' in result:
                    index_punct = result.index('.')
                    if index_punct + 1 < len(result) and result[
                        index_punct + 1] in self.gramatica_imbogatita.nonterminals:
                        productions_B = self.gramatica_imbogatita.getProductionsByNonterminal(result[index_punct + 1])
                        for production in productions_B:
                            new_elem = [result[index_punct + 1]]
                            new_elem_rhs = ["."]
                            new_elem_rhs.extend(production)
                            new_elem.append(new_elem_rhs)
                            if new_elem not in C:
                                C.append(new_elem)
                                changed = True
        return C

    def goto(self, s, X):
        copy_s = copy.deepcopy(s)
        productions_found = []
        for production in copy_s:
            rhs = production[1]
            if "." in rhs:
                dot_index = rhs.index(".")
                if dot_index + 1 <= len(rhs) - 1 and rhs[dot_index + 1] == X:
                    del rhs[dot_index]
                    rhs.insert(dot_index + 1, ".")
                    productions_found.append(production)

        if productions_found:
            return self.closure(productions_found)

    def ColCan(self):
        self.states = []
        self.table = [{}]
        s_0 = self.closure([[self.gramatica_imbogatita.starting_symbol, [".", self.initial_starting_symbol]]])
        self.table[-1]['action'] = self.determineAction((s_0))
        self.states.append(s_0)
        C = [s_0]
        C_changed = True
        while C_changed:
            C_changed = False
            for any_state in C:
                for any_symbol in self.gramatica_imbogatita.nonterminals + self.gramatica_imbogatita.alphabet:
                    new_state = self.goto(any_state, any_symbol)
                    if new_state:
                        if new_state not in C:
                            index = C.index(any_state)
                            self.table.append({})
                            self.states.append(new_state)
                            self.table[index][any_symbol] = len(self.states) - 1
                            self.table[-1]['action'] = self.determineAction(new_state)
                            C.append(new_state)
                            C_changed = True
                        else:
                            index = C.index(any_state)
                            index_already_existent_state = C.index(new_state)
                            self.table[index][any_symbol] = index_already_existent_state

        return C  # = self.states

    def isProductionShift(self, production):
        if '.' in production[1]:
            if production[1].index('.') < len(production[1]) - 1:
                return True
        return False

    def isProductionReduce(self, production):
        if '.' in production[1]:
            if production[1].index('.') == len(production[1]) - 1 and production[0] != self.gramatica_imbogatita.starting_symbol:
                new_production = copy.deepcopy(production)
                new_production[1].remove('.')
                new_production[0] = (new_production[0],)
                return self.gramatica_imbogatita.productionsAsList().index(new_production)
        return

    def isProductionAccept(self, production):
        if '.' in production[1]:
            if production[0] == self.gramatica_imbogatita.starting_symbol and production[1] == [self.initial_starting_symbol, '.']:
                return True
        return False

    def determineAction(self, state):
        for production in state:
            if self.isProductionShift(production):
                return "shift"

        for production in state:
            result = self.isProductionReduce(production)
            if result != None:
                return result

        for production in state:
            if self.isProductionAccept(production):
                return "acc"

        return 'error'
