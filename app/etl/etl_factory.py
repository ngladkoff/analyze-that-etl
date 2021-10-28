from etl.psico.psico_xapi_transformer import PsicoXApiTransformer
from etl.scrum.scrum_xapi_transformer import ScrumXApiTransformer
from etl.scrum.scrum_file_loader import ScrumFileLoader
from etl.psico.psico_file_loader import PsicoFileLoader
from etl.scrum.scrum_json_transformer import ScrumJsonTransformer
from etl.psico.psico_json_transformer import PsicoJsonTransformer
from etl.scrum.scrum_firebase_extractor import ScrumFirebaseExtractor
from etl.psico.psico_firebase_extractor import PsicoFirebaseExtractor
from etl.scrum.scrum_api_loader import ScrumApiLoader
from etl.psico.psico_api_loader import PsicoApiLoader
from etl.game_etl import GameEtl
from etl.scrum.scrum_game_etl import ScrumGameEtl
from etl.psico.psico_game_etl import PsicoGameEtl


class EtlFactory():

    @staticmethod
    def create_etl(etl_type: str, isXApi: bool, isFileLoader: bool) -> GameEtl:
        if etl_type == 'scrum':
            return ScrumGameEtl(ScrumFirebaseExtractor(),
                                ScrumXApiTransformer() if isXApi
                                else ScrumJsonTransformer(),
                                ScrumFileLoader() if isFileLoader
                                else ScrumApiLoader())
        elif etl_type == 'psico':
            return PsicoGameEtl(PsicoFirebaseExtractor(),
                                PsicoXApiTransformer() if isXApi
                                else PsicoJsonTransformer(),
                                PsicoFileLoader() if isFileLoader
                                else PsicoApiLoader())
        else:
            raise ValueError(etl_type)
