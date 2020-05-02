# @ykslkrkci tarafından Persona Non Grata için Hazırlanmıştır.
# Şarapçı arkadaşım @keyiflerolsun'a selam olsun :)
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def back(self):
        self.webView.back()

    def forward(self):
        self.webView.forward()

    def reload(self):
        self.webView.reload()

    def home(self):
        self.webView.load(QtCore.QUrl("http://www.google.com"))
        self.lineEdit.setText("http://www.google.com")






    def setupUi(self, Form):
        self.say = 0
        Form.setObjectName("Form")
        Form.resize(1087, 584)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.geri = QtWidgets.QPushButton(Form)
        self.geri.setObjectName("geri")
        self.horizontalLayout.addWidget(self.geri)
        self.ileri = QtWidgets.QPushButton(Form)
        self.ileri.setObjectName("ileri")
        self.horizontalLayout.addWidget(self.ileri)
        self.yenile = QtWidgets.QPushButton(Form)
        self.yenile.setObjectName("yenile")
        self.horizontalLayout.addWidget(self.yenile)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("http://")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.ara = QtWidgets.QPushButton(Form)
        self.ara.setObjectName("ara")
        self.horizontalLayout.addWidget(self.ara)
        self.anasayfa = QtWidgets.QPushButton(Form)
        self.anasayfa.setObjectName("anasayfa")
        self.horizontalLayout.addWidget(self.anasayfa)
        self.sekmeolustur = QtWidgets.QPushButton(Form)
        self.sekmeolustur.setObjectName("sekmeolustur")
        self.horizontalLayout.addWidget(self.sekmeolustur)
        self.ayarlar = QtWidgets.QPushButton(Form)
        self.ayarlar.setObjectName("ayarlar")
        self.horizontalLayout.addWidget(self.ayarlar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.YeniSekme = QtWidgets.QTabWidget(Form)
        self.YeniSekme.setObjectName("YeniSekme")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.webView = QtWebKitWidgets.QWebView(self.tab_3)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.horizontalLayout_3.addWidget(self.webView)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.YeniSekme.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.webView_2 = QtWebKitWidgets.QWebView(self.tab_4)
        self.webView_2.setUrl(QtCore.QUrl("about:blank"))
        self.webView_2.setObjectName("webView_2")
        self.horizontalLayout_5.addWidget(self.webView_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.YeniSekme.addTab(self.tab_4, "")
        self.horizontalLayout_2.addWidget(self.YeniSekme)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.geri.clicked.connect(self.back)
        self.yenile.clicked.connect(self.reload)
        self.ileri.clicked.connect(self.forward)
        self.anasayfa.clicked.connect(self.home)
        self.ara.clicked.connect(self.search)
        self.sekmeolustur.clicked.connect(self.yenisekme)

        self.retranslateUi(Form)
        self.YeniSekme.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Çakma Chrome Browser"))
        self.geri.setText(_translate("Form", "Geri"))
        self.ileri.setText(_translate("Form", "İleri"))
        self.yenile.setText(_translate("Form", "Yenile"))
        self.ara.setText(_translate("Form", "Ara"))
        self.anasayfa.setText(_translate("Form", "AnaSayfa"))
        self.sekmeolustur.setText(_translate("Form", "Yeni Sekme"))
        self.ayarlar.setText(_translate("Form", "Ayarlar"))
        self.YeniSekme.setTabText(self.YeniSekme.indexOf(self.tab_3), _translate("Form", "Ana Sekme"))

    def yenisekme(self):


        self.say += 1
        self.tab = 3
        self.tab = self.tab + self.say
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab_{}".format(self.tab))
        self.YeniSekme.addTab(self.tab, "Yeni Sekme {}".format(self.say))
        self.webView = 2
        self.webView = self.webView + self.say
        self.webView = QtWebKitWidgets.QWebView(self.tab)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView_{}".format(self.webView))


    def search(self):
        #self.say += 1
        #self.webView = 0
        #self.webView = self.webView + self.say
        url = self.lineEdit.text()
        self.webView.load(QtCore.QUrl(url))

        from mechanize import Browser
        br = Browser()
        br.open(url)
        self.YeniSekme.addTab(self.tab, "{}".format(br.title()))


from PyQt5 import QtWebKitWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
