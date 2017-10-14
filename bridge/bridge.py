from abc import ABCMeta, abstractmethod


class Display(object):
    """
    Display class
    """
    def __init__(self, impl):
        self.impl = impl


    def open(self):
        self.impl.rawOpen()


    def print(self):
        self.impl.rawPrint()


    def close(self):
        self.impl.rawClose()


    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    """
    CountDisplay class
    """
    def __init__(self, impl):
        super(CountDisplay, self).__init__(impl)


    def multiDisplay(self, times):
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class DisplayImpl(metaclass=ABCMeta):
    """
    DisplayImpl class
    """
    @abstractmethod
    def rawOpen(self):
        pass


    @abstractmethod
    def rawPrint(self):
        pass


    @abstractmethod
    def rawClose(self):
        pass


class StringDisplayImpl(DisplayImpl):
    """
    StringDisplayImpl class
    """
    def __init__(self, string):
        self.string = string
        self.width = len(string)


    def rawOpen(self):
        self._printLine()


    def rawPrint(self):
        print("|{}|".format(self.string))


    def rawClose(self):
        self._printLine()


    def _printLine(self):
        print("+","-"*self.width,"+")