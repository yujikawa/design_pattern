class _SingletonType(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(_SingletonType, cls).__call__(*args, **kwargs)

        return cls._instance


class Singleton(metaclass=_SingletonType):
    def __init__(self,name):
        self.name = name
        print("Create {} instance.".format(self.name))