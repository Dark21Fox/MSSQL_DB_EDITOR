# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Develop\PyProject\MsSQLDB\enter.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Enter(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(336, 315)
        Form.setStyleSheet("")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget#widget{ background-image: url(:/newPrefix/image/wallhaven-mdeo68.jpg);}")
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_5.setSpacing(20)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("background-color: #333;\n"
"border-radius: 30px;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setStyleSheet("border-radius: 3px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setStyleSheet("color: white; ")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setStyleSheet("color: white; ")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;      \n"
"  border-width: 1px;      \n"
"  border-color:  black;   \n"
"  border-style: outset;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("color: white; ")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;      \n"
"  border-width: 1px;      \n"
"  border-color:  black;   \n"
"  border-style: outset;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(102, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"  color: white;                     \n"
"    \n"
"    background-color: rgb(255, 49, 69);\n"
"  width: 70px;                      \n"
"  height: 25px;                    \n"
"  font-size: 14px;                \n"
"  font-weight: bold;              \n"
"  border: none;                     \n"
"  text-align: center;\n"
"  border-radius: 7px;               \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(40,40,40);  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(60,60,60);   \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setStyleSheet("QPushButton{\n"
"  color: white;                     \n"
"  background-color: rgb(255, 49, 69);\n"
"  width: 70px;                      \n"
"  height: 25px;                    \n"
"  font-size: 14px;                \n"
"  font-weight: bold;              \n"
"  border: none;                     \n"
"  text-align: center;\n"
"  border-radius: 7px;      \n"
"  border-width: 2px;         \n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(40,40,40);  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(60,60,60);   \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 3)
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setStyleSheet("border-radius: 3px;")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(20)
        self.frame.setMidLineWidth(20)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("color: white; ")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("color: white; \n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;      \n"
"  border-width: 1px;      \n"
"  border-color:  black;   \n"
"  border-style: outset;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;      \n"
"  border-width: 1px;      \n"
"  border-color:  black;   \n"
"  border-style: outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setStyleSheet("color: white; ")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вход"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Пользователь</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Имя пользователя</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Пароль</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Выход"))
        self.pushButton.setText(_translate("Form", "Соединение"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Имя сервера</span></p></body></html>"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p>color: white; </p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Имя базы данных </span></p></body></html>"))
        self.lineEdit_2.setText(_translate("Form", "Agentstvo"))
        self.lineEdit.setText(_translate("Form", "VEDROID"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Источник данных</span></p></body></html>"))
import xrc_rc
