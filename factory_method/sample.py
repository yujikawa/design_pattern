from idcard import IDCardFactory


if __name__ == "__main__":
    factory = IDCardFactory()
    card1 = factory.create("Yujikawa")
    card2 = factory.create("Tanaka")
    card1.use()
    card2.use()
    print(factory.owners)