from abc import ABC, abstractmethod
from etl.data_loader import DataLoader
from etl.data_transformer import DataTransformer
from etl.data_extractor import DataExtractor


class GameEtl(ABC):

    @abstractmethod
    def __init__(self, extractor: DataExtractor,
                 transformer: DataTransformer,
                 loader: DataLoader):
        pass

    @abstractmethod
    def start(self):
        pass
