from abc import ABCMeta, abstractmethod


class AbstractDisplay(metaclass=ABCMeta):
    """
    AbstractDisplay class
    """
    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()


    @abstractmethod
    def open(self):
        pass


    @abstractmethod
    def print(self):
        pass


    @abstractmethod
    def close(self):
        pass


class CharDisplay(AbstractDisplay):
    """
    CharDisplay class
    """

    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print("<<",end="")

    def print(self):
        print(self.ch,end="")

    def close(self):
        print(">>")