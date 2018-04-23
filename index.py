from bs4 import  BeautifulSoup
import requests

class index(object):

    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        self.local = 'http://dict.cn/'
        self.answer = []
    def start(self):
        get_html = requests.get(url=self.local+self.word,headers = self.header) #获取html
        soup = BeautifulSoup(get_html.text,'lxml')
        en_div = soup.find_all("div",class_="layout detail") #其中查找英文单词div class 为layout detail
        cn_div = soup.find_all("div",class_ = "layout cn")  #而中文的div class 为 latout cn


        # 截取en中的 li标签
        if len(en_div) == 1:
            for d in en_div:
                for li in d.find_all("li"):
                    self.answer.append(li.text)

            for s in self.answer:
                print(s)



        # 截取cn中的 li标签
        elif len(cn_div) == 1:
            for d in cn_div:
                for li in d.find_all("li"):
                    self.answer.append(li.text)

            for s in self.answer:
                print(s)

        else:
            print("未查询成功")

    def cn_show(self):
        self.word = str(input('>>>>'))
        self.start()

index_install = index()