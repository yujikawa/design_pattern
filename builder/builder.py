from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    """
    Builder interface
    """
    @abstractmethod
    def makeTitle(self, title):
        pass


    @abstractmethod
    def makeString(self, str):
        pass


    @abstractmethod
    def makeItems(self, items):
        pass


    @abstractmethod
    def close(self):
        pass



class TextBuilder(Builder):
    """
    TextBuilder class
    """
    def __init__(self):
        self.buffer = []


    def makeTitle(self, title):
        self.buffer.append("===================¥n")
        self.buffer.append("「{}」¥n".format(title))
        self.buffer.append("¥n")


    def makeString(self, str):
        self.buffer.append("▪️{}¥n".format(str))
        self.buffer.append("¥n")


    def makeItems(self, items):
        for item in items:
            self.buffer.append("・{}".format(item))

        self.buffer.append("¥n")


    def close(self):
        self.buffer.append("===================¥n")


    def getResult(self):
        return "".join(self.buffer)


class HtmlBuilder(Builder):
    """
    HtmlBuilder class
    """
    def __init__(self):
        self.filename = ""
        self.writer = ""


    def makeTitle(self, title):
        self.filename = "{}.html".format(title)
        self.f = open(self.filename, "w")
        self.f.write("<html><head><title>{}</title><head><body>".format(title))
        self.f.write("<h1>{}</h1>".format(title))


    def makeString(self, str):
        self.f.write("<p>{}</p>".format(str))


    def makeItems(self, items):
        self.f.write("<ul>")
        for item in items:
            self.f.write("<li>{}</li>".format(item))

        self.f.write("</ul>")


    def close(self):
        self.f.write("</body></html>")
        self.f.close()


    def getResult(self):
        return self.filename


class Director(object):
    """
    Director class
    """
    def __init__(self, builder):
        self.builder = builder


    def construct(self):
        self.builder.makeTitle("Greeting")
        self.builder.makeString("From morning to noon")
        self.builder.makeItems(["Good morning", "Hello"])
        self.builder.makeString("At night")
        self.builder.makeItems(["Good evening", "Good night", "Good bye"])
        self.builder.close()


