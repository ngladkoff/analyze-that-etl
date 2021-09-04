from typing import Dict
from etl.data_transformer import DataTransformer


class ScrumJsonTransformer(DataTransformer):

    def transform(self, data: Dict) -> Dict:
        print("ScrumJsonTransformer.transform")
        return data
