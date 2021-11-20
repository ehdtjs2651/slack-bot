"""
DB 와 연결하는 부분
"""
import warnings
from logging import getLogger

import pandas as pd
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.util.compat import contextmanager

logger = getLogger(__name__)


class BaseDBAdapter(object):
    name = "BaseDBAdapter"
    db_name = None
    engine_info = None
    is_echo_init = True
    is_echo_sql = False

    def __init__(self, direct: dict):
        """
        # DB 연결 생성
        """
        # DB 연결정보
        self.get_settings(direct)
        # DB 연결 engine 생성
        self.engine = self.create_db_engine()
        # DB 세션 생성
        self.session_maker = sessionmaker(bind=self.engine)

    def get_settings(self, direct: dict):
        # settings 파일에서 가져오기
        if not direct:
            try:
                from settings import IS_SQL_ECHO, DATABASES, DB_NickName, ECHO_DB_SETTING
                # db 이름이 비어있을 시
                if self.db_name is None:
                    self.db_name = DB_NickName
                else:
                    warnings.warn(f"초기화전 DB 이름을 직접 입력하여 사용하셨습니다.")

                # DB 이름이 비어있을 시 - DB_NickName이 None인경우
                if self.db_name is None:
                    warnings.warn(f"DB를 설정파일에서 찾을 수 없습니다.\n"
                                  f"DB 이름을 local로 변경합니다.")
                    self.db_name = 'local'
                try:
                    self.engine_info = DATABASES[self.db_name]
                except KeyError as ke:
                    warnings.warn(f"해당 DB 이름을 settings의 DATABASES에서 찾을 수 없습니다.")
                    raise ke

                self.is_echo_sql = IS_SQL_ECHO
                self.is_echo_init = ECHO_DB_SETTING

            except ModuleNotFoundError as e:
                warnings.warn(f"설정파일을 import 할 수 없습니다.\n"
                              f"direct로 직접 입력해 주세요")
                raise e

        # 직접 세팅
        else:
            self.engine_info = {
                "database": direct['database'],
                "user": direct['user'],
                "password": direct['password'],
                "host": direct['host'],
                "port": direct['port'],
            }

    def create_db_engine(self):
        """
        :param on_test:
        :return: engine
        """
        db_link = f'postgresql://{self.engine_info["user"]}:{self.engine_info["password"]}' \
                  f'@{self.engine_info["host"]}:{self.engine_info["port"]}/{self.engine_info["database"]}'

        # engine 생성
        engine = create_engine(db_link, echo=self.is_echo_sql)
        # echo
        if self.is_echo_init:
            print(f"{self.name} engine create: {self.engine_info}")
        return engine


class DBAdapter(BaseDBAdapter):
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self, name, direct=None, db_name=None):
        # 테스트 모드시 설정
        self.db_name = db_name
        self.name = name
        super().__init__(direct=direct)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session_maker()
        try:
            yield session
            session.commit()
            session.expunge_all()

        except:
            session.rollback()
            raise
        finally:
            session.close()

    def execute_sql(self, sql: str):
        """
        sql문 단순 실행
        :param sql:
        :return:
        """
        session = self.session_maker()
        try:
            session.execute(sql)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def fetch_data_by_sql(self, sql: str):
        """
        sql문 단순 실행
        :param sql:
        :return:
        """
        session = self.session_maker()
        try:
            result_proxy = session.execute(sql)
            return result_proxy.fetchall()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def fetch_df_by_sql(self, sql: str):
        """
        sql문 단순 실행
        :param sql:
        :return:
        """
        session = self.session_maker()
        try:
            data = pd.read_sql(sql, session.bind)
            return data
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def insert_df(self, table_name: str, data: pd.DataFrame, **kwargs):
        data.to_sql(
            table_name,
            self.engine,
            index=False,
            if_exists='append',
            **kwargs
        )

    def select_filter_one(self, model, **filter_list):
        result = session.query(model).filter_by(**filter_list).first()
        return result
