from typing import Dict
from etl.data_loader import DataLoader
import json


class ScrumFileLoader(DataLoader):

    def load(self, data: Dict):
        print("ScrumFileLoader.load")
        with open("scrum.json", "w") as file:
            json.dump(data, file)
