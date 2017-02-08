import requests
from bs4 import BeautifulSoup
import re
import urllib.request

url='https://bigbigbananas.tumblr.com/following/page/'
def get_all_blog_address(url,page_id):
    #page_id 从1开始
    list_address = []
    r = requests.get(url=url+str(page_id),timeout=10)
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text, "html.parser")
    blog_address = soup.select('.blog-name')

    if len(blog_address)!=0:
        for x in range(0,len(blog_address)):
            list_address.append(blog_address[x].get('href'))
    print(list_address)
    return list_address

get_all_blog_address(url,3)

# blog_address='http://slutmoonbeam.tumblr.com/page/2'
# def getHtml(url):
#     try:
#         page = urllib.request.urlopen(url)
#         html = page.read().decode('utf-8')
#         return html
#     except:
#         print('The URL you requested could not be found in Module Video')
#         return 'Html'

# # http://vt.media.tumblr.com/tumblr_o97j6zzYpG1vnl0qg.mp4

# def getMP4(url):
#     downurl = 'http://vt.media.tumblr.com/'
#     html =getHtml(url)
#     reg = r'<iframe src=\'(https\://www\.tumblr\.com/video/.*?)\''
#     videopagere = re.compile(reg)
#     videopageurl = re.findall(videopagere, html)
#     list_url = []
#     if videopageurl:
#         for x in videopageurl:
#             videohtml = getHtml(x)
#             reg_url = r'<source src="(https://www.tumblr.com/video_file/t:.*?)" type="video/mp4">'
#             videore = re.compile(reg_url)
#             videourl = re.findall(videore, videohtml)[0]
#             list_url.append(downurl+videourl[72:96]+'.mp4')
    
#     return list_url     
    

# print(getMP4(blog_address))
