# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Ui_MainWindow(QtWidgets.QMainWindow):
    selected_value = []
    value = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buang_air_besar = QtWidgets.QCheckBox(self.centralwidget)
        self.buang_air_besar.setGeometry(QtCore.QRect(30, 70, 441, 20))
        self.buang_air_besar.setObjectName("buang_air_besar")
        self.berak_encer = QtWidgets.QCheckBox(self.centralwidget)
        self.berak_encer.setGeometry(QtCore.QRect(30, 100, 261, 20))
        self.berak_encer.setObjectName("berak_encer")
        self.berak_berdarah = QtWidgets.QCheckBox(self.centralwidget)
        self.berak_berdarah.setGeometry(QtCore.QRect(30, 130, 271, 20))
        self.berak_berdarah.setObjectName("berak_berdarah")
        self.lesu = QtWidgets.QCheckBox(self.centralwidget)
        self.lesu.setGeometry(QtCore.QRect(30, 160, 331, 20))
        self.lesu.setObjectName("lesu")
        self.tidak_selera_makan = QtWidgets.QCheckBox(self.centralwidget)
        self.tidak_selera_makan.setGeometry(QtCore.QRect(30, 190, 231, 20))
        self.tidak_selera_makan.setObjectName("tidak_selera_makan")
        self.mual_muntah = QtWidgets.QCheckBox(self.centralwidget)
        self.mual_muntah.setGeometry(QtCore.QRect(30, 220, 431, 20))
        self.mual_muntah.setObjectName("mual_muntah")
        self.sakit_di_perut = QtWidgets.QCheckBox(self.centralwidget)
        self.sakit_di_perut.setGeometry(QtCore.QRect(30, 250, 281, 20))
        self.sakit_di_perut.setObjectName("sakit_di_perut")
        self.tekanan_darah_rendah = QtWidgets.QCheckBox(self.centralwidget)
        self.tekanan_darah_rendah.setGeometry(QtCore.QRect(30, 280, 251, 20))
        self.tekanan_darah_rendah.setObjectName("tekanan_darah_rendah")
        self.pusing = QtWidgets.QCheckBox(self.centralwidget)
        self.pusing.setGeometry(QtCore.QRect(30, 310, 201, 20))
        self.pusing.setObjectName("pusing")
        self.pingsan = QtWidgets.QCheckBox(self.centralwidget)
        self.pingsan.setGeometry(QtCore.QRect(30, 340, 231, 20))
        self.pingsan.setObjectName("pingsan")
        self.suhu_badan_tinggi = QtWidgets.QCheckBox(self.centralwidget)
        self.suhu_badan_tinggi.setGeometry(QtCore.QRect(30, 370, 221, 20))
        self.suhu_badan_tinggi.setObjectName("suhu_badan_tinggi")
        self.luka_badan = QtWidgets.QCheckBox(self.centralwidget)
        self.luka_badan.setGeometry(QtCore.QRect(30, 400, 311, 20))
        self.luka_badan.setObjectName("luka_badan")
        self.anggota_badan_tidak_bisa_gerak = QtWidgets.QCheckBox(self.centralwidget)
        self.anggota_badan_tidak_bisa_gerak.setGeometry(QtCore.QRect(30, 430, 421, 20))
        self.anggota_badan_tidak_bisa_gerak.setObjectName("anggota_badan_tidak_bisa_gerak")
        self.makan_sesuatu = QtWidgets.QCheckBox(self.centralwidget)
        self.makan_sesuatu.setGeometry(QtCore.QRect(30, 460, 271, 20))
        self.makan_sesuatu.setObjectName("makan_sesuatu")
        self.makan_daging = QtWidgets.QCheckBox(self.centralwidget)
        self.makan_daging.setGeometry(QtCore.QRect(30, 490, 221, 20))
        self.makan_daging.setObjectName("makan_daging")
        self.makan_jamur = QtWidgets.QCheckBox(self.centralwidget)
        self.makan_jamur.setGeometry(QtCore.QRect(30, 520, 221, 20))
        self.makan_jamur.setObjectName("makan_jamur")
        self.makan_makanan_kaleng = QtWidgets.QCheckBox(self.centralwidget)
        self.makan_makanan_kaleng.setGeometry(QtCore.QRect(30, 550, 271, 20))
        self.makan_makanan_kaleng.setObjectName("makan_makanan_kaleng")
        self.beli_susu = QtWidgets.QCheckBox(self.centralwidget)
        self.beli_susu.setGeometry(QtCore.QRect(30, 580, 201, 20))
        self.beli_susu.setObjectName("beli_susu")
        self.makan_susu = QtWidgets.QCheckBox(self.centralwidget)
        self.makan_susu.setGeometry(QtCore.QRect(30, 610, 201, 20))
        self.makan_susu.setObjectName("makan_susu")
        self.tittle = QtWidgets.QLabel(self.centralwidget)
        self.tittle.setGeometry(QtCore.QRect(320, 0, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.tittle.setFont(font)
        self.tittle.setObjectName("tittle")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(340, 650, 461, 41))
        self.submit_button.setObjectName("submit_button")
        self.submit_button.clicked.connect(self.start_process)
        self.subtitle_pertanyaan = QtWidgets.QLabel(self.centralwidget)
        self.subtitle_pertanyaan.setGeometry(QtCore.QRect(30, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.subtitle_pertanyaan.setFont(font)
        self.subtitle_pertanyaan.setObjectName("subtitle_pertanyaan")
        self.subtitle_hasil = QtWidgets.QLabel(self.centralwidget)
        self.subtitle_hasil.setGeometry(QtCore.QRect(570, 40, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.subtitle_hasil.setFont(font)
        self.subtitle_hasil.setObjectName("subtitle_hasil")
        self.staphylococcus_result = QtWidgets.QLabel(self.centralwidget)
        self.staphylococcus_result.setGeometry(QtCore.QRect(570, 70, 361, 16))
        self.staphylococcus_result.setObjectName("staphylococcus_result")
        self.jamur_result = QtWidgets.QLabel(self.centralwidget)
        self.jamur_result.setGeometry(QtCore.QRect(570, 100, 391, 16))
        self.jamur_result.setObjectName("jamur_result")
        self.salmonellae_result = QtWidgets.QLabel(self.centralwidget)
        self.salmonellae_result.setGeometry(QtCore.QRect(570, 130, 401, 16))
        self.salmonellae_result.setObjectName("salmonellae_result")
        self.clostridium_result = QtWidgets.QLabel(self.centralwidget)
        self.clostridium_result.setGeometry(QtCore.QRect(570, 160, 411, 16))
        self.clostridium_result.setObjectName("clostridium_result")
        self.campylobacter_result = QtWidgets.QLabel(self.centralwidget)
        self.campylobacter_result.setGeometry(QtCore.QRect(570, 190, 411, 16))
        self.campylobacter_result.setObjectName("campylobacter_result")
        self.diagnosa_result = QtWidgets.QLabel(self.centralwidget)
        self.diagnosa_result.setGeometry(QtCore.QRect(570, 220, 421, 16))
        self.diagnosa_result.setObjectName("diagnosa_result")
        self.treshold_box = QtWidgets.QLineEdit(self.centralwidget)
        self.treshold_box.setGeometry(QtCore.QRect(210, 650, 113, 31))
        self.treshold_box.setObjectName("treshold_box")
        self.subtitle_treshold = QtWidgets.QLabel(self.centralwidget)
        self.subtitle_treshold.setGeometry(QtCore.QRect(120, 660, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.subtitle_treshold.setFont(font)
        self.subtitle_treshold.setObjectName("subtitle_treshold")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buang_air_besar.setText(_translate("MainWindow", "Apakah anda sering mengalami buang air besar (lebih dari dua kali)?"))
        self.berak_encer.setText(_translate("MainWindow", "Apakah anda mengalami berak encer?"))
        self.berak_berdarah.setText(_translate("MainWindow", "Apakah anda mengalami berak berdarah?"))
        self.lesu.setText(_translate("MainWindow", "Apakah anda merasa lesu dan tidak bergairah?"))
        self.tidak_selera_makan.setText(_translate("MainWindow", "Apakah anda tidak selera makan?"))
        self.mual_muntah.setText(_translate("MainWindow", "Apakah anda sering merasa mual dan muntah (lebih dari satu kali)?"))
        self.sakit_di_perut.setText(_translate("MainWindow", "Apakah anda merasa sakit di bagian perut?"))
        self.tekanan_darah_rendah.setText(_translate("MainWindow", "Apakah tekanan darah anda rendah?"))
        self.pusing.setText(_translate("MainWindow", "Apakah anda merasa pusing?"))
        self.pingsan.setText(_translate("MainWindow", "Apakah anda mengalami pingsan?"))
        self.suhu_badan_tinggi.setText(_translate("MainWindow", "Apakah suhu badan anda tinggi?"))
        self.luka_badan.setText(_translate("MainWindow", "Apakah anda memiliki luka di bagian tertentu?"))
        self.anggota_badan_tidak_bisa_gerak.setText(_translate("MainWindow", "Apakah anda tidak dapat menggerakkan anggota badan tertentu?"))
        self.makan_sesuatu.setText(_translate("MainWindow", "Apakah anda pernah memakan sesuatu?"))
        self.makan_daging.setText(_translate("MainWindow", "Apakah anda memakan daging?"))
        self.makan_jamur.setText(_translate("MainWindow", "Apakah anda memakan jamur?"))
        self.makan_makanan_kaleng.setText(_translate("MainWindow", "Apakah anda memakan makanan kaleng?"))
        self.beli_susu.setText(_translate("MainWindow", "Apakah anda membeli susu?"))
        self.makan_susu.setText(_translate("MainWindow", "Apakah anda memakan susu?"))
        self.tittle.setText(_translate("MainWindow", "INFEKSI SISTEM GASTRO-USUS"))
        self.submit_button.setText(_translate("MainWindow", "PROSES"))
        self.subtitle_pertanyaan.setText(_translate("MainWindow", "Pertanyaan"))
        self.subtitle_hasil.setText(_translate("MainWindow", "Hasil"))
        self.staphylococcus_result.setText(_translate("MainWindow", "Staphylococcus Aureus :"))
        self.jamur_result.setText(_translate("MainWindow", "Jamur Beracun :"))
        self.salmonellae_result.setText(_translate("MainWindow", "Salmonellae :"))
        self.clostridium_result.setText(_translate("MainWindow", "Clostridium Botulinum :"))
        self.campylobacter_result.setText(_translate("MainWindow", "Campylobacter :"))
        self.diagnosa_result.setText(_translate("MainWindow", "Diagnosa Infeksi :"))
        self.subtitle_treshold.setText(_translate("MainWindow", "Treshold"))

    @pyqtSlot()
    def start_process(self):
        if self.buang_air_besar.isChecked():
            self.selected_value.append('1')
        if self.berak_encer.isChecked():
            self.selected_value.append('2')
        if self.berak_berdarah.isChecked():
            self.selected_value.append('3')
        if self.lesu.isChecked():
            self.selected_value.append('4')
        if self.tidak_selera_makan.isChecked():
            self.selected_value.append('5')
        if self.mual_muntah.isChecked():
            self.selected_value.append('6')
        if self.sakit_di_perut.isChecked():
            self.selected_value.append('7')
        if self.tekanan_darah_rendah.isChecked():
            self.selected_value.append('8')
        if self.pusing.isChecked():
            self.selected_value.append('9')
        if self.pingsan.isChecked():
            self.selected_value.append('10')
        if self.suhu_badan_tinggi.isChecked():
            self.selected_value.append('11')
        if self.luka_badan.isChecked():
            self.selected_value.append('12')
        if self.anggota_badan_tidak_bisa_gerak.isChecked():
            self.selected_value.append('13')
        if self.makan_sesuatu.isChecked():
            self.selected_value.append('14')
        if self.makan_daging.isChecked():
            self.selected_value.append('15')
        if self.makan_jamur.isChecked():
            self.selected_value.append('16')
        if self.makan_makanan_kaleng.isChecked():
            self.selected_value.append('17')
        if self.beli_susu.isChecked():
            self.selected_value.append('18')
        if self.makan_susu.isChecked():
            self.selected_value.append('19')
            
        ciri_mencret = ['1', '2', '4', '5']
        ciri_muntah = ['4', '5', '6']
        ciri_sakit_perut = ['4', '7']
        ciri_darah_rendah = ['4', '8', '9']
        ciri_koma = ['8', '10']
        ciri_demam = ['4', '5', '9', '11']
        ciri_septicaemia = ['4', '8', '11', '12']
        ciri_lumpuh = ['4', '13']
        ciri_mencret_berdarah = ['1', '2', '3', '4', '5']
        ciri_makan_daging = ['14', '15']
        ciri_makan_jamur = ['14', '16']
        ciri_makan_makanan_kaleng = ['14', '17']
        ciri_minum_susu = ['18', '19']
        
        staphylococcus = (self.get_ciri_value(ciri_mencret) + self.get_ciri_value(ciri_muntah) + self.get_ciri_value(ciri_sakit_perut) + self.get_ciri_value(ciri_darah_rendah) + self.get_ciri_value(ciri_makan_daging)) / 5
        self.value.append(staphylococcus)
        jamur_beracun = (self.get_ciri_value(ciri_mencret) + self.get_ciri_value(ciri_muntah) + self.get_ciri_value(ciri_sakit_perut) + self.get_ciri_value(ciri_koma) + self.get_ciri_value(ciri_makan_jamur)) / 5
        self.value.append(jamur_beracun)
        salmonellae = (self.get_ciri_value(ciri_mencret) + self.get_ciri_value(ciri_muntah) + self.get_ciri_value(ciri_sakit_perut) + self.get_ciri_value(ciri_demam) + self.get_ciri_value(ciri_septicaemia) + self.get_ciri_value(ciri_makan_daging)) / 6
        self.value.append(salmonellae)
        clostridium = (self.get_ciri_value(ciri_muntah) + self.get_ciri_value(ciri_lumpuh) + self.get_ciri_value(ciri_makan_makanan_kaleng)) / 3
        self.value.append(clostridium)
        campylobacter = (self.get_ciri_value(ciri_mencret_berdarah) + self.get_ciri_value(ciri_sakit_perut) + self.get_ciri_value(ciri_demam) + self.get_ciri_value(ciri_minum_susu)) / 4
        self.value.append(campylobacter)

        staphylococcus_value = "Staphylococcus Aureus : " + str(self.value[0]) + "%"
        # print(staphylococcus_value)
        self.staphylococcus_result.setText(staphylococcus_value)
        self.staphylococcus_result.show()

        jamur_beracun_value = "Jamur Beracun : " + str(self.value[1]) + "%"
        # print(jamur_beracun_value)
        self.jamur_result.setText(jamur_beracun_value)
        self.jamur_result.show()

        salmonellae_value = "Salmonellae : " + str(self.value[2]) + "%"
        # print(salmonellae_value)
        self.salmonellae_result.setText(salmonellae_value)
        self.salmonellae_result.show()

        clostridium_value = "Clostridium Botulinum : " + str(self.value[3]) + "%"
        # print(clostridium_value)
        self.clostridium_result.setText(clostridium_value)
        self.clostridium_result.show()

        campylobacter_value = "Campylobacter : " + str(self.value[4]) + "%"
        # print(campylobacter_value)
        self.campylobacter_result.setText(campylobacter_value)
        self.campylobacter_result.show()
        
        diagnosa_value = self.get_max_value()
        # print(diagnosa_value)
        self.diagnosa_result.setText(diagnosa_value)
        self.diagnosa_result.show()

    def get_category(self, max_index):
        category = ["Staphylococcus Aureus", "Jamur Beracun", "Salmonellae", "Clostridium Botulinum", "Campylobacter"]
        temp = ""
        for i in range(len(category)):
            if i == max_index:
                temp = category[i]
                break
        return temp

    def get_ciri_value(self, ciri):
        count = 0
        for i in range(len(ciri)):
            for j in range(len(self.selected_value)):
                if ciri[i] == self.selected_value[j]:
                    count += 1
        result = (count / len(ciri)) * 100
        return result
        
    def get_max_value(self):
        result = ""
        if max(self.value) >= float(self.treshold_box.text()):
            result = "Diagnosa Infeksi : " + str(self.get_category(self.value.index(max(self.value)))) + " - " + str(max(self.value)) + "%"
        else:
            result = "Diagnosa Infeksi : Tidak terinfeksi apapun"
        return result


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
