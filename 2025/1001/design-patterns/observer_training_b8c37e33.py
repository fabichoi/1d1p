# observer pattern









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
