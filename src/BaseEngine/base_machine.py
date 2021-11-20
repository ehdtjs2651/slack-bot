from src.DB.DB_Adapter import DBAdapter


class BaseMachine:
    db = DBAdapter(name="BaseMachine")

    def init_by_db(self):
        """
        db에 저장된 세팅 불러오기
        :return:
        """
        pass

    def init_reset(self):
        """
        db에 저장된 값 없이 처음부처 시작하기
        :return:
        """