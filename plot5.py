## Ex 5-12. QPixmap.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QPushButton,QMessageBox,QCheckBox,QDialog,QTableWidgetItem, QTableWidget, QAbstractItemView
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtGui



#pdf 파일 열기
import webbrowser as wb
#현재 디렉토리 경로 얻기
import os

global gg
gg = None



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #pixmap = QPixmap("C:/Users/wanseok/Desktop/plot2/plot2.jpg")
        #pixmap4 = pixmap.scaled(pixmap.width() * 0.29, pixmap.height() * 0.29)
        self.setWindowTitle('Hyundai Chemical HPC Project Off Site Tank DWG')
        self.setWindowIcon(QIcon('IMG\\hdo.ico'))

        self.setGeometry(0,0,1200,1000)
        #self.showMaximized()
        self.pixmap = QPixmap("IMG\\plot.png")
        self.pixmap4 = self.pixmap.scaled(int(self.pixmap.width() * 1.05), int(self.pixmap.height() * 1.05))

        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap4)
        #self.lbl_size = QLabel('Width: '+str(self.pixmap.width())+', Height: '+str(self.pixmap.height()))
        self.lbl_size = QLabel('Hyundai Chemical HPC Project ')
        self.lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_img)
        vbox.addWidget(self.lbl_size)
        self.setLayout(vbox)

        #self.setWindowTitle('QPixmap')
        self.move(0, 0)

        self.cb = QCheckBox('21년 9월 사진', self)
        self.cb.move(30,880)
        self.cb.resize(190,20)
        self.cb.isChecked()
        self.cb.stateChanged.connect(self.changeTitle)

        self.cb2 = QCheckBox('Detail DWG Show', self)
        self.cb2.move(30,910)
        self.cb2.isChecked()


#        self.btn1 = QPushButton('Photo', self)
#        self.btn1.move(260, 200)
#        self.btn1.resize(110, 30)
#        self.btn1.clicked.connect(self.btn_clicked_1)

