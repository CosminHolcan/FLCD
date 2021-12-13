import copy

from Node import Node


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
                elif action == "acc":
                    print("Great success")
                    return phi
                else:
                    self.ActionReduce([alpha, beta, phi])
        except:
            print("Not great success")
            return

    def printTable(self, phi):
        table = [Node(0, self.parser.gramatica_imbogatita.starting_symbol, -1, -1)]
        currentIndexNode = 1
        current_father_index = 0
        for prod_index in range(len(phi)):
            prod = self.parser.gramatica_imbogatita.getProductionIndex(phi[prod_index])
            rhs = prod[1]
            next_father_index = None
            for index_rhs in range(len(rhs)):
                if prod_index != len(phi) - 1:
                    next_prod = self.parser.gramatica_imbogatita.getProductionIndex(phi[prod_index + 1])
                    next_father = next_prod[0][0]
                    if rhs[index_rhs] == next_father:
                        next_father_index = currentIndexNode
                if index_rhs != len(rhs) - 1:
                    currentNode = Node(currentIndexNode, rhs[index_rhs], current_father_index, currentIndexNode + 1)
                    table.append(currentNode)
                    currentIndexNode = currentIndexNode + 1
                else:
                    currentNode = Node(currentIndexNode, rhs[index_rhs], current_father_index, -1)
                    table.append(currentNode)
                    currentIndexNode = currentIndexNode + 1
            current_father_index = next_father_index
        print("Index     Value     Parent     RightSibling")
        for node in table:
            print(node.index, node.value, node.parent, node.rightSibling)
