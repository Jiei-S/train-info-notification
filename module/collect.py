"""運行情報収集モジュール
"""
from concurrent.futures import ThreadPoolExecutor
import requests

from bs4 import BeautifulSoup


class NotFoundElementError(Exception):
    """ 要素が存在しない時のエラー """
    pass


class Collector:
    """ 収集クラス """
    def __init__(self):
        try:
            with open('train_urls.txt', 'r') as file:
                self.urls = file.read().splitlines()
        except FileNotFoundError as err:
            raise NotFoundElementError('url get failed!') from err

    def format_train_info(self, info, err_trains):
        """運行情報整形

        @param:
          info [ <str: 路線>, <str: 詳細> ]
          err_trains [ <str: 運行情報失敗URL> ]
        @return:
          train_info <str: 運行情報>
        """
        train_info = '\n'
        for i in info:
            try:
                lead, _, detail = i[1].strip('\n').split('\n')
                train_info += '{0}\n{1}\n{2}\n\n'.format(i[0], lead, detail)
            except ValueError as err:
                raise ValueError('format failed!') from err

        if not err_trains:
            train_info += 'Collect Complete!'
            return train_info

        train_info += 'This is Error url!'
        for url in err_trains:
            train_info += '\n' + url
        return train_info

    def get_train_info(self):
        """運行情報収集

        @return:
          format_train_info(train_info, err_trains) <str: 運行情報>
        """
        pool = ThreadPoolExecutor()
        res_list = pool.map(requests.get, self.urls)

        train_info, err_trains = [[], []]
        for res in res_list:
            try:
                res.raise_for_status()
            except requests.exceptions.RequestException:
                err_trains.append(res.url)
                continue

            bs_obj = BeautifulSoup(res.text, 'lxml')
            try:
                route = bs_obj.h1.text
                detail = bs_obj.find(id='mdServiceStatus').text
            except AttributeError:
                err_trains.append(res.url)
            else:
                train_info.append([route, detail])

        if not train_info:
            raise NotFoundElementError('collect failed!')
        return self.format_train_info(train_info, err_trains)
