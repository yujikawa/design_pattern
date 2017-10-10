import sys
from builder import TextBuilder, HtmlBuilder, Director


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Please input: ex python sample.py html (or plain)")
        sys.exit()

    elif sys.argv[1]=="plain":
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.getResult()
        print(result)

    elif sys.argv[1]=="html":
        html_builder = HtmlBuilder()
        director = Director(html_builder)
        director.construct()
        filename = html_builder.getResult()
        print("{} created.".format(filename))
