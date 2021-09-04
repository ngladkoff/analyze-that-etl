from typing import Dict
from etl.data_transformer import DataTransformer


class ScrumXApiTransformer(DataTransformer):

    def transform(self, data: Dict) -> Dict:
        print("ScrumXApiTransformer.transform")
        xAPI = self.create_xApi_dict()
        for user in data['users']:
            xAPI['xps'].append(self.create_user_xp(user))
        return xAPI

    def create_xApi_dict(self):
        return {
            'xps': []
            }

    def create_user_xp(self, user):
        return {
            'actor': {
                'name': user['name'],
                'id': user['uid']
            },
            'verb': {
                'id': 'http://adlnet.gov/expapi/verbs/registered',
                'display': {
                    'en-US': 'Registered',
                    'es-AR': 'Registrado'
                }
            },
            'object': {
                'objectType': 'player',
                'name': user['name'],
                'id': user['uid'],
                'mail': user['mail'],
                'gender': user['gender'],
                'age': user['age'],
                'profession': user['profession'],
                'country': user['country'],
                'state': user['state'],
                'city': user['city'],
                'gameTimeLevel': user['gameTimeLevel'],
                'gameTasteLevel': user['gameTasteLevel']
            }
        }
