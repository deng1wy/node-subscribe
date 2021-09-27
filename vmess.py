import base64
from bs4 import BeautifulSoup

import requests

if __name__ == '__main__':
    url = "https://github.com/learnhard-cn/free_proxy_ss/blob/main/v2ray/v2raysub"
    content = requests.get(url).content
    document = BeautifulSoup(content, features="lxml")
    source = document.find("td", id="LC1").text
    result = base64.b64decode(source).decode("utf-8")
    print(result)
