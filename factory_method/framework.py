from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    """
    Product class
    """
    @abstractmethod
    def use(self):
        pass


class Factory(object):
    """
    Factory class
    """

    def create(self, owner):
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p


    @abstractmethod
    def createProduct(self, owner):
        pass


    @abstractmethod
    def registerProduct(self, product):
        pass