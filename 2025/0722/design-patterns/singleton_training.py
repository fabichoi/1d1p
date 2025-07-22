# singleton pattern
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = ''

        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

assert singleton1 is singleton2
assert singleton1.value == singleton2.value

singleton1.value = "changed"
assert singleton2.value == "changed"
