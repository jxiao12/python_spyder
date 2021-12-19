import urllib.request, urllib.response, urllib.error, urllib.parse
import ssl

"""
try:
    res = urllib.request.urlopen("http://www.baidu.com", timeout=0.001)
    print(res.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("no enough time")
"""

# res = urllib.request.urlopen("http://www.baidu.com")
# print(res.status)
#
# print(res.getheaders())
#
# print(res.getheader("Bdqid"))


"""
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
#url = "http://movie.douban.com/top250?start="
url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"name":"eric"}), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
respones = urllib.request.urlopen(req)
print(respones.read().decode("utf-8"))
"""

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.google.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=headers)
respones = urllib.request.urlopen(req)
print(respones.read().decode("utf-8"))