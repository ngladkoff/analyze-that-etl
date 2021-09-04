from etl.scrum.scrum_xapi_transformer import ScrumXApiTransformer
from etl.scrum.scrum_file_loader import ScrumFileLoader
from etl.scrum.scrum_json_transformer import ScrumJsonTransformer
from etl.scrum.scrum_firebase_extractor import ScrumFirebaseExtractor
from etl.game_etl import GameEtl
from etl.scrum.scrum_game_etl import ScrumGameEtl
from etl.psico.psico_game_etl import PsicoGameEtl


class EtlFactory():

    @staticmethod
    def create_etl(etl_type: str, isXApi: bool) -> GameEtl:
        if etl_type == 'scrum':
            return ScrumGameEtl(ScrumFirebaseExtractor(),
                                ScrumXApiTransformer() if isXApi
                                else ScrumJsonTransformer(),
                                ScrumFileLoader())
        elif etl_type == 'psico':
            return PsicoGameEtl()
        else:
            raise ValueError(etl_type)
