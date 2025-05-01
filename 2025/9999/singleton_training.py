# singleton pattern

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = "singleton"

        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

assert singleton1 is singleton2
assert singleton1.value == singleton2.value

singleton1.value = "changed"
assert singleton2.value == "changed"
