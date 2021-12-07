from Grammar import Grammar
from Parser import LRParser


if __name__ == "__main__":
    grammar = Grammar()
    grammar.readFromFile("g1.txt")
    lrp = LRParser(grammar)
    print(lrp.ColCan())
    for e in lrp.table:
        print(e)
