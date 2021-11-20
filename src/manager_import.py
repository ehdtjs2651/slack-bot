"""
아래 함수들은 main에서 한번씩 실행하는 함수 입니다.
스케줄러 이외에 한번씩 실행하고 싶으실때 아래에 코드를 추가하시면 될 것 같습니다.
- import는 아래와 같이 해당 함수 내에서 작성하시면 좋을 것 같습니다.
- 객체 생성도 아래 함수내에서 선언하시면 됩니다.
"""
# 하이라이트 라도 제거 금지
# 해당 폴더 자체를 import
from logging import getLogger
logger = getLogger(__name__)


def collect(is_server):
    """
    :param is_server: 서버 실행 유무
    :return:
    """
    # 모듈 import - 자체 제작한 모듈들은 반드시 아래에 import
    from Collect.API_Short.api_short import API_Short
    from Collect.API_LDAPS.ldaps_machine import API_LDAPS
    from Collect.CRAWL_generation.generation import CRAWL_Generation_Machine

    # Must import object !!!
    api_short_machine = API_Short()
    api_ldaps_machine = API_LDAPS()
    crawl_generation_machine = CRAWL_Generation_Machine()

    ##############################################################
    logger.info(f"run collect : is_server=={is_server}")



    # Run only one time!
    if is_server:
        # Docker Server
        # Just put my toy program
        crawl_generation_machine.collect_run()

        pass
    else:
        # Docker Local
        crawl_generation_machine.collect_run()

        # open_adr_machine.collect_run()
        # api_short_machine.collect_run()
        # api_ldaps_machine.collect_run()
        # generation_collector_in_server()
        # api_short_machine.collect_run()
        # api_ldaps_machine.collect_run()

        pass
    ##############################################################


def predict(is_server):
    """
    :param is_server: 서버 실행 유무
    :return:
    """
    # 모듈 import - 자체 제작한 모듈들은 반드시 아래에 import
    # from Predict.Sample.sample_machine import SampleMachine

    # 임시 객체 생성
    # sample_machine = SampleMachine()

    ##############################################################
    logger.info(f"run predict : is_server=={is_server}")

    if is_server:
        # just_test()
        pass
    else:
        # sample_machine.train_run()
        # sample_machine.predict_run()
        pass
    ##############################################################
