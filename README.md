# Mourse-Kit

マールスを動かすためのスターターキットです．

手順に従ってUnityとFlask APIリポジトリ，VOICEVOXをダウンロードしてください．

配布して各自がAPIを実装することを想定しているため，最低限の機能しか実装していません．

# 導入手順
## 1. Unityの導入

以下にアクセスしてUnity Hubをダウンロードして，インストールしてください．

https://unity.com/ja/download

以下の手順に従ってプロジェクトを作成してください．

https://tech.pjin.jp/blog/2020/08/31/unity-project-create

プロジェクトの種類は３Dを選択してください．

## 2. Unity Packageのダウンロード
以下のGoogle DriveからUnity Package（Unityのデータを配布するためのもの）をダウンロードしてください．

URL

## 3. Unity Packageのインポート
以下の記事を見て，Unity PackageをUnityにインポートしてください．（ドラッグ＆ドロップするだけです）

https://tech.pjin.jp/blog/2021/02/28/unity_unitypackage_import_export/

インポートしたら，Asset>ScenesにあるMainというファイルをダブルクリックしてください．

GameタブをクリックするとマールスのUIが表示されるはずです．

また，この際アスペクト比が適切でないことがあるので，Gameタブの下にプルダウンメニューを参照し，Free Aspectから16:9に変更してください．

この操作でUnity側の準備は終わりです．

## 4. Flask APIの導入
以下の手順でGit CloneしてPythonファイルを実行することで，APIサーバが立ち上がります．

```bash
git clone https://github.com/uec-mourse/Mourse-API-flask.git
cd Mourse-API-flask
pip install -r requirements.txt
python3 app.py
```

## 5. VOICEVOXの導入
以下から音声合成ソフトVOICEVOXをダウンロードしてください．

https://voicevox.hiroshiba.jp/

以下のURLに導入方法が載っています．

https://voicevox.hiroshiba.jp/how_to_use/

また，設定からCPUを使うかGPUを使うかを選択することが出来ます．

VOICEVOXを起動すると勝手に音声合成のためのサーバが立ち上がります．

Flaskサーバ，VOICEVOX，Unityが起動している状態で，Unityの`Gameタブ`にある`再生ボタン▶`を押すとマールスが起動します．
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

