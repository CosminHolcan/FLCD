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
    productions = []
    for production_id in phi:
        productions.append(lrp.gramatica_imbogatita.getProductionIndex(production_id))
    print(po.parseProductions(productions))
    with open("table.txt", 'w') as file:
        file.write(str(po.parseProductions(productions)))
    file.close()
    # po.IsAccepted(["a", "a"])
