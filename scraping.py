import requests
from bs4 import BeautifulSoup

def get_paper_titles(page,keywords):
    delimiter="+"
    keyword =delimiter.join(keywords)
    url = f"https://scholar.google.co.jp/scholar?start={page}&q={keyword}"

    # Google Scholarへのリクエストを送信し、HTMLを取得
    response = requests.get(url)
    html = response.text

    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html, "html.parser")

    # 論文タイトルを含む要素を検索
    title_elements = soup.find_all("h3", class_="gs_rt")

    # タイトルのテキストを取得
    titles = [title.text for title in title_elements]

    return titles

# キーワードを指定して論文タイトルを取得

keywords =["orb","slam","frame"]
for page in range(0,91,10):
    print(f"start{page}")
    paper_titles = get_paper_titles(page,keywords)
    for title in paper_titles:
        print(title)
