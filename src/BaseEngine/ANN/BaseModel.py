import logging
import pandas as pd

logger = logging.getLogger(__name__)


class PredictBaseModel:
    model = None

    def __init__(self):
        self.model_name = "PredictBaseModel"
        self.model_name = self.__class__.__name__

    def train(self, x_dataset, y_dataset):
        """
        예측 모델 학습
        :param x_dataset:
        :param y_dataset:
        :return:
        """
        # 훈련
        if self.model is not None:
            self.model.fit(x_dataset, y_dataset)
            logger.debug("model train")

        # 모델 없음
        else:
            logger.error(f"model 이 없어 학습을 수행 할 수 없습니다..")

    # logger.debug(self.model.coef_)

    def predict(self, input_data: pd.DataFrame):
        """
        :param input_data: 예측시 입력하는 데이터
        :return: 예측된 결과물
        """
        # 예측 수행
        if self.model is not None:
            y_predict = self.model.predict(input_data)
            logger.debug("predict")
            return y_predict

        # 모델 없음
        else:
            logger.error(f"model 이 없어 학습을 수행 할 수 없습니다..")
        # 데이터 출력

    def save_model(self):
        """
        학습된 모델 저장
        :return:
        """
        pass

    def load_model(self):
        """
        저장된 모델 불러오기
        :return:
        """
        pass

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
