# import requests
# from bs4 import BeautifulSoup
# import re
# proxies = { "http": "http://127.0.0.1:1080","https": "https://127.0.0.1:1080" }
# url='https://bigbigbananas.tumblr.com/following/page/'
# def get_all_blog_address(url,page_id):
#     #page_id 从1开始
#     list_address = []
#     r = requests.get(url=url+str(page_id),timeout=5,proxies=proxies)
#     r.encoding='utf-8'
#     soup = BeautifulSoup(r.text, "html.parser")
#     blog_address = soup.select('.blog-name')

#     if len(blog_address)!=0:
#         for x in range(0,len(blog_address)):
#             list_address.append(blog_address[x].get('href'))
#     print(list_address)
#     return list_address

# get_all_blog_address(url,1)

# blog_address='http://slutmoonbeam.tumblr.com/page/2'
# def getHtml(url):
#     try:
#         page = requests.get(url,timeout=5,proxies=proxies)
#         html = page.content.decode('utf-8')
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


# import requests

# url = "https://api8.pcloud.com/downloadfile"

# querystring = {"folderid":"0","progresshash":"upload-9087083-xhr-496","nopartial":"1","url":"http://vt.media.tumblr.com/tumblr_ohi9mbrbwY1vlyevp.mp4","auth":"mS9A7XZT5kwZOX744AA1zmhExgU2VIy63V1dsByk"}

# payload = ""
# headers = {
#     'accept': "application/json, text/javascript, */*; q=0.01",
#     'origin': "https://my.pcloud.com",
#     'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
#     'referer': "https://my.pcloud.com/",
#     'accept-encoding': "gzip, deflate, br",
#     'accept-language': "zh-CN,zh;q=0.8",
#     'cache-control': "no-cache",
#     'postman-token': "cb960d50-70f9-3ad5-d8db-abdb20aff0f8"
#     }

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

# print(response.text)

# aa ={'result': 0, 'metadata': [{'videocodec': 'h264', 'comments': 0, 'height': 360, 'audiocodec': 'aac', 'name': 'tumblr_o6zupfX0Xc1u7poit.mp4', 'created': 'Thu, 09 Feb 2017 02:40:14 +0000', 'icon': 'video', 'category': 2, 'contenttype': 'video/mp4', 'audiobitrate': 62, 'thumb': True, 'videobitrate': 1010, 'parentfolderid': 0, 'width': 640, 'fileid': 2155668483, 'size': 2993312, 'fps': '30.00', 'isfolder': False, 'path': '/tumblr_o6zupfX0Xc1u7poit.mp4', 'modified': 'Thu, 09 Feb 2017 02:49:31 +0000', 'hash': 291473307810560467, 'audiosamplerate': 44100, 'rotate': 0, 'ismine': True, 'id': 'f2155668483', 'isshared': False, 'duration': '22.22'}]}
# print(aa['metadata'][0]['name'])
# print(aa.items())