#        self.btn2 = QPushButton('DWG', self)
#        self.btn2.move(450, 200)
#        self.btn2.resize(110, 30)
#        self.btn2.clicked.connect(self.btn_clicked_2)


        n11= 'MP-M53-023~025'
        self.btn11 = QPushButton('MP-M53-024', self)
        self.btn11.move(1520, 190)
        self.btn11.resize(100, 25)
        self.btn11.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn11.setToolTip('MP-M53-024')
        self.btn11.clicked.connect(
            lambda state, button=self.btn11: self.btn_clicked_3(state, button, n11))
        self.btn11.setToolTip('1-3 Butadiene Tank\nID: 18.5(t23.5)\nWeight: 310Ton')


        n12 = 'MP-M53-023~025'
        self.btn12 = QPushButton('MP-M53-023', self)
        self.btn12.move(1580, 140)
        self.btn12.resize(100, 25)
        self.btn12.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn12.clicked.connect(
            lambda state, button=self.btn12: self.btn_clicked_3(state, button, n12))
        self.btn12.setToolTip('1-3 Butadiene Tank\nID: 18.5(t23.5)\nWeight: 310Ton')


        n13 = 'MP-M53-023~025'
        self.btn13 = QPushButton('MP-M53-025', self)
        self.btn13.move(1650, 175)
        self.btn13.resize(100, 25)
        self.btn13.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn13.clicked.connect(
            lambda state, button=self.btn13: self.btn_clicked_3(state, button, n13))
        self.btn13.setToolTip('1-3 Butadiene Tank\nID: 18.5(t23.5)\nWeight: 310Ton')

        n14 = 'MP-M53-021,022'
        self.btn14 = QPushButton('MP-M53-021', self)
        self.btn14.move(1750, 180)
        self.btn14.resize(100, 25)
        self.btn14.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn14.clicked.connect(
            lambda state, button=self.btn14: self.btn_clicked_3(state, button, n14))
        self.btn14.setToolTip('Mixed C4 Tank\nID: 23(t27.5)\nWeight: 574Ton')


        n15 = 'MP-M53-026,027'
        self.btn15 = QPushButton('MP-M53-026', self)
        self.btn15.move(1520, 280)
        self.btn15.resize(100, 25)
        self.btn15.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn15.clicked.connect(
            lambda state, button=self.btn15: self.btn_clicked_3(state, button, n15))
        self.btn15.setToolTip('Raffinate-1 Tank\nID: 23(t27.5)\nWeight: 574Ton')


        n16 = 'MP-M53-026,027'
        self.btn16 = QPushButton('MP-M53-027', self)
        self.btn16.move(1630, 280)
        self.btn16.resize(100, 25)
        self.btn16.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn16.clicked.connect(
            lambda state, button=self.btn16: self.btn_clicked_3(state, button, n16))
        self.btn16.setToolTip('Raffinate-1 Tank\nID: 23(t27.5)\nWeight: 574Ton')


        n17 = 'MP-M53-021,022'
        self.btn17 = QPushButton('MP-M53-022', self)
        self.btn17.move(1740, 280)
        self.btn17.resize(100, 25)
        self.btn17.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn17.clicked.connect(
            lambda state, button=self.btn17: self.btn_clicked_3(state, button, n17))
        self.btn17.setToolTip('Mixed C4 Tank\nID: 23(t27.5)\nWeight: 574Ton')

        n18 = 'MP-M52-001,002'
        self.btn18 = QPushButton('MP-M52-001', self)
        self.btn18.move(1520, 380)
        self.btn18.resize(100, 25)
        self.btn18.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn18.clicked.connect(
            lambda state, button=self.btn18: self.btn_clicked_3(state, button, n18))
        self.btn18.setToolTip('Propane Tank\nID: 23(t45)\nWeight: 785Ton')

        n19 = 'MP-M52-001,002'
        self.btn19 = QPushButton('MP-M52-002', self)
        self.btn19.move(1630, 380)
        self.btn19.resize(100, 25)
        self.btn19.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn19.clicked.connect(
            lambda state, button=self.btn19: self.btn_clicked_3(state, button, n19))
        self.btn19.setToolTip('Propane Tank\nID: 23(t45)\nWeight: 785Ton')


        n20 = 'MP-M53-028'
        self.btn20 = QPushButton('MP-M53-028', self)
        self.btn20.move(1740, 380)
        self.btn20.resize(100, 25)
        self.btn20.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn20.clicked.connect(
            lambda state, button=self.btn20: self.btn_clicked_3(state, button, n20))
        self.btn20.setToolTip('1-Butene Tank\nID: 18.5(t23.5)\nWeight: 310Ton')


        n21 = 'MP-M53-011,012'
        self.btn21 = QPushButton('MP-M53-011', self)
        self.btn21.move(1520, 475)
        self.btn21.resize(100, 25)
        self.btn21.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn21.clicked.connect(
            lambda state, button=self.btn21: self.btn_clicked_3(state, button, n21))
        self.btn21.setToolTip('Propylene Tank\nID: 23(t48)\nWeight: 837Ton')


        n22 = 'MP-M53-011,012'
        self.btn22 = QPushButton('MP-M53-012', self)
        self.btn22.move(1630, 475)
        self.btn22.resize(100, 25)
        self.btn22.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn22.clicked.connect(
            lambda state, button=self.btn22: self.btn_clicked_3(state, button, n22))


        n23 = 'MP-M53-013'
        self.btn23 = QPushButton('MP-M53-013', self)
        self.btn23.move(1740, 475)
        self.btn23.resize(100, 25)
        self.btn23.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn23.clicked.connect(
            lambda state, button=self.btn19: self.btn_clicked_3(state, button, n23))


        n24 = 'MF-M53-004'
        self.btn24 = QPushButton('MF-M53-004', self)
        self.btn24.move(1650, 650)
        self.btn24.resize(100, 25)
        self.btn24.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn24.clicked.connect(
            lambda state, button=self.btn24: self.btn_clicked_3(state, button, n24))

        n25 = 'MP-M53-001'
        self.btn25 = QPushButton('MP-M53-001', self)
        self.btn25.move(1580, 770)
        self.btn25.resize(100, 25)
        self.btn25.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn25.clicked.connect(
            lambda state, button=self.btn25: self.btn_clicked_3(state, button, n25))

        n26 = 'MP-M53-002,003'
        self.btn26 = QPushButton('MP-M53-002', self)
        self.btn26.move(1680, 780)
        self.btn26.resize(100, 25)
        self.btn26.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn26.clicked.connect(
            lambda state, button=self.btn26: self.btn_clicked_3(state, button, n26))

        n27 = 'MP-M53-002,003'
        self.btn27 = QPushButton('MP-M53-003', self)
        self.btn27.move(1780, 780)
        self.btn27.resize(100, 25)
        self.btn27.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn27.clicked.connect(
            lambda state, button=self.btn27: self.btn_clicked_3(state, button, n27))


        n28 = 'MF-M52-081,082'
        self.btn28 = QPushButton('MF-M52-082', self)
        self.btn28.move(1370, 275)
        self.btn28.resize(100, 25)
        self.btn28.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn28.setToolTip('T-DAO TANK \nID: 41.1 \nHeight: 24 \nWeight: 857Ton \nCapacity: 31798m3')
        self.btn28.clicked.connect(
            lambda state, button=self.btn28: self.btn_clicked_3(state, button, n28))

        n29 = 'MF-M52-083'
        self.btn29 = QPushButton('MF-M52-083', self)
        self.btn29.move(1175, 275)
        self.btn29.resize(100, 25)
        self.btn29.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn29.setToolTip('Light T-DAO TANK \nID: 41.1 \nHeight: 24 \nWeight: 857Ton \nCapacity: 31798m3')
        self.btn29.clicked.connect(
            lambda state, button=self.btn29: self.btn_clicked_3(state, button, n29))

        n30 = 'MF-M52-081,082'
        self.btn30 = QPushButton('MP-M52-081', self)
        self.btn30.move(1370, 425)
        self.btn30.resize(100, 25)
        self.btn30.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn30.setToolTip('T-DAO TANK \nID: 41.1 \nHeight: 24 \nWeight: 857Ton \nCapacity: 31798m3')
        self.btn30.clicked.connect(
            lambda state, button=self.btn30: self.btn_clicked_3(state, button, n30))

        n31 = 'MF-M60-001'
        self.btn31 = QPushButton('MF-M60-001', self)
        self.btn31.move(1250, 380)
        self.btn31.resize(100, 25)
        self.btn31.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn31.setToolTip('Slop Oil TANK \nID: 17 \nHeight: 21 \nWeight: 181Ton \nCapacity: 4770m3')
        self.btn31.clicked.connect(
            lambda state, button=self.btn31: self.btn_clicked_3(state, button, n31))

        n32 = 'MF-M53-081,082'
        self.btn32 = QPushButton('MP-M53-082', self)
        self.btn32.move(1210, 470)
        self.btn32.resize(100, 25)
        self.btn32.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn32.setToolTip('Slop Oil TANK \nID: 22.5 \nHeight: 24 \nWeight: 365Ton \nCapacity: 9539m3')
        self.btn32.clicked.connect(
            lambda state, button=self.btn32: self.btn_clicked_3(state, button, n32))

        n33 = 'MF-M53-081,082'
        self.btn33 = QPushButton('MF-M53-081', self)
        self.btn33.move(1280, 531)
        self.btn33.resize(100, 25)
        self.btn33.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn33.setToolTip('PFO TANK \nID: 22.5 \nHeight: 24 \nWeight: 365Ton \nCapacity: 9539m3')
        self.btn33.clicked.connect(
            lambda state, button=self.btn33: self.btn_clicked_3(state, button, n33))

        n34 = 'MF-M52-051'
        self.btn34 = QPushButton('MF-M52-051', self)
        self.btn34.move(1410, 542)
        self.btn34.resize(100, 25)
        self.btn34.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn34.setToolTip('DFU Gas Oil TANK \nID: 17 \nHeight: 21 \nWeight: 159Ton \nCapacity: 4770m3')
        self.btn34.clicked.connect(
            lambda state, button=self.btn34: self.btn_clicked_3(state, button, n34))

        n35 = 'MP-M53-031,032'
        self.btn35 = QPushButton('MP-M53-032', self)
        self.btn35.move(990, 281)
        self.btn35.resize(100, 25)
        self.btn35.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn35.clicked.connect(
            lambda state, button=self.btn33: self.btn_clicked_3(state, button, n35))

        n36 = 'MP-M53-031,032'
        self.btn36 = QPushButton('MP-M53-031', self)
        self.btn36.move(870, 311)
        self.btn36.resize(100, 25)
        self.btn36.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn36.clicked.connect(
            lambda state, button=self.btn36: self.btn_clicked_3(state, button, n36))

        n37 = 'MF-M53-038'
        self.btn37 = QPushButton('MF-M53-038', self)
        self.btn37.move(980, 441)
        self.btn37.resize(100, 25)
        self.btn37.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn37.setToolTip('TPG TANK \nID: 31.8 \nHeight: 24 \nWeight: 541Ton \nCapacity: 19079m3')
        self.btn37.clicked.connect(
            lambda state, button=self.btn37: self.btn_clicked_3(state, button, n37))

        n38 = 'MF-M53-061'
        self.btn38 = QPushButton('MF-M53-061', self)
        self.btn38.move(865, 451)
        self.btn38.resize(100, 25)
        self.btn38.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn38.setToolTip('C9+ TANK \nID: 17 \nHeight: 21 \nWeight: 159Ton \nCapacity: 4770m3')
        self.btn38.clicked.connect(
            lambda state, button=self.btn38: self.btn_clicked_3(state, button, n38))

        n39 = 'MF-M53-037'
        self.btn39 = QPushButton('MF-M53-037', self)
        self.btn39.move(980, 568)
        self.btn39.resize(100, 25)
        self.btn39.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn39.setToolTip('RPG TANK \nID: 31.8 \nHeight: 24 \nWeight: 541Ton \nCapacity: 19079m3')
        self.btn39.clicked.connect(
            lambda state, button=self.btn39: self.btn_clicked_3(state, button, n39))


        n40 = 'MF-M53-036'
        self.btn40 = QPushButton('MF-M53-036', self)
        self.btn40.move(970, 715)
        self.btn40.resize(100, 25)
        self.btn40.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn40.setToolTip('RPG TANK \nID: 41.1 \nHeight: 24 \nWeight: 775Ton \nCapacity: 31798m3')
        self.btn40.clicked.connect(
            lambda state, button=self.btn40: self.btn_clicked_3(state, button, n40))

        n41 = 'MF-M52-021,022'
        self.btn41 = QPushButton('MF-M52-021', self)
        self.btn41.move(785, 715)
        self.btn41.resize(100, 25)
        self.btn41.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn41.setToolTip('Petro Naptha TANK \nID: 41.1 \nHeight: 24 \nWeight: 775Ton \nCapacity: 31798m3')
        self.btn41.clicked.connect(
            lambda state, button=self.btn41: self.btn_clicked_3(state, button, n41))

        n42 = 'MF-M53-005'
        self.btn42 = QPushButton('MF-M53-005', self)
        self.btn42.move(865, 620)
        self.btn42.resize(100, 25)
        self.btn42.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn42.setToolTip('Vynil Acetate TANK \nID: 22.5 \nHeight: 24 \nWeight: 299Ton \nCapacity: 9539m3')
        self.btn42.clicked.connect(
            lambda state, button=self.btn33: self.btn_clicked_3(state, button, n42))

        n43 = 'MF-M52-021,022'
        self.btn43 = QPushButton('MF-M52-022', self)
        self.btn43.move(785, 532)
        self.btn43.resize(100, 25)
        self.btn43.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn43.setToolTip('Petro Naptha TANK \nID: 41.1 \nHeight: 24 \nWeight: 775Ton \nCapacity: 31798m3')
        self.btn43.clicked.connect(
            lambda state, button=self.btn43: self.btn_clicked_3(state, button, n43))

        n44 = 'MF-M75-001'
        self.btn44 = QPushButton('MF-M75-001', self)
        self.btn44.move(560, 770)
        self.btn44.resize(100, 25)
        self.btn44.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn44.setToolTip('Fire Water TANK \nID: 31 \nHeight: 25.7 \nWeight: 460.6Ton \nCapacity: 19398m3')
        self.btn44.clicked.connect(
            lambda state, button=self.btn44: self.btn_clicked_3(state, button, n44))

        n45 = 'MF-M32-003'
        self.btn45 = QPushButton('MF-M32-003', self)
        self.btn45.move(400, 590)
        self.btn45.resize(100, 25)
        self.btn45.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn45.setToolTip('Polished Water TANK \nID: 19.8 \nHeight: 21 \nWeight: 167.2Ton \nCapacity: 6466m3')
        self.btn45.clicked.connect(
            lambda state, button=self.btn45: self.btn_clicked_3(state, button, n45))

        n46 = 'MF-M32-001'
        self.btn46 = QPushButton('MF-M32-001', self)
        self.btn46.move(400, 510)
        self.btn46.resize(100, 25)
        self.btn46.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn46.setToolTip('Desalinated Polished Water TANK \nID: 25.7 \nHeight: 24 \nWeight: 326.1Ton \nCapacity: 14255m3')
        self.btn46.clicked.connect(
            lambda state, button=self.btn46: self.btn_clicked_3(state, button, n46))

        n47 = 'MF-M32-005'
        self.btn47 = QPushButton('MF-M32-005', self)
        self.btn47.move(500, 470)
        self.btn47.resize(100, 25)
        self.btn47.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn47.setToolTip('Portable Water TANK \nID: 6.5 \nHeight: 9 \nWeight: 22.7Ton \nCapacity: 299m3')
        self.btn47.clicked.connect(
            lambda state, button=self.btn47: self.btn_clicked_3(state, button, n47))

        n47_1 = 'MF-M32-002'
        self.btn47_1 = QPushButton('MF-M32-002', self)
        self.btn47_1.move(500, 420)
        self.btn47_1.resize(100, 25)
        self.btn47_1.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn47_1.setToolTip('Utility Water TANK \nID: 14.5 \nHeight: 12 \nWeight: 67.7Ton \nCapacity: 1982m3')
        self.btn47_1.clicked.connect(
            lambda state, button=self.btn47_1: self.btn_clicked_3(state, button, n47_1))

        n48 = 'MF-M32-051AS'
        self.btn48 = QPushButton('MF-M32-051S', self)
        self.btn48.move(530, 370)
        self.btn48.resize(110, 25)
        self.btn48.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn48.setToolTip('20wt Caustic Storage TANK \nID: 10 \nHeight: 12 \nWeight: 44.1Ton \nCapacity: 942m3')
        self.btn48.clicked.connect(
            lambda state, button=self.btn48: self.btn_clicked_3(state, button, n48))


        n49 = 'MF-M32-051AS'
        self.btn49 = QPushButton('MF-M32-051A', self)
        self.btn49.move(370, 370)
        self.btn49.resize(110, 25)
        self.btn49.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn49.setToolTip('20wt Caustic Storage TANK \nID: 10 \nHeight: 12 \nWeight: 44.1Ton \nCapacity: 942m3')
        self.btn49.clicked.connect(
            lambda state, button=self.btn49: self.btn_clicked_3(state, button, n49))

        n50 = 'MF-M40-001AS'
        self.btn50 = QPushButton('M40-001S', self)
        self.btn50.move(170, 610)
        self.btn50.resize(80, 20)
        self.btn50.setFont(QtGui.QFont("맑은고딕", 9))
        self.btn50.setToolTip('Contaminated Storm Water TANK \nID: 18 \nHeight: 21 \nWeight: 107.8Ton \nCapacity: 4222m3')
        self.btn50.clicked.connect(
            lambda state, button=self.btn50: self.btn_clicked_3(state, button, n50))

        n51 = 'MF-M40-001AS'
        self.btn51 = QPushButton('M40-001A', self)
        self.btn51.move(170, 680)
        self.btn51.resize(80, 20)
        self.btn51.setFont(QtGui.QFont("맑은고딕",9))
        self.btn51.setToolTip(
            'Contaminated Storm Water TANK \nID: 18 \nHeight: 21 \nWeight: 107.8Ton \nCapacity: 4222m3')
        self.btn51.clicked.connect(
            lambda state, button=self.btn51: self.btn_clicked_3(state, button, n51))


        n52 = 'MF-M40-002AS'
        self.btn52 = QPushButton('M40-002A', self)
        self.btn52.move(105, 630)
        self.btn52.resize(80,20)
        self.btn52.setFont(QtGui.QFont("맑은고딕",9))
        self.btn52.setToolTip(
            'Water Waste Collection TANK \nID: 19.5 \nHeight: 27 \nWeight: 217.5Ton \nCapacity: 8063m3')
        self.btn52.clicked.connect(
            lambda state, button=self.btn52: self.btn_clicked_3(state, button, n52))

        n53 = 'MF-M40-002AS'
        self.btn53 = QPushButton('M40-002S', self)
        self.btn53.move(105, 700)
        self.btn53.resize(80, 20)
        self.btn53.setFont(QtGui.QFont("맑은고딕",9))
        self.btn53.setToolTip(
            'Water Waste Collection TANK \nID: 19.5 \nHeight: 27 \nWeight: 217.5Ton \nCapacity: 8063m3')
        self.btn53.clicked.connect(
            lambda state, button=self.btn53: self.btn_clicked_3(state, button, n53))

        n54 = 'MF-M40-003AS'
        self.btn54 = QPushButton('M40-003A', self)
        self.btn54.move(45, 610)
        self.btn54.resize(80,20)
        self.btn54.setFont(QtGui.QFont("맑은고딕",9))
        self.btn54.setToolTip(
            'Abnormal Waste Water TANK \nID: 19.5 \nHeight: 27 \nWeight: 217.5Ton \nCapacity: 8063m3')
        self.btn54.clicked.connect(
            lambda state, button=self.btn54: self.btn_clicked_3(state, button, n54))

        n55 = 'MF-M40-003AS'
        self.btn55 = QPushButton('M40-003B', self)
        self.btn55.move(45, 680)
        self.btn55.resize(80, 20)
        self.btn55.setFont(QtGui.QFont("맑은고딕",9))
        self.btn55.setToolTip(
            'Abnormal Waste Water TANK \nID: 19.5 \nHeight: 27 \nWeight: 217.5Ton \nCapacity: 8063m3')
        self.btn55.clicked.connect(
            lambda state, button=self.btn55: self.btn_clicked_3(state, button, n55))

        n56 = 'MT-M22-7003'
        self.btn56 = QPushButton(n56, self)
        self.btn56.move(20, 80)
        self.btn56.resize(105, 20)
        self.btn56.setFont(QtGui.QFont("맑은고딕",9))
        self.btn56.setToolTip(
            'Waste Hexane TANK \nID: 7.62 \nHeight: 7.3 \nWeight: 26Ton \nCapacity: 333m3')
        self.btn56.clicked.connect(
            lambda state, button=self.btn56: self.btn_clicked_3(state, button, n56))

        n57 = 'MT-M22-7004'
        self.btn57 = QPushButton(n57, self)
        self.btn57.move(125, 80)
        self.btn57.resize(105, 20)
        self.btn57.setFont(QtGui.QFont("맑은고딕",9))
        self.btn57.setToolTip(
            '1-Hexane TANK \nID: 10.1 \nHeight: 12.45 \nWeight: 56Ton \nCapacity: 997m3')
        self.btn57.clicked.connect(
            lambda state, button=self.btn57: self.btn_clicked_3(state, button, n57))

        n58 = 'MT-M22-7002'
        self.btn58 = QPushButton(n58, self)
        self.btn58.move(20, 140)
        self.btn58.resize(105, 20)
        self.btn58.setFont(QtGui.QFont("맑은고딕",9))
        self.btn58.setToolTip(
            'Pure Hexane TANK \nID: 10.1 \nHeight: 12.45 \nWeight: 53Ton \nCapacity: 997m3')
        self.btn58.clicked.connect(
            lambda state, button=self.btn58: self.btn_clicked_3(state, button, n58))

        n59 = 'MT-M22-7001'
        self.btn59 = QPushButton(n59, self)
        self.btn59.move(125, 140)
        self.btn59.resize(105, 20)
        self.btn59.setFont(QtGui.QFont("맑은고딕",9))
        self.btn59.setToolTip(
            'Crude Hexane TANK \nID: 9.8 \nHeight: 12.18 \nWeight: 52Ton \nCapacity: 919m3')
        self.btn59.clicked.connect(
            lambda state, button=self.btn59: self.btn_clicked_3(state, button, n59))

        n60 = 'MT-M14-501'
        self.btn60 = QPushButton(n60, self)
        self.btn60.move(220, 115)
        self.btn60.resize(100, 20)
        self.btn60.setFont(QtGui.QFont("맑은고딕",9))
        self.btn60.setToolTip(
            'Solvent Surge TANK \nID: 8 \nHeight: 10.73 \nWeight: 34.8Ton \nCapacity: 539m3')
        self.btn60.clicked.connect(
            lambda state, button=self.btn60: self.btn_clicked_3(state, button, n60))

        n61 = 'MT-M10-201'
        self.btn61 = QPushButton(n61, self)
        self.btn61.move(320, 115)
        self.btn61.resize(100, 20)
        self.btn61.setFont(QtGui.QFont("맑은고딕",9))
        self.btn61.setToolTip(
            'Flux Oil TANK \nID: 8.5 \nHeight: 8.5 \nWeight: 33Ton \nCapacity: 482m3')
        self.btn61.clicked.connect(
            lambda state, button=self.btn61: self.btn_clicked_3(state, button, n61))

        n62 = 'MT-M10-301'
        self.btn62 = QPushButton(n62, self)
        self.btn62.move(425, 115)
        self.btn62.resize(100, 20)
        self.btn62.setFont(QtGui.QFont("맑은고딕",9))
        self.btn62.setToolTip(
            'Wash Oil Storage TANK \nID: 8.5 \nHeight: 8.5 \nWeight: 29Ton \nCapacity: 482m3')
        self.btn62.clicked.connect(
            lambda state, button=self.btn61: self.btn_clicked_3(state, button, n62))

        n63 = 'MT-M10-961'
        self.btn63 = QPushButton(n63, self)
        self.btn63.move(530, 80)
        self.btn63.resize(100, 20)
        self.btn63.setFont(QtGui.QFont("맑은고딕",9))
        self.btn63.setToolTip(
            'Spent Caustic TANK \nID: 14.65 \nHeight: 14 \nWeight: 92.4Ton \nCapacity: 2360m3')
        self.btn63.clicked.connect(
            lambda state, button=self.btn63: self.btn_clicked_3(state, button, n63))



