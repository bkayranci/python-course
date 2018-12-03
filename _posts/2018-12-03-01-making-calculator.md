---
layout: post
title: "Hesap Makinesi"
description: "PyQt5 ile hesap makinesi yapımı"
tags: [code, example]
---

1- Çalışma dosyamıza `main.py` isimli bizim uygulamamızı çalıştıracağımız bir dosya ekliyoruz.

{% include image.html path="new-form-extension.png" path-detail="new-form-extension.png" alt="Yeni tasarım oluşturma" %}

2- Daha sonra visual studio code editöründen sağ tıklayıp, `New Form` butonuna tıklayarak;

- `Grid Layout`
- `Line Edit`
- `Push Button`

öğelerini sürekleyerek hesap makinesi görünümümüzü oluşturacağız.

{% include image.html path="calculator-designer.png" path-detail="calculator-designer.png" alt="Hesap makinesi görünümü" %}

3- `main.py` dosyamızda bu butonlara erişmek istediğimizde kullanmak istediğimiz nesne isimlerini ilgili öğenin üzerine sağ tıklayıp `change ObjectName` butonuna tıklayarak değiştirelim.

4- Bu tasarımı `hesapmakinesi.ui` dosyası olarak kaydedelim.

5- Visual studio code editöründen sağ tarafta bulunan dosyaya sağ tıklayıp, `Compile Form` seçeneğine tıklayarak oluşturduğumuz tasarımın python kodlarını otomatik oluşturalım. Bu işlemin sonunda `Ui_hesapmakinesi.py` isimli bir python dosyasının oluştuğunu göreceğiz.

6- Buradan sonra yaptığımız tasarımı uygulamamıza entegre ederken `Ui_hesapmakinesi.py` dosyasını kullanacağız.

Örnek bir `main.py` dosyası:

{% highlight python %}

from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_hesapmakinesi import Ui_MainWindow
import sys

class HesapMakinesi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(HesapMakinesi, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    h = HesapMakinesi()
    h.show()

    sys.exit(app.exec_())

{% endhighlight %}


7- Şimdi ise bu tasarladığımız butonlara tıklandığında ne olması gerektiğini `main.py` dosyamızda belirtelim.

{% highlight python %}

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Ui_hesapmakinesi import Ui_MainWindow
import sys

class HesapMakinesi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(HesapMakinesi, self).__init__()
        self.setupUi(self)
        self.btn0.clicked.connect(self.tiklandi)
        self.btn1.clicked.connect(self.tiklandi)
        self.btn2.clicked.connect(self.tiklandi)
        self.btn3.clicked.connect(self.tiklandi)
        self.btn4.clicked.connect(self.tiklandi)
        self.btn5.clicked.connect(self.tiklandi)
        self.btn6.clicked.connect(self.tiklandi)
        self.btn7.clicked.connect(self.tiklandi)
        self.btn8.clicked.connect(self.tiklandi)
        self.btn9.clicked.connect(self.tiklandi)
        self.btnArti.clicked.connect(self.tiklandi)
        self.btnEksi.clicked.connect(self.tiklandi)
        self.btnCarpi.clicked.connect(self.tiklandi)
        self.btnBolme.clicked.connect(self.tiklandi)
        self.btnSonuc.clicked.connect(self.hesapla)
        self.btnTemizle.clicked.connect(self.clear)

    def clear(self):
        self.txtEkran.clear()
    
    def hesapla(self):
        self.txtEkran.setText(str(eval(self.txtEkran.text())))

    def tiklandi(self):
        sender = self.sender()
        self.txtEkran.setText(self.txtEkran.text() + sender.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    h = HesapMakinesi()
    h.show()

    sys.exit(app.exec_())


{% endhighlight %}