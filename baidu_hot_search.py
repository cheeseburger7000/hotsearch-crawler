import requests
from bs4 import BeautifulSoup
import json

BAIDU_ROOT_URL = 'https://www.baidu.com/'
baidu_hot_search_url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=baidu&fenlei=256&rsv_pq=8c475a4100039a9a&rsv_t=98e0bG6P16UQ5U9Y8uEvs3S3c1Le7P52pP7DjOoQb56LpYtxYJtFVHHtgJQ&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_sug3=7&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=baidu&rsp=0&inputT=1052&rsv_sug4=3762'

res = requests.get(baidu_hot_search_url)
status = res.status_code
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    result = []
    tables = soup.find_all('table', class_='c-table opr-toplist1-table')[0].find_all('tbody')
    for table in tables:
        main = table.find_all('td', class_='toplist1-td opr-toplist1-link')
        for item in main:
            news = {}
            rank = item.find_all('span')[0].text.strip() # todo 热tag
            url_title = item.find('a', href=True)
            relative_url = url_title['href']
            title = url_title.text.strip()
            news['rank'] = int(rank)
            news['url'] = BAIDU_ROOT_URL + relative_url
            news['title'] = title
            result.append(news)
    print(result)
