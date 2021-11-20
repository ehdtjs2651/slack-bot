import logging

from src.BaseEngine.base_machine import BaseMachine
from src.Controller.Schedule.schedule_manager import MainScheduler
from src.DB.DB_Adapter import DBAdapter

logger = logging.getLogger(__name__)


class PredictBaseMachine(BaseMachine):
    scheduler = MainScheduler(name=f"PredictBaseMachine")
    predict_time = {}
    train_time = {}

    def __init__(self):
        self.name = "PredictBaseMachine"

    def train_run(self):
        """
        학습 시작
        :return:
        """
        logger.debug(f"{self.name} train_run - {self.train_time}")
        pass

    def predict_run(self):
        """
        예측 시작
        :return:
        """
        logger.debug(f"{self.name} predict_run - {self.predict_time}")

        pass

    def train_test(self):
        """
        학습 테스트
        :return:
        """
        logger.debug(f"{self.name} train_test - {self.train_time}")

        pass

    def predict_test(self):
        """
        예측 테스트
        :return:
        """
        logger.debug(f"{self.name} predict_test - {self.predict_time}")

        pass

