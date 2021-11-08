class FiniteAutomaton:

    def __init__(self):
        self.__states = list()
        self.__alphabet = list()
        self.__transitions = dict()
        self.__finalStates = list()
        self.__initialState = 'q0'

    def readFromFile(self, fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
            self.__states = lines[0].split(":")[1].strip().split(",")
            self.__alphabet = self.__getAlphabetFromLine(lines[1])
            self.__initialState = lines[2].split(":")[1].strip()
            self.__transitions = self.__getTransitionsFromLine(lines[3])
            self.__finalStates = lines[4].split(":")[1].strip().split(",")
        file.close()

    def __getAlphabetFromLine(self, line):
        alphabet = list()
        content = line.split(":")[1]
        symbols = content.split(",")
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

    def __getTransitionsFromLine(self, line):
        content = line.split(":")[1]
        pairs = content.split(";")
        transitions = dict()
        for pair in pairs:
            firstPart = pair.split("->")[0]
            resultState = pair.split("->")[1].strip()
            initialState = firstPart.split(",")[0].strip()
            symbol = firstPart.split(",")[1].strip()
            allSymbols = list()
            if ".." in symbol:
                symbol = symbol.strip()
                first = symbol[0]
                last = symbol[-1]
                for i in range(ord(first), ord(last) + 1):
                    allSymbols.append(chr(i))
            #this can happens only if the symbol is space
            if symbol == "":
                symbol = ' '
            if len(allSymbols) == 0 :
                allSymbols.append(symbol)
            for symbol in allSymbols:
                transitions[(initialState, symbol)] = resultState
        return transitions

    def acceptsSequence(self, sequence):
        currentState = self.__initialState
        for symbol in sequence:
            if (currentState, symbol) in self.__transitions:
                currentState = self.__transitions[(currentState, symbol)]
            else:
                return False
        return currentState in self.__finalStates

    def getStates(self):
        return self.__states

    def getAlphabet(self):
        return self.__alphabet

    def getTransitions(self):
        return self.__transitions

    def getFinalStates(self):
        return self.__finalStates

    def getInitialState(self):
        return self.__initialState
