from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
url = 'https://greasyfork.org/zh-CN/scripts'
def get_one_page(url):
    # 设置爬虫网页和headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/80.0.3987.163 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

# 用BeautifulSoup提取有效信息

def find_name(response):
    soup = BeautifulSoup(response, "html.parser")
    info = soup.find_all('li')
    list = []
    with open('data.csv', 'w', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['text', 'daily_install', 'total_instal'])
        # print(info)
        for i in info:
            name = i.get('data-script-name')
            daily_install = i.get('data-script-daily-installs')
            tot_install = i.get('data-script-total-installs')
            if (name):
                writer.writerow([name, daily_install, tot_install])
                templist = [name, daily_install, tot_install]
                print(templist)
                list.append(templist)
    return list

def main():
    response = get_one_page(url)
    soup = find_name(response)
    # print(soup)
    data = pd.DataFrame(data=find_name(response),columns=['name','daily_install','tot_install'])
    data.to_excel("data.xlsx")
main()
