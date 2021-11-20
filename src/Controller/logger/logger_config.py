from src.Controller.logger.logger_env import setting_logger_env

logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s:%(name)s:%(lineno)s (%(levelname)s) %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "complex": {
            "format": "[%(asctime)s] %(levelname)s [%(module)s %(name)s :%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": setting_logger_env("CONSOLE_HANDLER_LEVEL", default="INFO"),
            "stream": "ext://sys.stdout",
        },
        "errors_file": {
            "class": "logging.FileHandler",
            "filename": "logs/error.log",
            "formatter": "complex",
            "level": "WARNING",
        },
        "all_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "complex",
            "filename": "logs/all/all.log",
            "when": "midnight",
            "backupCount": 30,
            "interval": 1,
            "encoding": "utf-8"
        },
        "test_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "complex",
            "filename": "logs/test_log/test.log",
            "when": "midnight",
            "backupCount": 30,
            "interval": 1,
            "encoding": "utf-8"
        },
        "info_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "complex",
            "filename": "logs/server_info/info.log",
            "when": "midnight",
            "backupCount": 30,
            "interval": 1,
            "encoding": "utf-8"
        },
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ["console"],
        },
        "__main__": {
            "level": "DEBUG",
            "handlers": ["console", "errors_file", "info_file", "all_file"],
            "propagate": False,
        },
        "Predict": {
            "level": "DEBUG",
            "handlers": ["console", "errors_file", "info_file", "all_file"],
            "propagate": False,
        },
        "Collect": {
            "level": "DEBUG",
            "handlers": ["console", "errors_file", "info_file", "all_file"],
            "propagate": False,
        },
        "src": {
            "level": "DEBUG",
            "handlers": ["console", "errors_file", "info_file", "all_file"],
            "propagate": False,
        },
        "src.Controller.Schedule": {
            "level": setting_logger_env("SCHEDULE_LOGGER_LEVEL", default="INFO"),
            "handlers": ["console", "errors_file", "info_file", "all_file"],
            "propagate": False,
        },
        "test": {
            "level": "DEBUG",
            "handlers": ["console", "errors_file", "test_file"],
            "propagate": False,
        },
        "apscheduler": {
            "level": setting_logger_env("SCHEDULE_LOGGER_LEVEL", default="INFO"),
            "handlers": ["console", "errors_file", "info_file", "all_file"],
            "propagate": False,
        },
    },
}

# docker 없이 test 코드 실행때 로그 설정
test_logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s:%(name)s:%(lineno)s (%(levelname)s) %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "complex": {
            "format": "[%(asctime)s] %(levelname)s [%(module)s %(name)s :%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
        "src.Controller.Schedule": {
            "level": setting_logger_env("SCHEDULE_LOGGER_LEVEL", default="INFO"),
            "handlers": ["console"],
            "propagate": False,
        },
        "apscheduler": {
            "level": setting_logger_env("SCHEDULE_LOGGER_LEVEL", default="INFO"),
            "handlers": ["console"],
            "propagate": False,
        },
        "urllib3": {
            "level": setting_logger_env("CONSOLE_HANDLER_LEVEL", default="INFO"),
            "handlers": ["console"],
            "propagate": False,
        },
    },
}