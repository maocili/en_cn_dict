import excel
class test(object):

    def __init__(self):
        self.word="go"
        print("input ok")

    def save(self):
        print('save is ok')
        excel.excel.word=self.word
        excel.excel.save()

test_install = test()
test_install.save()