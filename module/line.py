"""
LINE通知モジュール
"""
import os
import requests


class Line:
    """LINE通知クラス"""
    def __init__(self):
        """環境変数取得"""
        try:
            self.url = os.environ['LINE_API_URL']
            self.token = os.environ['LINE_API_TOKEN']
            self.headers = {'Authorization': 'Bearer ' + self.token}
        except KeyError as err:
            raise KeyError(err)

    def send_success(self, info):
        """収集成功

        @param:
          info <str: 運行情報>
        """
        requests.post(self.url,
                      headers=self.headers,
                      params={'message': info})

    def send_error(self, err_msg):
        """収集失敗

        @param:
          err_msg <str: エラーメッセージ>
        """
        requests.post(self.url,
                      headers=self.headers,
                      params={'message': err_msg})
