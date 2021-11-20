DEV_SETTINGS = {
    # 테스트 실행
    "IS_RUN_TEST": False,
    # 테스트 코드 전체 실행, false시 일부 지정된 테스트 코드만 실행
    "IS_TEST_ALL": True,

    # main 함수 계속 동작 여부

    "IS_MAIN_RUNNING": True,
    "MAIN_INTERVAL": 10,
    # 스케줄러 실행 여부
    "IS_RUN_SCHEDULER": True,   # by DH 2021-10-17

    # SQL문 출력
    "IS_SQL_ECHO": False,
    # DB 연결 설정 출력
    "ECHO_DB_SETTING": True,

}

LOGGER_SETTINGS = {
    # 로그 출력 수준 설정: DEBUG - 모든 로그 출력, INFO - 알림 로그만 출력
    "CONSOLE_HANDLER_LEVEL": "DEBUG",
    # 스케줄러 로그 출력 수준 설정
    "SCHEDULE_LOGGER_LEVEL": "DEBUG",
}
