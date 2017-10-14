from bridge import Display, CountDisplay, StringDisplayImpl


if __name__ == "__main__":
    d1 = Display(StringDisplayImpl("Hello, Japan."))
    d2 = CountDisplay(StringDisplayImpl("Hello, World."))
    d1.display()
    d2.display()
    d2.multiDisplay(5)
