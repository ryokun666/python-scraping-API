# Pythonを使ったスクレイピングで諸々のAPIたち

## URLから記事本文を取得する関数
 header:'/extract'
 
 テストURL↓↓↓
 
 http://127.0.0.1:5000/extract?url=https://morioh.com/p/215d1c10b5f5
@app.route('/extract', methods=['GET'])


## 任意のワードからGoogle検索を行い一番上に出てきたサイトのURLを取得する関数
 header:'/search'
 
 テストURL↓↓↓
 
 http://127.0.0.1:5000/search?q=ドラえもん　のび太
 
@app.route('/search', methods=['GET'])

