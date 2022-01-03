import copy

from Node import Node
from Table import Table


class ParserOutput:
    def __init__(self, parser):
        self.parser = parser
        self.parser.ColCan()

    def ActionShift(self, config):
        alpha, beta, phi = config
        head = copy.deepcopy(beta[0])
        s_m = copy.deepcopy(alpha[-1])
        S_j = copy.deepcopy(self.parser.table[s_m][head])
        alpha.append(head)
        alpha.append(S_j)
        del beta[0]

    def ActionReduce(self, config):
        alpha, beta, phi = config
        s_m = copy.deepcopy(alpha[-1])
        I = self.parser.table[s_m]["action"]
        move = self.parser.gramatica_imbogatita.getProductionIndex(I)
        A = move[0][0]
        result = move[1]
        index = len(result) - 1
        index_alpha = len(alpha) - 1
        ok = True
        while index >= 0:
            index_alpha = index_alpha - 1
            if index_alpha < 0:
                ok = False
                break
            x_m = alpha[index_alpha]
            index_alpha = index_alpha - 1
            if x_m != result[index]:
                ok = False
                break
            index = index - 1
        if not ok:
            raise "error"
        # alpha = alpha[:index_alpha + 1]
        del alpha[index_alpha + 1:]
        s_m_p = index_alpha
        s_j = self.parser.table[alpha[index_alpha]][A]
        alpha.append(A)
        alpha.append(s_j)
        phi.insert(0, I)

    def IsAccepted(self, word):
        try:
            alpha = [0]
            beta = word
            phi = list()
            while True:
                s_m = alpha[-1]
                action = self.parser.table[s_m]["action"]
                if action == "shift":
                    self.ActionShift([alpha, beta, phi])
                elif action == "acc" and beta==[]:
                    print("Great success")
                    return phi
                else:
                    self.ActionReduce([alpha, beta, phi])
        except:
            print("Not great success")
            return

    def parseProductions(self, productions):
        # terms = []
        table = Table()
        table.add(Node(productions[0][0][0], -1, -1))
        # first iteration
        for child_index in range(len(productions[0][1])):
            if child_index == 0:
                table.add(Node(productions[0][1][child_index], 0, -1))
            else:
                table.add(
                    Node(productions[0][1][child_index], 0, table.getIndexOfInfo(productions[0][1][child_index - 1])))

        for production in productions[1:]:
            current = production[0][0]
            children = production[1]
            parentIndex = table.getIndexOfInfo(current)
            for child_index in range(len(children)):
                if child_index == 0:
                    table.add(Node(children[0], parentIndex, -1))
                else:
                    table.add(Node(children[child_index], parentIndex, table.getIndexOfInfo(children[child_index - 1])))
        return table
