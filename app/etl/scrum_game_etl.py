from etl.game_etl import GameEtl
import json
from firebase.firebase_db import get_db

class ScrumGameEtl(GameEtl):

    def create_data_obj(self):
        data = {}
        data['users'] = []
        return data

    def start(self):
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

        print("Guardando archivo")

        with open("scrum.json", "w") as file:
            json.dump(data, file)

        print("Proceso finalizado")


