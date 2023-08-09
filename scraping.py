import requests
import os
list_int = [i for i in range(1,120,1)]
def get_paper_titles(page):
    print(page)
    
    url = f""

    print(url)
    # Google Scholarへのリクエストを送信し、HTMLを取得
    response = requests.get(url)
    print(response)

    # # BeautifulSoupを使用してHTMLを解析
    # soup = BeautifulSoup(html, "html.parser")

    # # 論文タイトルを含む要素を検索
    # title_elements = soup.find_all("h3", class_="gs_rt")
    # print(title_elements)

    # # タイトルのテキストを取得
    # titles = [title.text for title in title_elements]
    # print(titles)


# キーワードを指定して論文タイトルを取得

keywords =["orb","slam","frame"]
for page in range(1,120,1):
    get_paper_titles(page)
    # try:
    #     paper_titles = get_paper_titles(page,keywords)
    # except:
    #     print("no document")
    #     exit(1)
    # else:
    #     for title in paper_titles:
    #         print(title)
