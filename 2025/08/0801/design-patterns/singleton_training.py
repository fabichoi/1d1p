# singleton pattern









singleton1 = Singleton()
singleton2 = Singleton()

assert singleton1 is singleton2
assert singleton1.value == singleton2.value

singleton1.value = "changed"
assert singleton2.value == "changed"
