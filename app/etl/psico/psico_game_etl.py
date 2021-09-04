
from etl.data_loader import DataLoader
from etl.data_transformer import DataTransformer
from etl.data_extractor import DataExtractor
from etl.game_etl import GameEtl
from firebase.firebase_db import get_db
import json


class PsicoGameEtl(GameEtl):

    def __init__(self, extractor: DataExtractor,
                 transformer: DataTransformer,
                 loader: DataLoader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def create_data_obj(self):
        data = {}
        data['users'] = []
        return data

    def start(self):
        data = self.create_data_obj()
        db = get_db()
        collection = db.collection('usersPsycho')

        all_users = collection.stream()
        for user in all_users:
            print(user.id)
            user_dict = user.to_dict()
            # user_collections = user.reference.collections()
            # for user_collection in user_collections:
            #     if user_collection.id == 'levels':
            #         user_dict['levels'] = []
            #         for level in user_collection.stream():
            #             level_dict = level.to_dict()
            #             user_dict['levels'].append(level_dict)
            data['users'].append(user_dict)

        print("Guardando archivo")

        with open("psico.json", "w") as file:
            json.dump(data, file)

        print("Proceso finalizado")