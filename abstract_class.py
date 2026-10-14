from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("bark")
dog1=dog()
dog1.sound()