# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Regular.ui'
#
# Created: Thu Nov 18 15:46:10 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(440, 460)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        # set font
        self.setFont(MainForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon_32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        MainForm.setStyleSheet("None")
        self.verticalLayout = QtGui.QVBoxLayout(MainForm)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RegSet = QtGui.QHBoxLayout()
        self.RegSet.setObjectName("RegSet")
        self.SetGroupBox = QtGui.QGroupBox(MainForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetGroupBox.sizePolicy().hasHeightForWidth())
        self.SetGroupBox.setSizePolicy(sizePolicy)
        self.SetGroupBox.setObjectName("SetGroupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.SetGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TextCode = QtGui.QPlainTextEdit(self.SetGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextCode.sizePolicy().hasHeightForWidth())
        self.TextCode.setSizePolicy(sizePolicy)
        self.TextCode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TextCode.setLineWidth(1)
        self.TextCode.setObjectName("TextCode")
        self.verticalLayout_2.addWidget(self.TextCode)
        self.SetChild_1 = QtGui.QHBoxLayout()
        self.SetChild_1.setObjectName("SetChild_1")
        self.SetLetter = QtGui.QCheckBox(self.SetGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetLetter.sizePolicy().hasHeightForWidth())
        self.SetLetter.setSizePolicy(sizePolicy)
        self.SetLetter.setObjectName("SetLetter")
        self.SetChild_1.addWidget(self.SetLetter)
        self.SetGlobal = QtGui.QCheckBox(self.SetGroupBox)
        self.SetGlobal.setChecked(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetGlobal.sizePolicy().hasHeightForWidth())
        self.SetGlobal.setSizePolicy(sizePolicy)
        self.SetGlobal.setObjectName("SetGlobal")
        self.SetChild_1.addWidget(self.SetGlobal)
        self.SetMultiline = QtGui.QCheckBox(self.SetGroupBox)
        self.SetMultiline.setChecked(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetMultiline.sizePolicy().hasHeightForWidth())
        self.SetMultiline.setSizePolicy(sizePolicy)
        self.SetMultiline.setObjectName("SetMultiline")
        self.SetChild_1.addWidget(self.SetMultiline)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.SetChild_1.addItem(spacerItem)
        self.QCButton = QtGui.QPushButton(self.SetGroupBox)
        self.QCButton.setMinimumSize(QtCore.QSize(90, 28))
        self.QCButton.setObjectName("QCButton")
        self.SetChild_1.addWidget(self.QCButton)
        self.verticalLayout_2.addLayout(self.SetChild_1)
        self.SetChild_2 = QtGui.QHBoxLayout()
        self.SetChild_2.setObjectName("SetChild_2")
        self.SetReplace = QtGui.QCheckBox(self.SetGroupBox)
        self.SetReplace.setObjectName("SetReplace")
        self.SetChild_2.addWidget(self.SetReplace)
        self.TextReplacer = QtGui.QLineEdit(self.SetGroupBox)
        self.TextReplacer.setDisabled(True)
        self.TextReplacer.setObjectName("TextReplacer")
        self.SetChild_2.addWidget(self.TextReplacer)
        self.verticalLayout_2.addLayout(self.SetChild_2)
        self.RegSet.addWidget(self.SetGroupBox)
        self.verticalLayout.addLayout(self.RegSet)
        self.RegText = QtGui.QHBoxLayout()
        self.RegText.setObjectName("RegText")
        self.TextGroupBox = QtGui.QGroupBox(MainForm)
        self.TextGroupBox.setObjectName("TextGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.TextGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TextMatch = QtGui.QPlainTextEdit(self.TextGroupBox)
        self.TextMatch.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextMatch.sizePolicy().hasHeightForWidth())
        self.TextMatch.setSizePolicy(sizePolicy)
        self.TextMatch.setBaseSize(QtCore.QSize(0, 0))
        self.TextMatch.setObjectName("TextMatch")
        self.verticalLayout_3.addWidget(self.TextMatch)
        self.RegText.addWidget(self.TextGroupBox)
        self.verticalLayout.addLayout(self.RegText)
        self.RegResualt = QtGui.QHBoxLayout()
        self.RegResualt.setObjectName("RegResualt")
        self.ResualtGroupBox = QtGui.QGroupBox(MainForm)
        self.ResualtGroupBox.setObjectName("ResualtGroupBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.ResualtGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TextResualt = QtGui.QPlainTextEdit(self.ResualtGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextResualt.sizePolicy().hasHeightForWidth())
        self.TextResualt.setSizePolicy(sizePolicy)
        self.TextResualt.setReadOnly(True)
        self.TextResualt.setObjectName("TextResualt")
        self.verticalLayout_4.addWidget(self.TextResualt)
        self.RegResualt.addWidget(self.ResualtGroupBox)
        self.verticalLayout.addLayout(self.RegResualt)

        # set font
        self.setFont(self.SetLetter)
        self.setFont(self.SetGlobal)
        self.setFont(self.SetMultiline)
        self.setFont(self.QCButton)
        self.setFont(self.SetReplace)
        self.setFont(self.TextReplacer)

        self.setFont(self.TextCode)
        self.setFont(self.TextMatch)
        self.setFont(self.TextResualt)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "PyRegEx Tester", None, QtGui.QApplication.UnicodeUTF8))
        self.SetGroupBox.setTitle(QtGui.QApplication.translate("MainForm", "正则表达式", None, QtGui.QApplication.UnicodeUTF8))
        self.SetLetter.setText(QtGui.QApplication.translate("MainForm", "大小写注意", None, QtGui.QApplication.UnicodeUTF8))
        self.SetGlobal.setText(QtGui.QApplication.translate("MainForm", "全局", None, QtGui.QApplication.UnicodeUTF8))
        self.SetMultiline.setText(QtGui.QApplication.translate("MainForm", "多行", None, QtGui.QApplication.UnicodeUTF8))
        self.QCButton.setText(QtGui.QApplication.translate("MainForm", "快速选择", None, QtGui.QApplication.UnicodeUTF8))
        self.SetReplace.setText(QtGui.QApplication.translate("MainForm", "替换", None, QtGui.QApplication.UnicodeUTF8))
        self.TextGroupBox.setTitle(QtGui.QApplication.translate("MainForm", "查找文本", None, QtGui.QApplication.UnicodeUTF8))
        self.ResualtGroupBox.setTitle(QtGui.QApplication.translate("MainForm", "结果", None, QtGui.QApplication.UnicodeUTF8))

    def setFont (self, ele):
        font = QtGui.QFont()
        font.setFamily(u"Courier New,微软雅黑")
        ele.setFont(font)

