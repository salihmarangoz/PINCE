# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 659)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(751, 659))
        MainWindow.setMaximumSize(QtCore.QSize(751, 659))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.processbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processbutton.sizePolicy().hasHeightForWidth())
        self.processbutton.setSizePolicy(sizePolicy)
        self.processbutton.setText("")
        self.processbutton.setObjectName("processbutton")
        self.horizontalLayout_5.addWidget(self.processbutton)
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Open.sizePolicy().hasHeightForWidth())
        self.pushButton_Open.setSizePolicy(sizePolicy)
        self.pushButton_Open.setText("")
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.horizontalLayout_5.addWidget(self.pushButton_Open)
        self.pushButton_Save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Save.sizePolicy().hasHeightForWidth())
        self.pushButton_Save.setSizePolicy(sizePolicy)
        self.pushButton_Save.setText("")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout_5.addWidget(self.pushButton_Save)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_SelectedProcess = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectedProcess.setObjectName("label_SelectedProcess")
        self.horizontalLayout_5.addWidget(self.label_SelectedProcess)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButton_Settings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Settings.sizePolicy().hasHeightForWidth())
        self.pushButton_Settings.setSizePolicy(sizePolicy)
        self.pushButton_Settings.setText("")
        self.pushButton_Settings.setObjectName("pushButton_Settings")
        self.horizontalLayout_5.addWidget(self.pushButton_Settings)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tableWidget_valuesearchtable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_valuesearchtable.sizePolicy().hasHeightForWidth())
        self.tableWidget_valuesearchtable.setSizePolicy(sizePolicy)
        self.tableWidget_valuesearchtable.setMinimumSize(QtCore.QSize(330, 0))
        self.tableWidget_valuesearchtable.setObjectName("tableWidget_valuesearchtable")
        self.tableWidget_valuesearchtable.setColumnCount(3)
        self.tableWidget_valuesearchtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_valuesearchtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_valuesearchtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_valuesearchtable.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_9.addWidget(self.tableWidget_valuesearchtable)
        self.QWidget_Toolbox = QtWidgets.QWidget(self.centralwidget)
        self.QWidget_Toolbox.setEnabled(False)
        self.QWidget_Toolbox.setObjectName("QWidget_Toolbox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.QWidget_Toolbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_NewFirstScan = QtWidgets.QPushButton(self.QWidget_Toolbox)
        self.pushButton_NewFirstScan.setObjectName("pushButton_NewFirstScan")
        self.horizontalLayout_6.addWidget(self.pushButton_NewFirstScan)
        self.pushButton_NextScan = QtWidgets.QPushButton(self.QWidget_Toolbox)
        self.pushButton_NextScan.setObjectName("pushButton_NextScan")
        self.horizontalLayout_6.addWidget(self.pushButton_NextScan)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pushButton_UndoScan = QtWidgets.QPushButton(self.QWidget_Toolbox)
        self.pushButton_UndoScan.setObjectName("pushButton_UndoScan")
        self.horizontalLayout_6.addWidget(self.pushButton_UndoScan)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget = QtWidgets.QWidget(self.QWidget_Toolbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_Bits = QtWidgets.QRadioButton(self.widget)
        self.radioButton_Bits.setObjectName("radioButton_Bits")
        self.verticalLayout_2.addWidget(self.radioButton_Bits)
        self.radioButton_Decimal = QtWidgets.QRadioButton(self.widget)
        self.radioButton_Decimal.setObjectName("radioButton_Decimal")
        self.verticalLayout_2.addWidget(self.radioButton_Decimal)
        self.checkBox_Hex = QtWidgets.QCheckBox(self.widget)
        self.checkBox_Hex.setObjectName("checkBox_Hex")
        self.verticalLayout_2.addWidget(self.checkBox_Hex)
        self.horizontalLayout_7.addWidget(self.widget)
        self.lineEdit_Scan = QtWidgets.QLineEdit(self.QWidget_Toolbox)
        self.lineEdit_Scan.setObjectName("lineEdit_Scan")
        self.horizontalLayout_7.addWidget(self.lineEdit_Scan)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget1 = QtWidgets.QWidget(self.QWidget_Toolbox)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_ScanType = QtWidgets.QComboBox(self.widget1)
        self.comboBox_ScanType.setObjectName("comboBox_ScanType")
        self.horizontalLayout_2.addWidget(self.comboBox_ScanType)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_ValueType = QtWidgets.QComboBox(self.widget1)
        self.comboBox_ValueType.setObjectName("comboBox_ValueType")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_ValueType)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton_ShowMemoryRegions = QtWidgets.QPushButton(self.widget1)
        self.pushButton_ShowMemoryRegions.setObjectName("pushButton_ShowMemoryRegions")
        self.verticalLayout_4.addWidget(self.pushButton_ShowMemoryRegions)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_4.addWidget(self.widget1)
        self.widget_2 = QtWidgets.QWidget(self.QWidget_Toolbox)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_RoundedDefault = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_RoundedDefault.setObjectName("radioButton_RoundedDefault")
        self.verticalLayout.addWidget(self.radioButton_RoundedDefault)
        self.radioButton_RoundedExtreme = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_RoundedExtreme.setObjectName("radioButton_RoundedExtreme")
        self.verticalLayout.addWidget(self.radioButton_RoundedExtreme)
        self.radioButton_Truncated = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_Truncated.setObjectName("radioButton_Truncated")
        self.verticalLayout.addWidget(self.radioButton_Truncated)
        self.checkBox_Unicode = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_Unicode.setObjectName("checkBox_Unicode")
        self.verticalLayout.addWidget(self.checkBox_Unicode)
        self.checkBox_CaseSensitive = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_CaseSensitive.setObjectName("checkBox_CaseSensitive")
        self.verticalLayout.addWidget(self.checkBox_CaseSensitive)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.checkBox_Unrandomizer = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_Unrandomizer.setObjectName("checkBox_Unrandomizer")
        self.verticalLayout_3.addWidget(self.checkBox_Unrandomizer)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9.addWidget(self.QWidget_Toolbox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_MemoryView = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_MemoryView.setObjectName("pushButton_MemoryView")
        self.horizontalLayout_8.addWidget(self.pushButton_MemoryView)
        spacerItem5 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.pushButton_CopyToAddressList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CopyToAddressList.setText("")
        self.pushButton_CopyToAddressList.setObjectName("pushButton_CopyToAddressList")
        self.horizontalLayout_8.addWidget(self.pushButton_CopyToAddressList)
        self.pushButton_CleanAddressList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CleanAddressList.setText("")
        self.pushButton_CleanAddressList.setObjectName("pushButton_CleanAddressList")
        self.horizontalLayout_8.addWidget(self.pushButton_CleanAddressList)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.pushButton_AddAddressManually = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AddAddressManually.setObjectName("pushButton_AddAddressManually")
        self.horizontalLayout_8.addWidget(self.pushButton_AddAddressManually)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.verticalLayout_6.addWidget(self.tableWidget_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_AdvancedOptions = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AdvancedOptions.setObjectName("pushButton_AdvancedOptions")
        self.horizontalLayout_10.addWidget(self.pushButton_AdvancedOptions)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.pushButton_TableExtras = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_TableExtras.setObjectName("pushButton_TableExtras")
        self.horizontalLayout_10.addWidget(self.pushButton_TableExtras)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.comboBox_ValueType.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PINCE"))
        self.label_SelectedProcess.setText(_translate("MainWindow", "No Process Selected"))
        item = self.tableWidget_valuesearchtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_valuesearchtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_valuesearchtable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Previous"))
        self.pushButton_NewFirstScan.setText(_translate("MainWindow", "First Scan"))
        self.pushButton_NextScan.setText(_translate("MainWindow", "Next Scan"))
        self.pushButton_UndoScan.setText(_translate("MainWindow", "Undo Scan"))
        self.radioButton_Bits.setText(_translate("MainWindow", "Bits"))
        self.radioButton_Decimal.setText(_translate("MainWindow", "Decimal"))
        self.checkBox_Hex.setText(_translate("MainWindow", "Hex"))
        self.label.setText(_translate("MainWindow", "Scan Type:"))
        self.label_2.setText(_translate("MainWindow", "Value Type:"))
        self.comboBox_ValueType.setItemText(0, _translate("MainWindow", "Byte"))
        self.comboBox_ValueType.setItemText(1, _translate("MainWindow", "2 Bytes"))
        self.comboBox_ValueType.setItemText(2, _translate("MainWindow", "4 Bytes"))
        self.comboBox_ValueType.setItemText(3, _translate("MainWindow", "8 Bytes"))
        self.comboBox_ValueType.setItemText(4, _translate("MainWindow", "Float"))
        self.comboBox_ValueType.setItemText(5, _translate("MainWindow", "Double"))
        self.comboBox_ValueType.setItemText(6, _translate("MainWindow", "String"))
        self.comboBox_ValueType.setItemText(7, _translate("MainWindow", "Array of byte"))
        self.pushButton_ShowMemoryRegions.setText(_translate("MainWindow", "Show Memory Regions"))
        self.radioButton_RoundedDefault.setText(_translate("MainWindow", "Rounded (Default)"))
        self.radioButton_RoundedExtreme.setText(_translate("MainWindow", "Rounded (Extreme)"))
        self.radioButton_Truncated.setText(_translate("MainWindow", "Truncated"))
        self.checkBox_Unicode.setText(_translate("MainWindow", "Unicode"))
        self.checkBox_CaseSensitive.setText(_translate("MainWindow", "Case Sensitive"))
        self.checkBox_Unrandomizer.setText(_translate("MainWindow", "Unrandomizer"))
        self.pushButton_MemoryView.setText(_translate("MainWindow", "Memory View"))
        self.pushButton_AddAddressManually.setText(_translate("MainWindow", "Add Address Manually"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Frozen"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Value"))
        self.pushButton_AdvancedOptions.setText(_translate("MainWindow", "Advanced Options"))
        self.pushButton_TableExtras.setText(_translate("MainWindow", "Table Extras"))

