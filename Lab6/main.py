from Grammar import Grammar
from Parser import LRParser


if __name__=="__main__":
    grammar = Grammar()
    grammar.readFromFile("g1.txt")
    lrp = LRParser(grammar)
    print(lrp.ColCan() == [[['start', ['.', 'S']], ['S', ['.', 'a', 'A']]], [['start', ['S', '.']]], [['S', ['a', '.', 'A']], ['A', ['.', 'b', 'A']], ['A', ['.', 'c']]], [['S', ['a', 'A', '.']]], [['A', ['b', '.', 'A']], ['A', ['.', 'b', 'A']], ['A', ['.', 'c']]], [['A', ['c', '.']]], [['A', ['b', 'A', '.']]]])
    print(lrp.states == [[['start', ['.', 'S']], ['S', ['.', 'a', 'A']]], [['start', ['S', '.']]], [['S', ['a', '.', 'A']], ['A', ['.', 'b', 'A']], ['A', ['.', 'c']]], [['S', ['a', 'A', '.']]], [['A', ['b', '.', 'A']], ['A', ['.', 'b', 'A']], ['A', ['.', 'c']]], [['A', ['c', '.']]], [['A', ['b', 'A', '.']]]])
    print(lrp.table == [{'S': 1, 'a': 2}, {}, {'A': 3, 'b': 4, 'c': 5}, {}, {'A': 6, 'b': 4, 'c': 5}, {}, {}])
