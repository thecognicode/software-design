from abc import ABC, abstractmethod

class Discount(ABC):

    @abstractmethod
    def apply(self, total):
        pass