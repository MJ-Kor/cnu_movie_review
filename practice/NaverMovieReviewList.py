# Naver 영화(1개 선택) 리뷰 정보를 수집(review, score, writer, date)
import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
result = requests.get(url,headers = headers)
doc = BeautifulSoup(result.text, 'html.parser')
review_list = doc.select('div.score_result > ul > li')

for i, one in enumerate(review_list):
    print('## USER -> {} ###############################################'.format(i + 1))

    # 평점 정보 수집
    score = one.select('div.star_score > em')[0].get_text()

    # 리뷰 정보 수집
    review = one.select('div.score_reple > p > span')
    j = 0

    if len(review) == 2:
        j = 1
    elif len(review) == 3:
        j = 2

    review_text = review[j].get_text().strip()

    # 작성자(닉네임) 정보 수집
    original_writer = one.select('div.score_reple dt em')[0].get_text().strip()
    idx_end = original_writer.find('(')
    writer = original_writer[0:idx_end]
    # 날짜 정보 수집
    original_date = one.select('div.score_reple dt em')[1].get_text()
    date = original_date[:10]


    print(':: REVIEW: {}'.format(review_text))
    print(':: WRITER: {}'.format(writer))
    print(':: SCORE: {}'.format(score))
    print(':: DATE: {}'.format(date))
