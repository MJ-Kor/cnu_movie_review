# 웹 크롤링 => 네이버 뉴스

import requests
from bs4 import BeautifulSoup

# requests => 웹사이트 코드 복사 GET
# BeautifulSoup4 => GET 해온 코드에서 필요한 정보만 find해서 가져옴


url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, 'html.parser') # bs4한테 text를 전달
# result.text를 html.parser로 읽으세요
# title = doc.select('h3.tit_view')# 리스트 타입으로 반환
# title2 = doc.select('h3.tit_view')[0]
title = doc.select('h3.tit_view')[0].get_text() # 태그 정보 제외, 텍스트만
# h3 중에서 class가 tit_view인 것 .은 class 구분분# print(title)
# print(title2)
contents = doc.select('section p') # section에 포함된 p 태그들
contents.pop(-1)                     # 기자정보 삭제
content = ''                         # 본문 총합
for info in contents:
    content += info.get_text()
print('###############################################################')
print('# 뉴스 제목 : {}'.format(title))
print('###############################################################')
print('# 뉴스 본문 : {}'.format(content))