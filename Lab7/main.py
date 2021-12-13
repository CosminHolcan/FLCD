from Grammar import Grammar
from Parser import LRParser
from ParserOutput import ParserOutput

if __name__ == "__main__":
    grammar = Grammar()
    grammar.readFromFile("g1.txt")
    lrp = LRParser(grammar)
    # print(lrp.ColCan())
    # print(grammar.productionsAsList())
    # for e in lrp.table:
    #     print(e)
    print(lrp.gramatica_imbogatita.getProductionIndex(0))
    po = ParserOutput(lrp)
    phi = po.IsAccepted(["a", "b", "b", "c"])
    po.printTable(phi)
    # po.IsAccepted(["a", "a"])
