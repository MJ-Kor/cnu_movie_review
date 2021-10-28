# Daum News에서 페이지를 돌면서 뉴스 기사의 제목과 본문을 수집

import requests
from bs4 import BeautifulSoup

# url2 = 'https://news.daum.net/breakingnews/digital?page=2'
# https://news.daum.net/breakingnews/digital # 실제 주소
# ?기준 page=2 오는 값 : 주소 x, 웹서버 넘겨주는 입력 값
count = 1
for page_num in range(1,4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(page_num)

    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    url_list = doc.select('ul.list_news2 a.link_txt')
    # 버튼 : a(앤커)태그, href변수에 주소가 들어있음
    new_url = []

    for url in (url_list):
        print('## NEWS -> {}번 #####################################'.format(count))
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
        count += 1