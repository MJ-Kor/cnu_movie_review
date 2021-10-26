# WebCrawling
# Daum News 목록 통해 여러건의 기사와 본문을 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
url_list = doc.select('ul.list_news2 a.link_txt')
# 버튼 : a(앤커)태그, href변수에 주소가 들어있음
new_url = []
for i, url in enumerate(url_list):
    print('## NEWS -> {}번 #####################################'.format(i+1))
    new_url = url['href']
    print('# URL: {}'.format(new_url))

    result = requests.get(new_url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')
    contents.pop(-1)
    content = ''
    for info in contents:
        content += info.get_text()
    print('# 뉴스 제목 : {}'.format(title))
    print('# 뉴스 본문 : {}'.format(content))