#    def btn_clicked_1(self):

#        self.pixmap = QPixmap("plot6.jpg")
#        self.pixmap4 = self.pixmap.scaled(self.pixmap.width() * 0.308, self.pixmap.height() * 0.31)

        #self.lbl_img = QLabel()
#        self.lbl_img.setPixmap(self.pixmap4)
        #self.lbl_size = QLabel('Width: '+str(self.pixmap.width())+', Height: '+str(self.pixmap.height()))
        #self.lbl_size.setAlignment(Qt.AlignCenter)

        #vbox = QVBoxLayout()
        #vbox.addWidget(lbl_img)
        #vbox.addWidget(lbl_size)
        #self.setLayout(vbox)

#    def btn_clicked_2(self):
#        self.pixmap = QPixmap("plot.png")
#        self.pixmap4 = self.pixmap.scaled(self.pixmap.width() * 1.05, self.pixmap.height() * 1.05)

        #self.lbl_img = QLabel()
#        self.lbl_img.setPixmap(self.pixmap4)

# 도면을 Click했을 때 GA 도면 출력

    def btn_clicked_3(self, state, button, bb):

        find_dic_name = []
        presant_dir = os.getcwd()

        if self.cb2.isChecked() == False :
            print('ok')
            #체크를 안했을 경우 GA도면만 출력
            try:
                file_names = os.listdir(presant_dir + '\\' + 'DWG' + '\\' + bb)

                for file_name in file_names:
                    if ('001' in file_name):
                        find_dic_name.append(file_name)
                        # print(find_dic_name[0])

                wb.open_new(presant_dir + '\\' + 'DWG' + '\\' + bb + '\\' + find_dic_name[0])

            except:
                QMessageBox.about(self, 'Error Message', "지정 디렉토리에 도면이 있는지 확인하세요")

        else:
            print('not ok')
            # 체크를 할 경우 DETAIL 도면 dialog 출력
            print(bb)
            global gg
            gg = bb
            dlg = Picture_view_100()
            dlg.exec_()






    def changeTitle(self, state):
        if state == Qt.Checked:
            self.pixmap = QPixmap("IMG\\plot13.jpg")
            #self.pixmap4 = self.pixmap.scaled(self.pixmap.width() * 0.318, self.pixmap.height() * 0.31) 현대 제공 사진
            self.pixmap4 = self.pixmap.scaled(int(self.pixmap.width() * 0.31), int(self.pixmap.height() * 0.298))
            self.lbl_img.setPixmap(self.pixmap4)


        else:
            self.pixmap = QPixmap("IMG\\plot.png")
            self.pixmap4 = self.pixmap.scaled(int(self.pixmap.width() * 1.05), int(self.pixmap.height() * 1.05))
            self.lbl_img.setPixmap(self.pixmap4)


