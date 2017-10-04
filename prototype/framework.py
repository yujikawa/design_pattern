from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Product(metaclass=ABCMeta):
    """
    Product class
    """
    @abstractmethod
    def use(self):
        pass


    @abstractmethod
    def createClone(self):
        pass


class Manager(object):
    """
    Manager class
    """
    def __init__(self):
        self.showcase = {}


    def register(self, name, proto):
        self.showcase.update({name:proto})


    def create(self, protoname):
        p = self.showcase.get(protoname, None)
        return p.createClone()


class MessageBox(Product):
    """
    MessageBox class
    """
    def __init__(self, decochar):
        self._decochar = decochar


    def use(self, s):
        print(self._decochar * (len(s)+len(self._decochar * 2)))
        print("{d}{s}{d}".format(d=self._decochar, s=s))
        print(self._decochar * (len(s)+len(self._decochar * 2)))


    def createClone(self):
        p = None
        try:
            p = deepcopy(self)
        except CloneNotSupportedException as e:
            print(e)

        return p


class UnderlinePen(Product):
    """
    UnderlinePen class
    """
    def __init__(self, ulchar):
        self._ulchar = ulchar


    def use(self, s):
        print(s)
        print(self._ulchar * len(s))


    def createClone(self):
        p = None
        try:
            p = deepcopy(self)
        except CloneNotSupportedException as e:
            print(e)

        return p


class CloneNotSupportedException(Exception):
    pass