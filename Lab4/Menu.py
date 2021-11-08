from FA import FiniteAutomaton


class Menu:

    def __init__(self):
        self.__finiteAutomaton = FiniteAutomaton()

    def __readAutomatonFromFile(self):
        fileName = input("Name of file : ")
        self.__finiteAutomaton.readFromFile(fileName)

    def __printStates(self):
        result = ""
        for state in self.__finiteAutomaton.getStates():
            result += state + " "
        print(result)

    def __printAlphabet(self):
        result = ""
        for symbol in self.__finiteAutomaton.getAlphabet():
            result += symbol + " "
        print(result)

    def __printTransitions(self):
        result = "\n"
        transitions = self.__finiteAutomaton.getTransitions()
        for key in transitions:
            result += "(" + key[0] + ", " + key[1] + ")" + " -> " + transitions[key] + "\n"
        print(result)

    def __printInitialState(self):
        print(self.__finiteAutomaton.getInitialState())

    def __printFinalStates(self):
        result = ""
        for state in self.__finiteAutomaton.getFinalStates():
            result += state + " "
        print(result)

    def __acceptsSequence(self):
        sequence = input("sequence : ")
        result = self.__finiteAutomaton.acceptsSequence(sequence)
        if result:
            print("Accepted sequence")
        else:
            print("Sequence was not accepted")

    def run(self):
        commands = {
            "1": self.__readAutomatonFromFile,
            "2": self.__printStates,
            "3": self.__printAlphabet,
            "4": self.__printTransitions,
            "5": self.__printInitialState,
            "6": self.__printFinalStates,
            "7": self.__acceptsSequence,
            "8": exit
        }
        print("Command 1 : read from file")
        print("Command 2 : print all states ")
        print("Command 3 : print alphabet")
        print("Command 4 : print transitions")
        print("Command 5 : print initial state")
        print("Command 6 : print final states")
        print("Command 7 : check if a sequence is accepted")
        print("Command 8 : exit")
        while True:
            command = input("Please introduce command : ")
            if command in commands:
                commands[command]()
            else:
                print("Invalid command !")
