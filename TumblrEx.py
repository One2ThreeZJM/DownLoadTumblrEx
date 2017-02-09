import requests
from bs4 import BeautifulSoup
import re
import json
import time

proxies = { "http": "http://127.0.0.1:1080","https": "https://127.0.0.1:1080" }
timeout = 5


def getHTML(url):
    try:
        page = requests.get(url = url,timeout=timeout,proxies=proxies)
        return page.content.decode('utf-8')
    except:
        print('The URL you requested could not be found in Module Video')
        return 'Html'

def get_blog_address(url):
    # url='https://bigbigbananas.tumblr.com/following/page/1'
    html = getHTML(url)
    soup = BeautifulSoup(html, "html.parser")
    blog_address = soup.select('.blog-name')
    
    list_address = []
    if len(blog_address)!=0:
        for x in blog_address:
            list_address.append(x.get('href'))
    print(list_address)
    return list_address

def get_page_mp4(url):
    # blog_address='http://slutmoonbeam.tumblr.com/page/2'
    downurl = 'http://vt.media.tumblr.com/'
    html =getHTML(url)
    reg = r'<iframe src=\'(https\://www\.tumblr\.com/video/.*?)\''
    videopagere = re.compile(reg)
    videopageurl = re.findall(videopagere, html)
    list_url = []

    if videopageurl:
        for x in videopageurl:
            videohtml = getHTML(x)
            reg_url = r'<source src="(https://www.tumblr.com/video_file/t:.*?)" type="video/mp4">'
            videore = re.compile(reg_url)
            videourl = re.findall(videore, videohtml)[0]
            list_url.append(downurl+videourl[72:96]+'.mp4')
    # print(list_url)
    return list_url

def post_pccloud(post_url):
    # url = "http://vt.media.tumblr.com/tumblr_o6zupfX0Xc1u7poit.mp4"
    url = "https://api8.pcloud.com/downloadfile"

    querystring = {"folderid":"0","progresshash":"upload-9087083-xhr-496","nopartial":"1","url":"http%3A%2F%2Fvt.media.tumblr.com%2Ftumblr_nqt6lx9nYw1tb92og.mp4","auth":"mS9A7XZT5kwZOX744AA1zmhExgU2VIy63V1dsByk"}
    querystring['url']= post_url
    payload = ""
    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'origin': "https://my.pcloud.com",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        'referer': "https://my.pcloud.com/",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'cache-control': "no-cache",
        'postman-token': "45c3ef40-d05d-c594-df12-caac7a5e25d8"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    text = json.loads(response.text)
    print(text)
    # if text['result']==0:
    #     try:
    #         print('上传文件成功：',text['metadata'][0]['name'])
    #     except Exception as e:
    #         raise e

# 


def main():

    # templist = []
    # for x in range(1,10):
    #     temp = get_blog_address(url+str(x))
    #     if len(temp)!=0:
    #         templist.append(temp)
    #     else:
    #         break
    mylist = []
    for x in templist:
        for y in x:
            mylist.append(y+'page/')
    
    temp_mp4 = []
    for x in mylist:
        for y in range(1,10):
            temp = get_page_mp4(x+str(y))
            if len(temp) !=0 :
                for z in temp:
                    # time.sleep(2)
                    post_pccloud(z)


if __name__ == '__main__':
    url='https://bigbigbananas.tumblr.com/following/page/'
    templist=[['https://mugoujiayi.tumblr.com/', 'http://shiyanan901210.tumblr.com/', 'http://sexysze.tumblr.com/', 'http://dusadoggy.tumblr.com/', 'http://lewdbitchgirl.tumblr.com/', 'http://76039.tumblr.com/', 'http://mugousissi.tumblr.com/', 'http://skymonk-s.tumblr.com/', 'https://miyadog.tumblr.com/', 'http://fateagel.tumblr.com/'], ['http://xnandly.tumblr.com/', 'http://chujue1987.tumblr.com/', 'http://uwo8.tumblr.com/', 'http://fuckme018.tumblr.com/', 'http://nicaiwoainime.tumblr.com/', 'http://mangoddd.tumblr.com/', 'http://srar3131.tumblr.com/', 'http://pamelang.tumblr.com/', 'http://sexy6girl9.tumblr.com/', 'http://aoooo1992.tumblr.com/'], ['https://xuanxuan0615.tumblr.com/', 'http://yaopaipai.tumblr.com/', 'https://fakekelsa.tumblr.com/', 'http://piaoliangpigu.tumblr.com/', 'https://sexbbpig.tumblr.com/', 'http://halipoo.tumblr.com/', 'http://3u1u1u.tumblr.com/', 'http://pussynah.tumblr.com/', 'http://srlive.tumblr.com/', 'http://happybabyeyes.tumblr.com/'], ['http://scatmcat.tumblr.com/', 'http://greenhat1314.tumblr.com/', 'http://yamakaso.tumblr.com/', 'http://yoursweetslovegirlworld.tumblr.com/', 'https://yoyo0508.tumblr.com/', 'http://jackrousi666.tumblr.com/', 'http://xjloveml.tumblr.com/', 'http://mrmmm233.tumblr.com/', 'http://r65270.tumblr.com/', 'http://xx1026.tumblr.com/'], ['http://yemao53113.tumblr.com/', 'https://mizhichasao.tumblr.com/', 'http://xiaoming-xiaotiandi.tumblr.com/', 'http://lelenvwang.tumblr.com/', 'http://slutmoonbeam.tumblr.com/', 'http://prinprin25.tumblr.com/', 'http://oreocool.tumblr.com/']]
    main()

# # blog_address='http://slutmoonbeam.tumblr.com/page/2'
# # get_page_mp4(blog_address)

# aa= {'result': 0, 'metadata': [{'height': 270, 'path': '/tumblr_o1y4kxhhOS1ta42xh.mp4', 'created': 'Thu, 09 Feb 2017 03:27:34 +0000', 'width': 480, 'category': 2, 'contenttype': 'video/mp4', 'ismine': True, 'audiosamplerate': 22050, 'audiobitrate': 126, 'modified': 'Thu, 09 Feb 2017 03:42:46 +0000', 'comments': 0, 'fps': '30.00', 'videocodec': 'h264', 'hash': 9237915073383151591, 'fileid': 2155791500, 'parentfolderid': 0, 'icon': 'video', 'duration': '298.40', 'id': 'f2155791500', 'videobitrate': 1353, 'isshared': False, 'isfolder': False, 'rotate': 0, 'thumb': True, 'size': 55391743, 'audiocodec': 'aac', 'name': 'tumblr_o1y4kxhhOS1ta42xh.mp4'}]}

# bb={'result': 0, 'metadata': []}


