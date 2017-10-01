from abc import ABCMeta, abstractmethod


class Banner(object):
    """
    Banner class
    """
    def __init__(self, string):
        self.string = string


    def showWithParen(self):
        print("(" + self.string + ")")


    def showWithAster(self):
        print("*" + self.string + "*")


class Print(metaclass=ABCMeta):
    """
    Print Interface
    """
    @abstractmethod
    def printWeak(self):
        pass


    @abstractmethod
    def printStrong(self):
        pass


class PrintBanner(Banner,Print):
    """
    PrintBanner class(Adapter)
    """
    def __init__(self, string):
        super().__init__(string)


    def printWeak(self):
        self.showWithParen()


    def printStrong(self):
        self.showWithAster()