# observer pattern

class Observer:
    def update(self, message):
        raise NotImplementedError("need to implement")


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
        self.messages = []

    def update(self, message):
        self.messages.append(message)


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


subject = Subject()
observer1 = ConcreteObserver("Observer1")
observer2 = ConcreteObserver("Observer2")

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Update 1")

assert observer1.messages == ["Update 1"]
assert observer2.messages == ["Update 1"]

subject.notify_observers("Update 2")

assert observer1.messages == ["Update 1", "Update 2"]
assert observer2.messages == ["Update 1", "Update 2"]