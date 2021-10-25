from SymbolTable import SymbolTable
from Utils import check_string_start_with_delimiter, check_if_constant, check_if_identifier


class Scanner:

    def __init__(self, programFileName, stIdentifiersFileName, stConstantsFileName, pifFileName):
        self.__programFileName = programFileName
        self.__stIdentifiersFileName = stIdentifiersFileName
        self.__stConstantsFileName = stConstantsFileName
        self.__pifFileName = pifFileName
        self.__pif: list = []
        self.__stIdentifiers: SymbolTable = SymbolTable(17)
        self.__stConstants: SymbolTable = SymbolTable(17)

    def __writeToFiles(self):
        with open(self.__stIdentifiersFileName, 'w') as file:
            file.write("Identifiers\n")
            file.write(str(self.__stIdentifiers))
        file.close()
        with open(self.__stConstantsFileName, 'w') as file:
            file.write("Constants\n")
            file.write(str(self.__stConstants))
        file.close()
        with open(self.__pifFileName, 'w') as file:
            toWrite = ""
            for (typeOfToken, pos) in self.__pif:
                toWrite += typeOfToken + " : " + str(pos) + "\n"
            file.write(toWrite)
        file.close()

    def run(self):
        with open(self.__programFileName, 'r') as file:
            indexLine = 0
            lines = file.readlines()
            for line in lines:
                indexLine += 1
                line = line.strip()
                if len(line) >= 2 and line[0] == '/' and line[1] == '/':
                    continue
                while line:
                    line = line.strip()
                    copy_line = line
                    delimiter = check_string_start_with_delimiter(line)
                    if delimiter:
                        self.__pif.append((delimiter, -1))
                        line = line.split(delimiter, 1)[1]
                        continue
                    while copy_line and not check_string_start_with_delimiter(copy_line):
                        copy_line = copy_line[1:]
                    if copy_line:
                        delimiter = check_string_start_with_delimiter(copy_line)
                        currentToken = line.split(delimiter, 1)[0]
                        line = copy_line
                    else:
                        currentToken = line
                        line = ""
                    currentToken = currentToken.strip(" ")
                    if check_if_constant(currentToken):
                        pos = self.__stConstants.pos(currentToken)
                        self.__pif.append(("constant", pos))
                        continue
                    if check_if_identifier(currentToken):
                        pos = self.__stIdentifiers.pos(currentToken)
                        self.__pif.append(("identifier", pos))
                        continue
                    print("Error at line " + str(indexLine) + " with token " + currentToken)
                    return
            self.__writeToFiles()
