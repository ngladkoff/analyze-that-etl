from typing import Dict
from etl.data_transformer import DataTransformer


class PsicoJsonTransformer(DataTransformer):

    def transform(self, data: Dict) -> Dict:
        print("PsicoJsonTransformer.transform")
        return data
