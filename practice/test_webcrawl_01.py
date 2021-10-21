# 웹 크롤링 => 네이버 뉴스

import requests
from bs4 import BeautifulSoup

# conda activate cnu
# install -c anaconda requests
# install -c anaconda beautifulsoup4
# conda list ( 추가 되었는지 확인 )

# requests => 웹사이트 코드 복사 GET
# BeautifulSoup4 => GET 해온 코드에서 필요한 정보만 find해서 가져옴


url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, 'html.parser') # bs4한테 text를 전달
# title = doc.select('h3.tit_view')# 리스트 타입으로 반환
# title2 = doc.select('h3.tit_view')[0]
title3 = doc.select('h3.tit_view')[0].get_text() # 태그 정보 제외, 텍스트만
# print(title)
# print(title2)
print('# 뉴스제목 : {}'.format(title3))