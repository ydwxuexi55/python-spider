
import requests

# 遍历页面
def looping_crawl_page(start_url,manager):
    ses = requests.Session()
    url_cur_page = start_url
    headers = ""
    while True:
        print(url_cur_page)

        r = ses.get(url_cur_page,headers=headers,timeout=10)
        # 通过解析网页  获得下一个url    或者是url列表
        url_next_url = ""
        if not url_next_url:
            print("已经到了最后一页。")
        else:
            url_cur_page=url_next_url




