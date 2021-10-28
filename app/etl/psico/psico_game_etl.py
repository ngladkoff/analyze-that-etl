
from etl.data_loader import DataLoader
from etl.data_transformer import DataTransformer
from etl.data_extractor import DataExtractor
from etl.game_etl import GameEtl


class PsicoGameEtl(GameEtl):

    def __init__(self, extractor: DataExtractor,
                 transformer: DataTransformer,
                 loader: DataLoader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def start(self):
        data = self.extractor.extract()
        data = self.transformer.transform(data)
        self.loader.load(data)
        print("Proceso finalizado")
