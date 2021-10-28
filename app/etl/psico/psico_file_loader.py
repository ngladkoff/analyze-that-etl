from typing import Dict
from etl.data_loader import DataLoader
import json


class PsicoFileLoader(DataLoader):

    def load(self, data: Dict):
        print("PsicoFileLoader.load")
        with open("psico.json", "w") as file:
            json.dump(data, file)
