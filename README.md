# 運行情報をLINE通知
<img src="https://user-images.githubusercontent.com/55335212/80302341-69783400-87e4-11ea-929f-2c4bc7230f40.jpeg" width="320px">

## Install
- [LINE Notify](https://notify-bot.line.me/ja/)にてアクセストークン発行
- git clone
~~~
$ git clone https://github.com/Jiei-S/train-info-notification.git
~~~
- 環境構築  
install.shの実行により、ライブラリのインストール、環境変数の設定を行います。
~~~
$ cd train-info-notification/
$ . install.sh
~~~
環境変数
<dl>
  <dt>LINE_API_URL</dt>
  <dd>https://notify-api.line.me/api/notify</dd>
  <dt>LINE_API_TOKEN</dt>
  <dd>アクセストークン</dd>
</dl>

路線URL  
train_urls.txt　に収集したい路線URLを記載する。
（例）
https://transit.yahoo.co.jp/traininfo/detail/21/0/

## Usage
- run
~~~
$ python main.py
~~~

## Requirement
install.shの実行により、インストールされます。  
- beautifulsoup4  
- requests  
- lxml

## License
MIT
