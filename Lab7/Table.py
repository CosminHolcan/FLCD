class Table:
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def getIndexOfInfo(self, symbol):
        for node_index in range(len(self.nodes))[::-1]:
            if self.nodes[node_index].info == symbol:
                return node_index

    def format(self, text, nrChars):
        while len(text) != nrChars:
            text += " "
        return text

    def __str__(self):
        result = "Index   Info           Parent   RightSibling\n"
        for node_index in range(len(self.nodes)):
            result += self.format(str(node_index), 8) + str(self.nodes[node_index]) + "\n"
        return result