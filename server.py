from flask import Flask, jsonify, request

from newspaper import Article
from googlesearch import search


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def extract_main_content(url):
    try:
        article = Article(url, language='ja')
        article.download()
        article.parse()

        extracted_text = article.text
        return extracted_text

    except Exception as e:
        return str(e)

# URLから記事本文を取得する関数
# header:'/extract'
# テストURL↓↓↓
# http://127.0.0.1:5000/extract?url=https://morioh.com/p/215d1c10b5f5
@app.route('/extract', methods=['GET'])
def extract():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    extracted_text = extract_main_content(url)
    return jsonify({'url': url, 'extracted_text': extracted_text})

# 任意のワードからGoogle検索を行い一番上に出てきたサイトのURLを取得する関数
# header:'/search'
# テストURL↓↓↓
# http://127.0.0.1:5000/search?q=ドラえもん　のび太
@app.route('/search', methods=['GET'])
def google_search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "検索ワードが見つかりませんでした。"}), 400

    try:
        urls = [j for j in search(query, num_results=1)]
        if urls:
            return jsonify({"top_result": urls[0]})
        else:
            return jsonify({"error": "検索結果が見つかりませんでした。"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
