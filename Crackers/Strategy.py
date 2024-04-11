from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, encrypted_message, n, e):
        pass
