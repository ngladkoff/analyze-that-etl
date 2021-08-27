from etl.game_etl import GameEtl
from etl.scrum_game_etl import ScrumGameEtl
from etl.psico_game_etl import PsicoGameEtl

class EtlFactory():

    @staticmethod
    def create_etl(etl_type: str) -> GameEtl:
        if etl_type == 'scrum':
            return ScrumGameEtl()
        elif etl_type == 'psico':
            return PsicoGameEtl()
        else:
            raise ValueError(etl_type)