class Picture_view_100(QDialog):


    find_name_mat = []
    find_name_mat_link = []


    def __init__(self):
        super().__init__()
        self.setupUI()
        

    def setupUI(self):
        self.setWindowTitle('Tank Detail Drawing')

        self.setWindowIcon(QIcon('IMG\\hdo.ico'))
       # self.setWindowIcon(QIcon('Data\PKG2.png'))
        self.resize(1400, 600)
        self.move(300, 200)

        # self.cb = QComboBox(self)


        bb = gg

        print(bb)
        presant_dir = os.getcwd()
        file_names = sorted(os.listdir(presant_dir + '\\' + 'DWG' + '\\' + bb))

    #    find_name_mat = []
    #    find_name_mat_link = []

        del Picture_view_100.find_name_mat
        del Picture_view_100.find_name_mat_link

        Picture_view_100.find_name_mat = []
        Picture_view_100.find_name_mat_link =[]

#        pkg2_tank = ['MF-M52-021,022', 'MF-M52-051', 'MF-M52-081,082', 'MF-M52-083', 'MF-M53-005', 'MF-M53-036',
#                     'MF-M53-037', 'MF-M53-038', 'MF-M53-061', 'MF-M53-081,082', 'MF-M60-001', 'MT-M22-7001', 'MT-M22-7002', 'MT-M22-7003', 'MT-M22-7004']
#
#        if bb in pkg2_tank :
#            cc = bb.split('-')
#            dd = cc[2]
#            if dd not 700
#                ee = dd[0:2]
#            else
#                ee = dd[]
            

