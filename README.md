# train-info-notification
電車の運行情報をLINE通知するアプリケーションです。

## Install
#### [LINE Notify](https://notify-bot.line.me/ja/)にてアクセストークン発行
#### git clone
~~~
$ git clone https://github.com/Jiei-S/train-info-notification.git
~~~
#### 環境構築
- ライブラリ インストール  
- 環境変数 設定
<dl>
  <dt>LINE_API_URL</dt>
  <dd>LINE Notifyのエンドポイント</dd>
  <dt>LINE_API_TOKEN</dt>
  <dd>アクセストークン</dd>
  <dt>TRAIN_URLS</dt>
  <dd>Yahoo!路線情報の路線URL<br>（例）https://transit.yahoo.co.jp/traininfo/detail/21/0/<br>複数設定の場合、半スペ区切り<br>（例）https://transit.yahoo.co.jp/traininfo/detail/21/0/ https://transit.yahoo.co.jp/traininfo/detail/22/0/</dd>
</dl>

~~~
$ cd train-info-notification/
$ . install.sh
~~~


## Usage
#### run
~~~
$ python main.py
~~~
