from abc import ABC, abstractmethod
from typing import Dict


class DataTransformer(ABC):

    @abstractmethod
    def transform(self, data: Dict) -> Dict:
        pass
