from abc import ABC, abstractmethod
from typing import Dict


class DataExtractor(ABC):

    @abstractmethod
    def extract(self) -> Dict:
        pass
