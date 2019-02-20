# YouTube Data API(v3)入門

---

## YouTube Data APIを使う前に

- Googleアカウントが必要
- アプリケーションの登録が必要
- 上記を行ってAPIキーを取得することが必要

+++

## Googleアカウントの作成

省略！

+++

## アプリケーションの登録

- ﻿Google Developers Console
  - https://console.developers.google.com/?hl=ja
- まずプロジェクトを作成する
  
![](gpimage/003.PNG)

+++

![](gpimage/004.PNG)

+++

- プロジェクト名はてきとう

![](gpimage/005.PNG)

+++

- プロジェクトを選択

![](gpimage/006.PNG)

+++

- APIを追加していく

![](gpimage/001.PNG)

+++

- YoutTube Data API v3を選ぶ

![](gpimage/002.PNG)

+++

- APIを有効にする

![](gpimage/007.PNG)

+++

- APIキーを登録する
  - 認証情報を追加する

![](gpimage/008.PNG)

+++

![](gpimage/009.PNG)

+++

- 使用するAPI -> YouTube Data API v3
- APIを呼び出す場所 -> その他UI
- アクセスするデータの種類 -> 一般公開データ

+++

<img src="gpimage/010.PNG" height="400" />

+++

- ここのAPIキーをコピペする。

![](gpimage/011.PNG)

+++

- 事前準備は以上で終了。

---

## 基本的な流れ

1. APIキーを呼び出す
1. APIキーを使ってHTTPリクエストを投げる
1. 情報を受け取る
1. パースする

---

## APIキーを呼び出す

- "Key"というファイルを作ってそこから呼び出す
- ほんとは環境変数のファイルとか作ってやった方がいいかも

+++

```python
KEY_FILENAME = "Key"


def main():
    with open(file=KEY_FILENAME, mode='r', encoding='utf-8') as f:
        API_KEY = f.readline()
    print(API_KEY)
    print("↑APIキー")


if __name__ == '__main__':
    main()
```

---

## APIキーを使ってHTTPリクエストを投げる

- APIエンドポイントの確認
  - https://www.googleapis.com/youtube/v3/
- 詳細はAPIのリファレンスを参照
  - https://developers.google.com/youtube/v3/docs/?hl=ja

+++

- 今回は検索機能を利用してみる
- エンドポイント + `search`

+++

- `search?part=snippet&q={}&order=date&maxResults={}&key={}`

+++

- データは詳細が欲しい -> `search?part=snippet`
- キーワードで検索する -> `&q={}`
- 日付でソートする -> `&order=date`
- 検索結果の数を指定する（デフォルトは5） -> `&maxResults={}`
- APIキーの情報を付与する -> `&key={}`

+++

- URLを実際に生成してアクセスしてみる
```python
    search_url = YOUTUBEAPI_ENDPOINT + "search?part=snippet&q={}&order=date&maxResults={}&key={}"

    print(search_url.format(
        "DaiGo",
        50,
        API_KEY
    ))
```

```ps1
https://www.googleapis.com/youtube/v3/search?part=snippet&q=DaiGo&order=date&maxResults=50&key=APIキー
```

+++

```json
{
 "kind": "youtube#searchListResponse",
 "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/RpspygOeyYCL80ksg5defsXLjhk\"",
 "nextPageToken": "CAUQAA",
 "regionCode": "JP",
 "pageInfo": {
  "totalResults": 1000000,
  "resultsPerPage": 5
 },
 "items": [
  {
   "kind": "youtube#searchResult",
   "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/DeQCMZdyQbZqDQK1A7noauzFAuA\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "8qdxiRm9r7g"
   },
   "snippet": {
    "publishedAt": "2019-02-20T02:58:43.000Z",
    "channelId": "UCFdBehO71GQaIom4WfVeGSw",
    "title": "筋トレは何日サボると筋肉減るのか判明",
    "description": "リサーチ協力:年5000論文を読むパレオな男▷http://ch.nicovideo.jp/paleo DaiGoの無料メンタルアプリ▷https://ch.nicovideo.jp/mentalist/blomaga/ar1712447 おいしい ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/8qdxiRm9r7g/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/8qdxiRm9r7g/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/8qdxiRm9r7g/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "メンタリスト DaiGo",
    "liveBroadcastContent": "none"
   }
  },
  ...
```

+++

- これでデータは取れそう
- リクエストを投げる
  - リクエストの種類に関してはおぐぐりください

+++

- GETリクエスト

```python
import requests # requestsライブラリ、HTTPリクエストなどの処理をやってくれる
from pprint import pprint # pprintライブラリ、jsonの成型表示とか便利
```

```python
    response = requests.get(search_url.format(
        "DaiGo", # キーワードは"DaiGo"
        50, # 検索結果は最大の50
        API_KEY # APIキー情報を付ける
    ))
    res_json = response.json()
    pprint(res_json)
```

+++

- `リクエストを投げる` ＋ `情報を受け取る`、が完了した

---

## パースする

