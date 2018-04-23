import  os
import  openpyxl


class save(object):
    def __init__(self):
        self.num = 1
        self.start()

    def sheet(self):
        sheet01 = self.wb.get_sheet_by_name('Sheet1')
        print(sheet01.max_row)


    def start(self):
        if os.path.exists('./excel/dict.xlsx'):
            self.wb = openpyxl.load_workbook('./excel/dict.xlsx')
            self.sheet()

save_test = save()