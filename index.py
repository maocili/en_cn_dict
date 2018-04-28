import  inquiry
import  excel
import sys
import os


class index(object):

    def __init__(self):

        self.local_path='.\\excel\\dict.txt'

        self.word = str(input('>>>>'))
        self.Local_search()
        self.local_word =[]

        #inquiry.inquiry_install.start(self)



    def Local_search(self):
        if not os.path.exists(self.local_path):
            print("生成")
        with open(self.local_path,'r',encoding='utf8')as f:
            while True:
                line = f.readline()
                if line:
                    print(line)
                else:
                    break

        f.close()


index_install = index()