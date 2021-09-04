from abc import ABC, abstractmethod
from typing import Dict


class DataLoader(ABC):

    @abstractmethod
    def load(self, data: Dict):
        pass
