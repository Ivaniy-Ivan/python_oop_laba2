class User:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def getName(self):
        return self.__name

    def getSurn(self):
        return self.__surname

    def setName(self, name):
        self.__name = name

    def setSurn(self, surname):
        self.__surname = surname