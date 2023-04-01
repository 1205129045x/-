import pandas as pd
from urllib import request
import time,random,re,os
import urllib.request
from lxml import etree
from pandas.core.frame import DataFrame
import datetime

# 随机获取headers
def getheaders():
    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
    ]
    UserAgent = random.choice(user_agent_list)
    header = {'User-Agent':UserAgent}
    return header

# 获取页面html
def get_page(url):
    headers = getheaders()
    # 尝试，有时候连接不成功，就多试几次，避免中途中断
    attempts = 0
    success = False
    while attempts < 10 and not success:
        try:
            req = urllib.request.Request(url = url, headers = headers)
            html = urllib.request.urlopen(req).read().decode('utf_8')
            success = True
        except:
            attempts += 1
            if attempts == 10:
                break
    # time.sleep(random.random()*0.1)
    return html

# 获得每个页面的df
def get_df(url):
    html = get_page(url)
    df = pd.read_html(html)[2]
    return df

# 获取所有页面数量
def get_page_num(url):
    html = get_page(url)
    selector = etree.HTML(html)
    try:
        pagenums = selector.xpath('/html/body/div[3]/div/a[12]/@data-ci-pagination-page')[0]
    except:
        pagenums = selector.xpath('count(/html//div[@class="table_all"]/div/a)')
    return int(pagenums)

if __name__ == '__main__':
    columnnames = ['项目批准号', '项目类别', '学科分类', '项目名称', '立项时间', '项目负责人', '专业职务', '工作单位', '单位类别', '所在省区市', '所属系统', '成果名称', '成果形式', '成果等级', '结项时间', '结项证书号', '出版社', '出版时间', '作者', '获奖情况']
    df = DataFrame(columns = columnnames)
# 标准url http://fz.people.com.cn/skygb/sk/index.php/index/seach?pznum=&xmtype=0&xktype=0&xmname=%E6%A0%87%E5%87%86&lxtime=0&xmleader=&zyzw=0&gzdw=&dwtype=0&szdq=0&ssxt=0&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj=
    for i in range(2012,2013):
        print('****标准第{}年****'.format(i))
        url = 'http://fz.people.com.cn/skygb/sk/index.php/index/seach/2?pznum=&xmtype=0&xktype=0&xmname=%E6%A0%87%E5%87%86&lxtime=' + str(i) + '&xmleader=&zyzw=0&gzdw=&dwtype=0&szdq=0&ssxt=0&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj='
        # pagenums = get_page_num(url)
        pagenums = 2
        print('**共{}页**'.format(pagenums))
        for n in range(1, pagenums + 1):
            new_url_renzheng='http://fz.people.com.cn/skygb/sk/index.php/index/seach/' + str(n) + '?pznum=&xmtype=0&xktype=0&xmname=%E8%AE%A4%E8%AF%81&lxtime=0&xmleader=&zyzw=0&gzdw=&dwtype=0&szdq=0&ssxt=0&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj='
            # new_url_biaozhun='http://fz.people.com.cn/skygb/sk/index.php/index/seach/' + str(n) + '?pznum=&xmtype=0&xktype=0&xmname=%E6%A0%87%E5%87%86&lxtime=0&xmleader=&zyzw=0&gzdw=&dwtype=0&szdq=0&ssxt=0&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj='
            # new_url = 'http://fz.people.com.cn/skygb/sk/index.php/index/seach/' + str(n) + '?pznum=&xmtype=0&xktype=0&xmname=%E6%A0%87%E5%87%86&lxtime=' + str(i) + '&xmleader=&zyzw=0&gzdw=&dwtype=0&szdq=0&ssxt=0&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj='
            print(new_url_renzheng)
            newdf = get_df(new_url_renzheng)
            df = df.append(newdf, ignore_index=True)
            print('---第{}页已获取---'.format(n))


    df.to_excel('认证2012-2022.xlsx', index = 0)