# Mourse-API-flask

Flaskで作成したマールスAPIです．
配布して各自がAPIを実装することを想定しているため，最低限の機能しか実装していません．
例えば応答生成機能などを追加したい場合は，APIを自作してください．

また，dockerコンテナ立ち上げと同時にFlaskサーバが起動するようにしてあるので，コンテナ内に入ってのサーバ起動などは不要です．

## 使い方

```
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