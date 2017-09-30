from iterator import Aggregate, Iterator


class Book(object):
    """
    Book class
    """
    def __init__(self,name):
        self.name = name


class BookShelf(Aggregate):
    """
    BookShelf class
    """
    last = 0
    def __init__(self):
        self.books = []


    def appendBook(self, book):
        self.books.append(book)
        self.last += 1


    def iterator(self):
        return BookShelfIterator(self)


class BookShelfIterator(Iterator):
    """
    BookShelfIterator class
    """
    def __init__(self, bookShelf):
        self.bookShelf = bookShelf
        self.index = 0


    def hasNext(self):
        if self.index < self.bookShelf.last:
            return True
        else:
            return False


    def next(self):
        book = self.bookShelf.books[self.index]
        self.index += 1
        return book


if __name__ == "__main__":
    bookShelf = BookShelf()
    bookShelf.appendBook(Book("Around the World in 80 Days"))
    bookShelf.appendBook(Book("Bible"))
    bookShelf.appendBook(Book("Cinderella"))
    bookShelf.appendBook(Book("Daddy-Long-Legs"))
    it = bookShelf.iterator()
    while(it.hasNext()):
        book = it.next()
        print(book.name)