#        for file_name in file_names:
#            if (ee in file_name):
#                #print(file_name + '완석')
#                link = presant_dir + '\\' + 'DWG' + '\\' + bb + '\\' + file_name
#                #print(aaa)
#                #print(link)
#                Picture_view_100.find_name_mat_link.append(file_name)
#                Picture_view_100.find_name_mat.append(link)

        #aa = Picture_view_100.find_name_mat_link

        for file_name in file_names:

            link = presant_dir + '\\' + 'DWG' + '\\' + bb + '\\' + file_name
            Picture_view_100.find_name_mat_link.append(file_name)
            Picture_view_100.find_name_mat.append(link)

        ddd = len(Picture_view_100.find_name_mat_link)
        #print(ddd)

        self.tableWidget  = QTableWidget(self)

        self.tableWidget.resize(1200,600)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(ddd)

        column_headers = ['Drawing', '기타']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        #    self.setTableWidgetData()
        # test 내부 수정 불가
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Table 내 열 조절하기
        header = self.tableWidget.horizontalHeader()
        header.resizeSection(0, 800)
        self.setTableWidgetData()


    def setTableWidgetData(self):
        for i in range(0, len(Picture_view_100.find_name_mat)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            #    print(len(find_name_mat_link))

            text_split = Picture_view_100.find_name_mat[i]
            text_split_name = text_split.split(os.path.sep)
            self.tableWidget.item(i, 0).setText(text_split_name[-1])

        self.tableWidget.cellDoubleClicked.connect(self.cellchanged_event)


    def cellchanged_event(self, row, col):
        data = self.tableWidget.item(row, col)
        print(data.text())
        bb = gg
        presant_dir = os.getcwd()
        print(presant_dir + '\\' + 'DWG' + '\\' + bb + '\\' + data.text())
        wb.open_new(presant_dir + '\\' + 'DWG' + '\\' + bb +'\\' + data.text())



    def btn_clicked_1(self, text):
        bb = gg
        presant_dir = os.getcwd()
        wb.open_new(presant_dir + '\\' + 'DWG' + '\\' + bb +'\\' + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
