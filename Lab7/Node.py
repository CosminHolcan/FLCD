class Node:
    def __init__(self, info, parent, rightSibling):
        self.info = info
        self.parent = parent
        self.rightSibling = rightSibling

    def __str__(self):
        return self.format(str(self.info), 25) + self.format(str(self.parent), 10) + \
               self.format(str(self.rightSibling), 15)

    def format(self, text, nrChars):
        while len(text) <= nrChars:
            text += " "
        return text
