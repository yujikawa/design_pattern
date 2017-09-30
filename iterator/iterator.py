from abc import ABCMeta, abstractmethod


class Aggregate(metaclass=ABCMeta):
    """
    Aggregate Interface
    """
    @abstractmethod
    def iterator(self)->object:
        pass


class Iterator(metaclass=ABCMeta):
    """
    Iterator Interface
    """
    @abstractmethod
    def hasNext(self)->bool:
        pass

    @abstractmethod
    def next(self)->object:
        pass



