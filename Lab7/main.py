from Grammar import Grammar
from Parser import LRParser
from ParserOutput import ParserOutput

def readPIF(pifFile):
    result = []
    with open(pifFile, 'r') as file:
        lines = file.readlines()
        for line in lines :
            rhs = line.split(":")[0].strip()
            result.append(rhs)
    return result

if __name__ == "__main__":
    grammar = Grammar()
    grammar.readFromFile("g2.txt")
    pif = readPIF("pif1.txt")
    lrp = LRParser(grammar)
    # print(lrp.ColCan())
    # print(grammar.productionsAsList())
    # for e in lrp.table:
    #     print(e)
    # print(lrp.gramatica_imbogatita.getProductionIndex(0))
    po = ParserOutput(lrp)
    # phi = po.IsAccepted(["declare", "int", "identifier", ";", "declare", "int", "identifier", ";"])
    phi = po.IsAccepted(pif)
    productions = []
    for production_id in phi:
        productions.append(lrp.gramatica_imbogatita.getProductionIndex(production_id))
    # print(po.parseProductions(productions))
    # with open("out1.txt", 'w') as file:
    #     file.write(str(po.parseProductions(productions)))
    # file.close()
    # po.IsAccepted(["a", "a"])
