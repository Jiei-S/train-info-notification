"""
環境構築
"""
import getpass
import os
import subprocess
import sys


COMMANDS = [
    'pip install beautifulsoup4',
    'pip install requests',
    'pip install lxml',
]


# pylint: disable=W0613
def check_null(func):
    """標準入力の空判定"""
    def wrapper(*args, **kwargs):
        input_val = func(args)
        while input_val == '':
            return wrapper(*args, **kwargs)
        os.environ[args[0]] = input_val
    return wrapper


@check_null
def set_line_api_url(env):
    """LINE API URL設定"""
    return input('LINE_API_URL: ')


@check_null
def set_line_api_token(env):
    """LINE API トークン設定"""
    return getpass.getpass('LINE_API_TOKEN: ')


@check_null
def set_train_info_url(env):
    """収集する運行情報のURL設定"""
    return input('Please input traininfo url: ')


# pylint: disable=W0703
def run():
    """環境構築"""
    print("""### Library Install ###""")
    try:
        [subprocess.call(cmd, shell=True) for cmd in COMMANDS]
    except Exception as err:
        print(err)
        sys.exit()

    print("""### LINE Notify ###""")
    try:
        set_line_api_url('LINE_URL')
        set_line_api_token('LINE_TOKEN')
    except Exception as err:
        print(err)
        sys.exit()

    print("""### Target Train ###""")
    try:
        set_train_info_url('TRAIN_URLS')
    except Exception as err:
        print(err)
        sys.exit()


if __name__ == '__main__':
    print("====================\nSetting Start!\n====================")
    run()
    print("====================\nSetting Finish!\n====================")
