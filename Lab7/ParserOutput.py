import copy

from Node import Node


class Row:
    def __init__(self, info, parent, rightSibling):
        self.info = info
        self.parent = parent
        self.rightSibling = rightSibling

    def __str__(self):
        return self.format(str(self.info), 15) + self.format(str(self.parent), 9) + \
               self.format(str(self.rightSibling), 8)

    def format(self, text, nrChars):
        while len(text) != nrChars:
            text += " "
        return text


class Table:
    def __init__(self):
        self.rows = []

    def add(self, row):
        self.rows.append(row)

    def getIndexOfInfo(self, symbol):
        # [::-1] face reverse de lista, cautam de la coata la inceput ca sa gasim ultima aparitie.
        for row_index in range(len(self.rows))[::-1]:
            if self.rows[row_index].info == symbol:
                return row_index

    def format(self, text, nrChars):
        while len(text) != nrChars:
            text += " "
        return text

    def __str__(self):
        result = "Index   Info           Parent   RightSibling\n"
        for row_index in range(len(self.rows)):
            result += self.format(str(row_index), 8) + str(self.rows[row_index]) + "\n"
        return result


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

    def parseProductions(self, productions):
        # terms = []
        table = Table()
        print(productions)
        table.add(Row(productions[0][0][0], -1, -1))
        # first iteration
        for child_index in range(len(productions[0][1])):
            if child_index == 0:
                table.add(Row(productions[0][1][child_index], 0, -1))
            else:
                table.add(
                    Row(productions[0][1][child_index], 0, table.getIndexOfInfo(productions[0][1][child_index - 1])))

        for production in productions[1:]:
            current = production[0][0]
            children = production[1]
            parentIndex = table.getIndexOfInfo(current)
            pos = 0
            for child_index in range(len(children)):
                if child_index == 0:
                    table.add(Row(children[0], parentIndex, -1))
                else:
                    table.add(Row(children[child_index], parentIndex, table.getIndexOfInfo(children[child_index - 1])))
        return table
