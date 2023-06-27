# Mourse-Kit

マールスを動かすためのスターターキットです．

手順に従ってUnityとFlask APIリポジトリ，VOICEVOXをダウンロードしてください．

配布して各自がAPIを実装することを想定しているため，最低限の機能しか実装していません．

# 各ツールについて（概要や役割など）
## Unity
Unityとはゲーム開発のためのプラットフォームです。

マールスはゲームではありませんが，UIを開発するために使用しています．

役割としてはユーザが見るUI部分を構成し，かつVOICEVOXやFlask APIサーバにリクエストを送る機能を備えています．

## VOICEVOX
無料で使える音声合成ツールです．[公式サイト](https://voicevox.hiroshiba.jp/)

VOICEVOXを起動すると同時にAPIサーバが立ち上がり，このサーバにリクエストを送ることで生成された音声を受け取ることができます．

VOICEVOXのAPIの仕様は[こちら](https://voicevox.github.io/voicevox_engine/api/#tag/%E3%82%AF%E3%82%A8%E3%83%AA%E4%BD%9C%E6%88%90/operation/audio_query_from_preset_audio_query_from_preset_post)をご覧ください．

もしくはVOICEVOXを起動している状態で`http://127.0.0.1:50021/docs`にアクセスしてもドキュメントを閲覧することができます．

役割としてはUnity側から受け取ったテキストデータから音声ファイルを作成し，Unity側に返すことです．

## Flask API
応答を作るためのAPIサーバです，

役割としては，Unityからテキストデータを受け取ってサーバ側で処理を行い，結果をUntiy側に返すことです．

例えばUnityから対話履歴を受け取り，対話履歴を踏まえた応答をサーバ側で生成し，Unity側に返します．

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


# プログラムの改造方法について
## Unity
以下の関数でFlask APIサーバにリクエストを送り，結果をVOICEVOXに送って音声を再生し，さらに画面に表示するところまでを行なっています．

```C#
public async Task<HttpResponseMessage> SetEchoResponse(string user_input){

  var client = new HttpClient();

  // ユーザ発話をJSON型に変換
  var param = new Dictionary<string, object>()
  {
    ["data"]=user_input
  };
  var jsonString = Newtonsoft.Json.JsonConvert.SerializeObject(param);
  var content = new StringContent(jsonString, Encoding.UTF8, @"application/json");

  // Flask APIサーバにリクエストを送る
  var result = await client.PostAsync(@"http://127.0.0.1:8000/echo", content);
  var string_json = await result.Content.ReadAsStringAsync();
  var json_data = JObject.Parse(string_json);

  // 受け取ったデータを格納
  string system_response = json_data["response"].ToString();

  // 音声合成，画面へのテキスト表示を行う
  StartCoroutine(DownlowdFromVOICEVOX(system_response));

  return result;
}
```

以下のコードでFlask APIの受け取りフォーマットに合わせます．
そのため，Flask API側の受け取りフォーマットとC#側の送信フォーマットを改造することで，より多くの情報のやり取りが可能です．
```C#
var param = new Dictionary<string, object>()
{
  ["data"]=user_input
};
```

以下のコードでJSONデータを`http://127.0.0.1:8000/echo`というエンドポイントに送信しています．
Flask API側でエンドポイントを追加したり変更した場合は，このURLを変更することで対応できます．

```C#
var result = await client.PostAsync(@"http://127.0.0.1:8000/echo", content);
```

例えばFlask API側で`/generateResponse`というエンドポイントを作った場合は以下のように変更することで，新しく作ったエンドポイントにリクエストを送信することができます．
```C#
var result = await client.PostAsync(@"http://127.0.0.1:8000/generateResponse", content);
```


## Flask APIについて
Flask APIでは以下のコードによって「送られてきた文字列をそのまま返す」ということを実現しています．
```py
@app.route("/echo", methods=["POST"])
def echo():
    # 送られてきたリクエストのdataキーから要素を取得
    text = request.json["data"]
    return text
```

例えば「送られてきた文字列に`system:`という文字列をつなげて返す」というAPIを作るとします．
これは以下のように実装することができます．
```py
@app.route("/concat_speaker", methods=["POST"])
def concat_speaker():
    # 送られてきたリクエストのdataキーから要素を取得
    text = request.json["data"]

    return "system:" + text
```

新しいエンドポイントを作ったので，Unity側にも変更を行います．
エンドポイントを`http://127.0.0.1:8000/concat_speaker`に変更して，以下のような関数を新しく作成しましょう．

```C#
public async Task<HttpResponseMessage> SetConcatResponse(string user_input){

  var client = new HttpClient();

  // ユーザ発話をJSON型に変換
  var param = new Dictionary<string, object>()
  {
    ["data"]=user_input
  };
  var jsonString = Newtonsoft.Json.JsonConvert.SerializeObject(param);
  var content = new StringContent(jsonString, Encoding.UTF8, @"application/json");

  // Flask APIサーバにリクエストを送る
  var result = await client.PostAsync(@"http://127.0.0.1:8000/concat_speaker", content);
  var string_json = await result.Content.ReadAsStringAsync();
  var json_data = JObject.Parse(string_json);

  // 受け取ったデータを格納
  string system_response = json_data["response"].ToString();

  // 音声合成，画面へのテキスト表示を行う
  StartCoroutine(DownlowdFromVOICEVOX(system_response));

  return result;
}
```