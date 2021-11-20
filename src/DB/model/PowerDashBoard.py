from datetime import datetime
from logging import getLogger

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer, DateTime

from src.Controller.Timer.time_utils import time_zone_KST
from src.DB.model_settings import Base

logger = getLogger(__name__)


class power_dashboard(Base):
    __tablename__ = "app_collect_power_dashboard"
    # power info 를 한눈에 보기 위해서 제작

    id = Column(Integer, primary_key=True)
    site_id = Column(String)
    perf_id = Column(Integer)

    # 하루 단위로 작성
    ymdms = Column(DateTime)

    # 데이터 길이
    data_length = Column(Integer)

    created_at = Column(DateTime)

    def __init__(self, site_id: str, perf_id: int,
                 ymdms: datetime, data_length: int):
        try:
            self.site_id = site_id
            self.perf_id = int(perf_id)

            # 한국 시간대로 변환
            self.ymdms = ymdms.replace(tzinfo=time_zone_KST)
            self.data_length = int(data_length)

            self.created_at = datetime.now()
        except ValueError as verr:
            logger.error(f"{verr}: 입력 값이 잘못되었습니다.\n"
                         f"siteID: {siteID}, perfId: {perfId}, ymdms: {ymdms}, "
                         f"data_length: {data_length}")
            raise ValueError(f"power_dashboard init error : {self}")

    def __repr__(self):
        return f"<power_dashboard({self.id}, {self.site_id}, {self.perf_id}, " \
               f"{self.ymdms}, {self.data_length}, " \
               f"{self.created_at})>"

    def __eq__(self, other):
        # 동일 객체인지 확인
        # 시간 요소 배제
        return self.site_id == other.site_id \
               and self.perf_id == other.perf_id \
               and self.ymdms == other.ymdms
