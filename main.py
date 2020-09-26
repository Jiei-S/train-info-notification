"""実行モジュール
"""
import sys
from module.collect import Collector, NotFoundElementError
from module.line import Line


def run():
    """ 実行関数 """
    try:
        line = Line()
    except KeyError:
        sys.exit()

    try:
        collector = Collector()
        train_info = collector.get_train_info()
    except (ValueError, NotFoundElementError) as err:
        line.send_error(err)
    else:
        line.send_success(train_info)


if __name__ == '__main__':
    run()
