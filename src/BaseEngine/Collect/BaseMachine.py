import logging

from src.BaseEngine.base_machine import BaseMachine
from src.Controller.API.adr_api_client import ADR_API_Client
from src.Controller.Schedule.schedule_manager import MainScheduler
from src.DB.DB_Adapter import DBAdapter

logger = logging.getLogger(__name__)


class CollectBaseMachine(BaseMachine):
    api = ADR_API_Client()
    scheduler = MainScheduler(name="CollectBaseMachine")
    name = "PredictBaseMachine"
    run_time = {}
    test_time = {
        "second": 30
    }

    def __init__(self):
        pass
        
    def test_hello(self):
        logger.debug(f"hello")

