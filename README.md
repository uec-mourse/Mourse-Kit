# Mourse-API-flask

Flaskで作成したマールスAPIです．
配布して各自がAPIを実装することを想定しているため，最低限の機能しか実装していません．

## 使い方

```bash
git clone https://github.com/uec-mourse/Mourse-API-flask.git
cd Mourse-API-flask
pip install -r requirements.txt
python3 app.py
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

