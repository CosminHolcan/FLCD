class Grammar:

    def __init__(self):
        self.nonterminals = list()
        self.alphabet = list()
        self.productions = dict()
        self.starting_symbol = "S"

    def readFromFile(self, fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
            self.nonterminals = lines[0].split(":")[1].strip().split("|")
            self.alphabet = self.__getAlphabetFromLine(lines[1])
            self.starting_symbol = lines[2].split(":")[1].strip()
            self.productions = self.__getProductionsFromLines(lines[4:])
        file.close()

    def __getAlphabetFromLine(self, line):
        alphabet = list()
        content = line.split(":")[1]
        symbols = content.split("|")
        for symbol in symbols:
            if ".." in symbol:
                symbol = symbol.strip()
                first = symbol[0]
                last = symbol[-1]
                for i in range(ord(first), ord(last) + 1):
                    alphabet.append(chr(i))
                continue
            if symbol == " ":
                alphabet.append(symbol)
                continue
            symbol = symbol.strip()
            alphabet.append(symbol)
        return alphabet

    def __getProductionsFromLines(self, lines):
        productions = dict()
        for line in lines:
            nonterminalsLHS = line.split("->")[0].strip().split(" ")
            for index in range(len(nonterminalsLHS)):
                nonterminalsLHS[index] = nonterminalsLHS[index].strip()
            nonterminalsLHS = tuple(nonterminalsLHS)
            resultsRHS = line.split("->")[1].split("|")
            for result in resultsRHS:
                if ".." in result:
                    result = result.strip()
                    firstChar = result[0]
                    secondChar = result[-1]
                    if nonterminalsLHS not in productions.keys():
                        productions[nonterminalsLHS] = list()
                    for i in range(ord(firstChar), ord(secondChar) + 1):
                        productions[nonterminalsLHS].append([chr(i)])
                        # productions.append((nonterminalsLHS,), [chr(i)])
                    continue
                result = result.strip().split(" ")
                for index in range(len(result)):
                    result[index] = result[index].strip()
                    if result[index] == 'empty_space':
                        result[index] = ' '
                if nonterminalsLHS not in productions.keys():
                    productions[nonterminalsLHS] = list()
                productions[nonterminalsLHS].append(result)
        return productions

    def checkCFG(self):
        for key in self.productions.keys():
            if len(key) != 1:
                return False
            for nonterminal in key:
                if nonterminal not in self.nonterminals:
                    return False
            for result in self.productions[key]:
                for symbol in result:
                    if symbol not in self.nonterminals and symbol not in self.alphabet:
                        return False
        return True

    def getProductionsByNonterminal(self, nonTerminal):
        if nonTerminal not in self.nonterminals:
            print("Not found nonterminal")
            return
        toReturn = list()
        for key in self.productions.keys():
            if nonTerminal in key:
                toReturn.extend(self.productions[key])
        if len(toReturn) != 0:
            return toReturn
        print("Not found productions with nonterminal " + nonTerminal)

    def __str__(self):
        toReturn = "nonterminals : " + ", ".join(self.nonterminals) + "\n"
        toReturn += "alphabet : " + ", ".join(self.alphabet) + "\n"
        productionsString = "productions : " + "\n"
        for key in self.productions.keys():
            productionsString += " ".join(key) + " -> "
            for index in range(len(self.productions[key])):
                productionsString += " ".join(self.productions[key][index])
                if index != len(self.productions[key]) - 1:
                    productionsString += " | "
            productionsString += "\n"
        toReturn += productionsString
        toReturn += "starting symbol : " + self.starting_symbol + "\n"
        return toReturn

    def getProductionIndex(self, index):
        return self.productionsAsList()[index]

    def productionsAsList(self):
        productionList = []
        for key in self.productions:
            for production in self.productions[key]:
                productionList.append([key, production])

        return  productionList