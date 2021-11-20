import json
import logging.config

from src.Controller.logger.logger_config import logger_config, test_logger_config


class log_settings:
    log_config = None

    def initialize(self):
        logging.config.dictConfig(self.log_config)


class py_log_settings(log_settings):

    @classmethod
    def init(cls):
        cls.log_config = logger_config
        cls.initialize(cls)

    @classmethod
    def test_init(cls):
        cls.log_config = test_logger_config
        cls.initialize(cls)

    # def change_config(self, key, *args):
    #     select = self.log_config
    #     for arg in args:
    #         select = select.get(arg)
    #
    #     pass


def open_log_setting_json():
    """
    json 파일 형식으로 된 logger 설정파일을 읽어와 로거를 설정한다.
    :return:
    """
    with open('loggers.json') as f:
        config_json = json.load(f)
        print("로그 설정")
        # print(config)
        logging.config.dictConfig(config_json)
