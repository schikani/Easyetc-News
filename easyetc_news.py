from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *
import random
from web_scraper import *


# Here we make a new class passing the base object class.
class Ui_easyetc(object):
    def setupUi(self, easyetc):
        easyetc.setObjectName("easyetc")
        easyetc.resize(1665, 813)
        self.mainWidget = QtWidgets.QWidget(easyetc)
        self.mainWidget.setGeometry(QtCore.QRect(10, 10, 1631, 771))
        self.mainWidget.setObjectName("mainWidget")

        self.webView = QWebEngineView(self.mainWidget)
        self.webView.setGeometry(QtCore.QRect(390, 10, 1231, 701))
        self.webView.setObjectName("webView")

        self.label_votes = QtWidgets.QLabel(self.mainWidget)
        self.label_votes.setGeometry(QtCore.QRect(1410, 730, 81, 31))

        self.display_votes = QtWidgets.QLCDNumber(self.mainWidget)
        self.display_votes.setGeometry(QtCore.QRect(1490, 720, 131, 41))
        self.display_votes.setObjectName("display_votes")

        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_votes.setFont(font)
        self.label_votes.setObjectName("label_votes")

        self.news1 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news1.setGeometry(QtCore.QRect(20, 20, 321, 51))
        self.news1.setObjectName("news1")

        self.link1 = QtWidgets.QPushButton(self.mainWidget)
        self.link1.setGeometry(QtCore.QRect(340, 20, 31, 51))
        self.link1.setObjectName("link1")

        self.news2 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news2.setGeometry(QtCore.QRect(20, 90, 321, 51))
        self.news2.setObjectName("news2")

        self.link2 = QtWidgets.QPushButton(self.mainWidget)
        self.link2.setGeometry(QtCore.QRect(340, 90, 31, 51))
        self.link2.setObjectName("link2")

        self.news3 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news3.setGeometry(QtCore.QRect(20, 160, 321, 51))
        self.news3.setObjectName("news3")

        self.link3 = QtWidgets.QPushButton(self.mainWidget)
        self.link3.setGeometry(QtCore.QRect(340, 160, 31, 51))
        self.link3.setObjectName("link3")

        self.news4 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news4.setGeometry(QtCore.QRect(20, 230, 321, 51))
        self.news4.setObjectName("news4")

        self.link4 = QtWidgets.QPushButton(self.mainWidget)
        self.link4.setGeometry(QtCore.QRect(340, 230, 31, 51))
        self.link4.setObjectName("link4")

        self.news5 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news5.setGeometry(QtCore.QRect(20, 300, 321, 51))
        self.news5.setObjectName("news5")

        self.link5 = QtWidgets.QPushButton(self.mainWidget)
        self.link5.setGeometry(QtCore.QRect(340, 300, 31, 51))
        self.link5.setObjectName("link5")

        self.news6 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news6.setGeometry(QtCore.QRect(20, 370, 321, 51))
        self.news6.setObjectName("news6")

        self.link6 = QtWidgets.QPushButton(self.mainWidget)
        self.link6.setGeometry(QtCore.QRect(340, 370, 31, 51))
        self.link6.setObjectName("link6")

        self.news7 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news7.setGeometry(QtCore.QRect(20, 440, 321, 51))
        self.news7.setObjectName("news7")

        self.link7 = QtWidgets.QPushButton(self.mainWidget)
        self.link7.setGeometry(QtCore.QRect(340, 440, 31, 51))
        self.link7.setObjectName("link7")

        self.news8 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news8.setGeometry(QtCore.QRect(20, 510, 321, 51))
        self.news8.setObjectName("news8")

        self.link8 = QtWidgets.QPushButton(self.mainWidget)
        self.link8.setGeometry(QtCore.QRect(340, 510, 31, 51))
        self.link8.setObjectName("link8")

        self.news9 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news9.setGeometry(QtCore.QRect(20, 580, 321, 51))
        self.news9.setObjectName("news9")

        self.link9 = QtWidgets.QPushButton(self.mainWidget)
        self.link9.setGeometry(QtCore.QRect(340, 580, 31, 51))
        self.link9.setObjectName("link9")

        self.news10 = QtWidgets.QTextBrowser(self.mainWidget)
        self.news10.setGeometry(QtCore.QRect(20, 650, 321, 51))
        self.news10.setObjectName("news10")

        self.link10 = QtWidgets.QPushButton(self.mainWidget)
        self.link10.setGeometry(QtCore.QRect(340, 650, 31, 51))
        self.link10.setObjectName("link10")

        self.btn_1to10 = QtWidgets.QPushButton(self.mainWidget)
        self.btn_1to10.setGeometry(QtCore.QRect(20, 720, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_1to10.setFont(font)
        self.btn_1to10.setObjectName("btn_1to10")

        self.btn_11to20 = QtWidgets.QPushButton(self.mainWidget)
        self.btn_11to20.setGeometry(QtCore.QRect(100, 720, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_11to20.setFont(font)
        self.btn_11to20.setObjectName("btn_11to20")

        self.btn_21to30 = QtWidgets.QPushButton(self.mainWidget)
        self.btn_21to30.setGeometry(QtCore.QRect(190, 720, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_21to30.setFont(font)
        self.btn_21to30.setObjectName("btn_21to30")

        self.btn_Randomize = QtWidgets.QPushButton(self.mainWidget)
        self.btn_Randomize.setGeometry(QtCore.QRect(280, 720, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Randomize.setFont(font)
        self.btn_Randomize.setObjectName("btn_Randomize")

        self.current_page = QtWidgets.QLabel(self.mainWidget)
        self.current_page.setGeometry(QtCore.QRect(140, -4, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.current_page.setFont(font)
        self.current_page.setAlignment(QtCore.Qt.AlignCenter)
        self.current_page.setObjectName("current_page")

        self.url_address = QtWidgets.QTextBrowser(self.mainWidget)
        self.url_address.setGeometry(QtCore.QRect(390, 730, 1000, 31))
        self.url_address.setObjectName("url_address")
        self.url_address.setOpenExternalLinks(True)

        self.button_1to10()
        self.clicked()

    def retranslateUi(self, easyetc, url=None, title=None, votes=None, current_page=None):
        _translate = QtCore.QCoreApplication.translate
        easyetc.setWindowTitle(_translate("easyetc", "Easyetc News"))
        easyetc.setWindowIcon(QIcon("hn.png"))
        self.label_votes.setText(_translate("easyetc", "VOTES"))
        self.current_page.setText(_translate("easyetc", current_page))
        self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[0]}>{url[0]}</a></p>"))

        self.news1.setHtml(_translate("easyetc", f"<p>{title[0]}</p>"))
        self.link1.setText(_translate("easyetc", ">>>"))
        self.link1.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[0])))
        self.link1.clicked.connect(lambda: self.display_votes.display(votes[0]))
        self.link1.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[0]}>{url[0]}</a></p>")))

        self.news2.setHtml(_translate("easyetc", f"<p>{title[1]}</p>"))
        self.link2.setText(_translate("easyetc", ">>>"))
        self.link2.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[1])))
        self.link2.clicked.connect(lambda: self.display_votes.display(votes[1]))
        self.link2.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[1]}>{url[1]}</a></p>")))

        self.news3.setHtml(_translate("easyetc", f"<p>{title[2]}</p>"))
        self.link3.setText(_translate("easyetc", ">>>"))
        self.link3.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[2])))
        self.link3.clicked.connect(lambda: self.display_votes.display(votes[2]))
        self.link3.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[2]}>{url[2]}</a></p>")))

        self.news4.setHtml(_translate("easyetc", f"<p>{title[3]}</p>"))
        self.link4.setText(_translate("easyetc", ">>>"))
        self.link4.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[3])))
        self.link4.clicked.connect(lambda: self.display_votes.display(votes[3]))
        self.link4.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[3]}>{url[3]}</a></p>")))

        self.news5.setHtml(_translate("easyetc", f"<p>{title[4]}</p>"))
        self.link5.setText(_translate("easyetc", ">>>"))
        self.link5.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[4])))
        self.link5.clicked.connect(lambda: self.display_votes.display(votes[4]))
        self.link5.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[4]}>{url[4]}</a></p>")))

        self.news6.setHtml(_translate("easyetc", f"<p>{title[5]}</p>"))
        self.link6.setText(_translate("easyetc", ">>>"))
        self.link6.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[5])))
        self.link6.clicked.connect(lambda: self.display_votes.display(votes[5]))
        self.link6.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[5]}>{url[5]}</a></p>")))

        self.news7.setHtml(_translate("easyetc", f"<p>{title[6]}</p>"))
        self.link7.setText(_translate("easyetc", ">>>"))
        self.link7.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[6])))
        self.link7.clicked.connect(lambda: self.display_votes.display(votes[6]))
        self.link7.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[6]}>{url[6]}</a></p>")))

        self.news8.setHtml(_translate("easyetc", f"<p>{title[7]}</p>"))
        self.link8.setText(_translate("easyetc", ">>>"))
        self.link8.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[7])))
        self.link8.clicked.connect(lambda: self.display_votes.display(votes[7]))
        self.link8.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[7]}>{url[7]}</a></p>")))

        self.news9.setHtml(_translate("easyetc", f"<p>{title[8]}</p>"))
        self.link9.setText(_translate("easyetc", ">>>"))
        self.link9.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[8])))
        self.link9.clicked.connect(lambda: self.display_votes.display(votes[8]))
        self.link9.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[8]}>{url[8]}</a></p>")))

        self.news10.setHtml(_translate("easyetc", f"<p>{title[9]}</p>"))
        self.link10.setText(_translate("easyetc", ">>>"))
        self.link10.clicked.connect(lambda: self.webView.setUrl(QtCore.QUrl(url[9])))
        self.link10.clicked.connect(lambda: self.display_votes.display(votes[9]))
        self.link10.clicked.connect(
            lambda: self.url_address.setHtml(_translate("easyetc", f"<p><a href={url[9]}>{url[9]}</a></p>")))

    # This function is for first 10 news
    def button_1to10(self):
        url = []
        title = []
        votes = []
        for item in d1to10:
            url.append(item['link'])
            title.append(item['title'])
            votes.append(item['votes'])

        self.display_votes.display(votes[0])
        self.webView.setUrl(QtCore.QUrl(url[0]))
        self.retranslateUi(easyetc, url=url, title=title, votes=votes, current_page="1-10")
        QtCore.QMetaObject.connectSlotsByName(easyetc)

    # This function is for news from 11-20
    def button_11to20(self):
        url = []
        title = []
        votes = []
        for item in d11to20:
            url.append(item['link'])
            title.append(item['title'])
            votes.append(item['votes'])

        self.display_votes.display(votes[0])
        self.webView.setUrl(QtCore.QUrl(url[0]))
        self.retranslateUi(easyetc, url=url, title=title, votes=votes, current_page="11-20")
        QtCore.QMetaObject.connectSlotsByName(easyetc)

    # This function is for news from 21-30
    def button_21to30(self):
        url = []
        title = []
        votes = []
        for item in d21to30:
            url.append(item['link'])
            title.append(item['title'])
            votes.append(item['votes'])

        self.display_votes.display(votes[0])
        self.webView.setUrl(QtCore.QUrl(url[0]))
        self.retranslateUi(easyetc, url=url, title=title, votes=votes, current_page="21-30")
        QtCore.QMetaObject.connectSlotsByName(easyetc)

    # This function is for randomly generating a news from dictionaries
    def button_randomize(self):
        dlist = d1to10 + d11to20 + d21to30
        rchoice = random.choices(dlist, k=10)

        url = []
        title = []
        votes = []
        for item in rchoice:
            url.append(item['link'])
            title.append(item['title'])
            votes.append(item['votes'])

        self.display_votes.display(votes[0])
        self.webView.setUrl(QtCore.QUrl(url[0]))

        self.retranslateUi(easyetc, url=url, title=title, votes=votes, current_page="Randomize")
        QtCore.QMetaObject.connectSlotsByName(easyetc)

    # This function is defined to sense the click of buttons and take necessary actions
    def clicked(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_1to10.setText(_translate("easyetc", "1-10"))
        self.btn_1to10.clicked.connect(lambda: self.button_1to10())

        self.btn_11to20.setText(_translate("easyetc", "11-20"))
        self.btn_11to20.clicked.connect(lambda: self.button_11to20())

        self.btn_21to30.setText(_translate("easyetc", "21-30"))
        self.btn_21to30.clicked.connect(lambda: self.button_21to30())

        self.btn_Randomize.setText(_translate("easyetc", "Randomize"))
        self.btn_Randomize.clicked.connect(lambda: self.button_randomize())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    easyetc = QtWidgets.QWidget()
    ui = Ui_easyetc()
    ui.setupUi(easyetc)
    easyetc.show()
    sys.exit(app.exec_())
