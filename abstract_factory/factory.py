from abc import ABCMeta, abstractmethod


### abstract classes
class Item(metaclass=ABCMeta):
    """
    Item class
    """
    def __init__(self, caption):
        self.caption = caption


    @abstractmethod
    def makeHTML(self):
        pass



class Link(Item, metaclass=ABCMeta):
    """
    Link class
    """
    def __init__(self, caption, url):
        super(Link, self).__init__(caption)
        self.url = url



class Tray(Item, metaclass=ABCMeta):
    """
    Tray class
    """
    def __init__(self, caption):
        self.tray = []
        super(Tray, self).__init__(caption)


    def add(self, item):
        self.tray.append(item)


class Page(metaclass=ABCMeta):
    """
    Page class
    """
    def __init__(self, title, author):
        self.content = []
        self.title = title
        self.author = author


    def add(self, item):
        self.content.append(item)


    def output(self):
        try:
            filename = self.title + ".html"
            with open(filename, "w") as f:
                f.write(self.makeHTML())
                print("{} created.".format(filename))

        except IOError as e:
            print(e)


    @abstractmethod
    def makeHTML(self):
        pass


class Factory(metaclass=ABCMeta):
    """
    Factory class
    """
    @classmethod
    def getFactory(cls, classname):
        factory = None
        try:
            factory = eval(classname)()
        except Exception as e:
            print("Not found {}. Exception={}".format(classname, e))

        return factory


    @abstractmethod
    def createLink(self, caption, url):
        pass


    @abstractmethod
    def createTray(self, caption):
        pass


    @abstractmethod
    def createPage(self, title, author):
        pass


### Implementation classes
class ListFactory(Factory):
    """
    ListFactory class
    """
    def createLink(self, caption, url):
        return ListLink(caption, url)


    def createTray(self, caption):
        return ListTray(caption)


    def createPage(self, title, author):
        return ListPage(title, author)


class ListLink(Link):
    """
    ListLink class
    """
    def __init__(self, caption, url):
        super(ListLink, self).__init__(caption, url)


    def makeHTML(self):
        return "<li><a href='{}'>{}</a></li>".format(self.url, self.caption)


class ListTray(Tray):
    """
    ListTray class
    """
    def __init__(self, caption):
        super(ListTray, self).__init__(caption)


    def makeHTML(self):
        buffer = []
        buffer.append("<li>")
        buffer.append("{}".format(self.caption))
        buffer.append("<ul>")
        for item in self.tray:
            buffer.append(item.makeHTML())
        buffer.append("</ul>")
        buffer.append("</li>")
        return "".join(buffer)


class ListPage(Page):
    """
    ListPage class
    """
    def __init__(self, title, author):
        super(ListPage, self).__init__(title, author)


    def makeHTML(self):
        buffer = []
        buffer.append("<html><head><title>{}</title></head>".format(self.title))
        buffer.append("<body>")
        buffer.append("<h1>{}</h1>".format(self.title))
        buffer.append("<ul>")
        for item in self.content:
            buffer.append(item.makeHTML())
        buffer.append("</ul>")
        buffer.append("<hr><address>{}</address>".format(self.author))
        buffer.append("</body></html>")
        return "".join(buffer)
