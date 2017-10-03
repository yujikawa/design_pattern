from singleton import Singleton


if __name__ == "__main__":
    obj1 = Singleton("dog")
    obj2 = Singleton("cat")
    if obj1 == obj2:
        print("obj1 and obj2 are the same instance.")
        print("obj1.name={} obj2.name={}".format(obj1.name, obj2.name))