from Grammar import Grammar

if __name__ == "__main__":
    grammar = Grammar()
    grammar.readFromFile("g2.txt")
    print("Checked ", grammar.checkCFG())
    print(grammar)
    print(grammar.getProductionsByNonterminal("Integer"))
