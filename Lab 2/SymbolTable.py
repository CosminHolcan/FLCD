import string
from collections import deque

#bucketsNumber should be a prime number (statistics say it's better this way)

class SymbolTable():

    def __init__(self, bucketsNumber):
        self.__bucketsNumber = bucketsNumber
        self.__buckets = []
        for i in range(bucketsNumber) :
            self.__buckets.append(deque())

    def __hashFunction(self, element: string):
        sum = 0
        for character in element:
            sum = sum + ord(character)
        return sum % self.__bucketsNumber

    def pos(self, element):
        hashValue = self.__hashFunction(element)
        elementIndexBucket = 0
        for bucketElement in self.__buckets[hashValue]:
            if element == bucketElement :
                return (hashValue, elementIndexBucket)
            else :
                elementIndexBucket += 1
        self.__buckets[hashValue].append(element)
        return (hashValue, elementIndexBucket)
