from framework import *


class IDCard(Product):
    """
    IDcard class
    """
    def __init__(self, owner):
        print("I create a {}'s card.".format(owner))
        self.owner = owner


    def use(self):
        print("I use {}'s card.".format(self.owner))


class IDCardFactory(Factory):
    """
    IDCardFactory class
    """
    def __init__(self):
        self.owners = []


    def createProduct(self, owner):
        return IDCard(owner)


    def registerProduct(self, product):
        self.owners.append(product.owner)