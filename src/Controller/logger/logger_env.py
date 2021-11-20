from settings_dev import LOGGER_SETTINGS
from src.utils.env.env_import import get_env_none


def check_logger_level(level):
    level_list = ["DEBUG", "INFO", "WARNING", "ERROR"]
    if level in level_list:
        return level
    else:
        raise ValueError


def setting_logger_env(env_name, default):
    if get_env_none('IS_SERVER') == "True":
        return default
    else:
        # 설정파일에서 해당 값 가져오기
        env = LOGGER_SETTINGS[env_name]
        return check_logger_level(env)

