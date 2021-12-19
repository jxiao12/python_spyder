import sys
from bs4 import BeautifulSoup as bs
import os
import re
import urllib.request, urllib.response, urllib.error, urllib.parse
import xlwt
import sqlite3
import ssl


findLink = re.compile(r'<a href="(.*?)">')    #生成正则表达式对象，表示规则
findImage = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findRatingNum = re.compile(r'<span>(\d*)人评价</span>')
findIntruc = re.compile(r'<span class="inq">(.*)</span>')
findInfor = re.compile(r'<p class="">(.*?)</p>', re.S)

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    baseurl = "https://movie.douban.com/top250?start="
    savepath = "Top250.xls"


    # 爬取网页
    datalist = getData(baseurl)
    # 逐一解析数据

    # 保存数据
    #saveData(savepath, datalist)
    #askUrl(baseurl)
    dbpath = "Top movie.db"
    saveSQlite(datalist, dbpath)

# 爬取网页
def getData(baseurl):
    datalist = []
    # 逐一解析数据
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)


        soup = bs(html, "html.parser")
        for item in soup.find_all("div", class_="item"): # 查找符合要求的字符串，形成列表
            data = [] # 保存一部电影的所有信息
            items = str(item)


            link = re.findall(findLink, items)[0]  # re库通过正则表达式找指定字符串
            data.append(link)

            image = re.findall(findImage, items)[0]
            data.append(image)

            name = re.findall(findTitle, items)
            if (len(name) == 2):
                data.append(name[0])
                data.append(name[1].replace("/", ""))
            else:
                data.append(name)
                data.append(" ")

            rating = re.findall(findRating, items)[0]
            data.append(rating)

            rateuNum = re.findall(findRatingNum, items)[0]
            data.append(rateuNum)

            intro = re.findall(findIntruc, items)
            if (len(intro) != 0):
                data.append(intro[0].replace(".", ""))
            else:
                data.append(" ")

            infor = re.findall(findInfor, items)[0]
            infor = re.sub('<br(\s+)?/>(\s+)?', " ", infor)
            infor = re.sub('/', " ", infor)
            data.append(infor.strip())

            datalist.append(data)


    return datalist


# 得到指定一个URL的网页内容
def askUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    html = ""
    try:
        respones = urllib.request.urlopen(request)
        html = respones.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html

def saveSQlite(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for item in datalist:
        for ele in range(len(item)):
            if ele == 4 or ele == 5:
                continue
            item[ele] = '"' + str(item[ele]) + '"'
        sql = '''
        insert into movieTop250
        (
        info_link, pic_link, china_name,
        foreign_name, rating, ratingNum,
        introduction, infor
        )values(%s)
        '''%",".join(item)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()



def init_db(dbpath):
    sql = '''
        create table movieTop250
        (
        id integer  primary key autoincrement,
        info_link text,
        pic_link text,
        china_name varchar ,
        foreign_name varchar ,
        rating numeric ,
        ratingNUm numeric, 
        introduction text,
        infor text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
# 保存数据
def saveData(savepath, data):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet("Movie", cell_overwrite_ok=True)
    col = ("电影详情链接", "电影图片链接", "中文名", "外文名", "评分", "评分人数", "评语", "简介")
    for i in range(len(col)):
        worksheet.write(0, i, col[i])
    for ele, index in enumerate(data):
        for in_ele, in_index in enumerate(index):
            worksheet.write(ele + 1, in_ele, in_index)
    workbook.save(savepath)

if __name__ == '__main__':
    main()
    #init_db("movie.db")