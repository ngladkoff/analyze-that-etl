from json.decoder import JSONDecodeError
import firebase_admin
from firebase_admin import credentials, firestore
import json


def create_data_obj():
    data = {}
    data['users'] = []
    return data


def get_db():
    cred= credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def import_scrum_game_data():
    data = create_data_obj()
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


def import_psycho_game_data():
    data = create_data_obj()
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

    with open("psycho.json", "w") as file:
        json.dump(data, file)    

    print("Proceso finalizado")




def main():
    option = 1
    while option != 0:
        option = int(input("Ingrese opción: [1-Scrum | 2-Psycho]"))
        if option == 1:
            import_scrum_game_data()
        if option == 2:
            import_psycho_game_data()
    print("Adios")


if __name__ == '__main__':
    main()