from abc import ABC, abstractmethod

class GameEtl(ABC):
    @abstractmethod
    def start(self):
        pass