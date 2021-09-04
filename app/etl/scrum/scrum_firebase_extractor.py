from typing import Dict
from etl.data_extractor import DataExtractor
from firebase.firebase_db import get_db


class ScrumFirebaseExtractor(DataExtractor):

    def create_data_obj(self):
        data = {}
        data['users'] = []
        return data

    def extract(self) -> Dict:
        print("ScrumFirebaseExtractor.extract")
        data = self.create_data_obj()
        db = get_db()
        collection = db.collection('users')

        all_users = collection.stream()
        for user in all_users:
            print(user.id)
            user_dict = user.to_dict()
            user_collections = user.reference.collections()
            for user_collection in user_collections:
                if user_collection.id == 'levels':
                    user_dict['levels'] = []
                    for level in user_collection.stream():
                        level_dict = level.to_dict()
                        user_dict['levels'].append(level_dict)
            data['users'].append(user_dict)
        return data
