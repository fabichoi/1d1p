# observer pattern

class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def __init__(self):
        self.messages = []


class ConcreteObserver(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, message):
        self.messages.append(message)


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
