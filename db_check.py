from datetime import date, datetime, timedelta
from logging import getLogger
from src.DB.DB_Adapter import DBAdapter

logger = getLogger(__name__)
# 데이터를 가져올 서버의 정보
database = {
    "database": 'ppc',
    "user": 'user',
    "password": '1234',
    "host": "3.38.129.72",
    "port": 12100,
}
db = DBAdapter(name="database", direct=database)


print("hello")


def search_table_start_str(start_str: str):
    result_table_list = []
    select_sql = f"SELECT relname as table_name " \
                 f"FROM pg_stat_user_tables"

    # 테이블 목록 수집
    table_name_list = db.fetch_data_by_sql(select_sql)

    # 테이블명 조회
    for db_table in table_name_list:
        table_name = db_table[0]  # 테이블 이름만 가져옴
        # app_collect 으로 시작하는 table name
        if table_name.startswith(start_str):
            result_table_list.append(table_name)

    return result_table_list


def counter(db, table_name, column_name, day):
    select_sql = f"SELECT COUNT(*) FROM {table_name} "\
                 f"WHERE {column_name} BETWEEN DATE '{day}' " \
                 f"AND DATE '{day}' + interval '1 day';"
    today_data = db.fetch_data_by_sql(select_sql)
    data_collect = today_data[0][0]
    return data_collect


def db_ls():
    time = datetime.strptime(date.today(), '%Y-%m-%d')
    column = 'issue'
    table_name_starts_with = 'app_collect'
    tables = search_table_start_str(table_name_starts_with)
    del tables[tables.index('app_collect_generation')]
    del tables[tables.index('app_collect_apiirradiation')]
    text = ""
    for table in tables:
        text += f"today's data collected : {counter(db, table, column, time)} at {table}"
    text += f"today's data collected : {counter(db, 'app_collect_generation', 'target', time)} at app_collect_generation"
    text += f"today's data collected : {counter(db, 'app_collect_apiirradiation', 'target', time)} at app_collect_apiirradiation"
    for table in tables:
        text += f"day 1 before data collected : {counter(db, table, column, time-timedelta(days = 1))} at {table}"
    text += f"day 1 before data collected : {counter(db, 'app_collect_generation', 'target', time-timedelta(days = 1))} at app_collect_generation"
    text += f"day 1 before data collected : {counter(db, 'app_collect_apiirradiation', 'target', time-timedelta(days = 1))} at app_collect_apiirradiation"
    for table in tables:
        text += f"day 2 before data collected : {counter(db, table, column, time-timedelta(days = 2))} at {table}"
    text += f"day 2 before data collected : {counter(db, 'app_collect_generation', 'target', time-timedelta(days = 2))} at app_collect_generation"
    text += f"day 2 before data collected : {counter(db, 'app_collect_apiirradiation', 'target', time-timedelta(days = 2))} at app_collect_apiirradiation"
    for table in tables:
        text += f"day 3 before data collected : {counter(db, table, column, time-timedelta(days = 3))} at {table}"
    text += f"day 3 before data collected : {counter(db, 'app_collect_generation', 'target', time-timedelta(days = 3))} at app_collect_generation"
    text += f"day 3 before data collected : {counter(db, 'app_collect_apiirradiation', 'target', time-timedelta(days = 3))} at app_collect_apiirradiation"
    for table in tables:
        text += f"day 4 before data collected : {counter(db, table, column, time-timedelta(days = 4))} at {table}"
    text += f"day 4 before data collected : {counter(db, 'app_collect_generation', 'target', time-timedelta(days = 4))} at app_collect_generation"
    text += f"day 4 before data collected : {counter(db, 'app_collect_apiirradiation', 'target', time-timedelta(days = 4))} at app_collect_apiirradiation"
    return text

