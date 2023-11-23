import sys
from PyQt5 import QtWidgets
from doviz_tasari import Ui_MainWindow 
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon,QPixmap

import requests
import json

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_convert.clicked.connect(self.convert)
        self.url = "https://api.apilayer.com/exchangerates_data/latest?base="
        self.payload = {}
        self.headers= {
          "apikey": "XEggDogcz0897NJIzcGBLBRW8e2V1jQN"
        }

    def convert(self):
        alinan_doviz = self.ui.txt_alinan.text()
        bozulan_doviz = self.ui.txt_bozulan.text()
        doviz_miktar = int(self.ui.txt_miktar.text())
        
        response = requests.request("GET", self.url+bozulan_doviz, headers=self.headers, data = self.payload)
        status_code = response.status_code

        result = response.text
        sonuc = json.loads(result)
        if sonuc["base"] == bozulan_doviz:
            s = "Other equivalents of "+str(bozulan_doviz)+" : \nOur other API variables are here too :"+result      #str(sonuc["rates"])
            self.ui.txt_browser.setText(s)
            self.ui.lbl_exc.setText(bozulan_doviz)
            self.ui.lbl_bir_birim.setText(str(sonuc["rates"][alinan_doviz])+" "+alinan_doviz)
            self.ui.lbl_equ_of_un.setText("1 "+bozulan_doviz+" = ")
            self.ui.lbl_kac_para.setText(str(doviz_miktar * sonuc["rates"][alinan_doviz])+" "+alinan_doviz)
        else:
            self.ui.lbl_uyari.setText("Check your enthernet connection or Make sure you entered the currency name correctly.")


'''url = "https://api.apilayer.com/exchangerates_data/latest?base=" #"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

#XEggDogcz0897NJIzcGBLBRW8e2V1jQN
#0c1a23fb2b1fb3093b24d1d5920f26d0

payload = {}
headers= {
  "apikey": "XEggDogcz0897NJIzcGBLBRW8e2V1jQN"
}

#key = "0c1a23fb2b1fb3093b24d1d5920f26d0"

#url2 = "https://api.apilayer.com/exchangerates_data/convert?to="+alinan_doviz+"from="+bozulan_doviz+"amount="+str(miktar) #+"?access_key=" + key
#response = requests.request("GET",url2,headers=headers,data=payload)
#status_code = response.status_code
#result = response.text
#print(result)


response = requests.request("GET", url+bozulan_doviz, headers=headers, data = payload)
status_code = response.status_code
result = response.text
print(result)
result = json.loads(result)
print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar * result["rates"][alinan_doviz],alinan_doviz))'''


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()