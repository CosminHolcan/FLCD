class Node:
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
