# Mourse-API-flask

Flaskで作成したマールスAPIです．
配布して各自がAPIを実装することを想定しているため，最低限の機能しか実装していません．

例えば応答生成機能などを追加したい場合は，APIを自作してください．

dockerコンテナ立ち上げと同時にFlaskサーバが起動するようにしてあるので，コンテナ内に入ってのサーバ起動などは不要です．

また，Elasticsearchも合わせてインストールするため，ルールベース対話などへの拡張が可能です．

もしElasticsearchをインストールしたくない場合は，`docker-compose.yml`の4行目〜19行目，つまり`build: ./elasticsearch`の下位インデント全てを削除してください．

## 使い方

```bash
docker-compose up --build
```

docker-composeの放置されている問題として，proxy下にあるwindows PCで上記コマンドをしてもネットワークエラーになることがあります．

その場合は初回build時のみ下記コマンドを利用してください．

```bash
docker pull python:3.8
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.16.2
docker-compose up --build
```

## 最低限の機能
* ルートのエンドポイントにアクセスするとメッセージが表示される
* エコーAPI

## エコーAPIへのRequestの送り方
以下はcurlで適当な文章をPOSTする例です．

```
curl -X 'POST' \
        'http://127.0.0.1:8000/echo' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
    "data": "ここに入力"
  }'
```

