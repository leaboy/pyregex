# -*- coding: utf-8 -*-

# The Main App for RegEx Test.
#
# Created: Tue Nov 09 20:56:08 2010
#      By: leaboy.w
#   Email: leaboy.w@gmail.com
#
# GNU Free Documentation License 1.3

from PyQt4 import QtCore, QtGui

from RegularUI import Ui_MainForm

import resource_rc

RegSpliter = "#[##]#"

class RegularUI(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RegularUI, self).__init__(parent)

        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.CreateQCMenu()
        self.ConnectEvent()

    def CreateQCMenu (self):
        # qc menu
        self.QCMenu = QtGui.QMenu(self)
        self.NewAction = QtGui.QAction(u"添加", self, triggered=self.NewRegular, shortcut="Ctrl+N")
        self.saveAction = QtGui.QAction(u"保存当前", self, triggered=self.SaveRegular, shortcut="Ctrl+S")
        self.aboutAction = QtGui.QAction(u"关于", self, triggered=self.AboutDialog)

        self.QCMenu.addAction(self.NewAction)
        self.QCMenu.addAction(self.saveAction)
        self.QCMenu.addSeparator()

        # get define regular
        InitRegular = []
        DataFile = QtCore.QFile(":/data/data.idx")
        if (DataFile.open(QtCore.QIODevice.ReadOnly)):
            DataText = QtCore.QTextStream(DataFile)
            while not DataText.atEnd():
                line = DataText.readLine()
                line = unicode(line.toUtf8(),'utf8', 'ignore')
                if line.find(RegSpliter) == -1: next
                [regName, regStr] = line.split(RegSpliter)
                receiver = (lambda v: lambda: self.UseRegular(v))(regStr)
                self.QCMenu.addAction(QtGui.QAction(regName, self, triggered=receiver))

        self.QCMenu.addSeparator()
        self.QCMenu.addAction(self.aboutAction)

        self.ui.QCButton.setMenu(self.QCMenu)

    def UseRegular (self, val):
        self.ui.TextCode.setPlainText(val)

    def NewRegular (self):
        self.openDialog()

    def SaveRegular (self):
        self.openDialog('aaa')

    def openDialog(self, v=None):
        dialog = DetailsDialog("Enter Customer Details", self)

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.createLetter(dialog.senderName(), dialog.senderAddress(),
                    dialog.orderItems(), dialog.sendOffers())

    def AboutDialog (self):
        QtGui.QMessageBox.about(self, "About PyRegEx Tester",
                "<p>The <b>PyRegEx Tester</b> helps you to " \
                "easily test the regular expression.<br/>" \
                "-- So, Try it. --</p>")

    def DoMatch (self):
        import re

        # unicode match regular and text
        TextReg = unicode(self.ui.TextCode.toPlainText().toUtf8(),'utf8', 'ignore')
        TextStr = unicode(self.ui.TextMatch.toPlainText().toUtf8(),'utf8', 'ignore')

        # get match setting
        SetLetter = self.ui.SetLetter.isChecked()
        SetGlobal = self.ui.SetGlobal.isChecked()
        SetMultiline = self.ui.SetMultiline.isChecked()
        SetReplace = self.ui.SetReplace.isChecked()

        # replacer str while SetReplace is True
        TextReplacer = self.ui.TextReplacer.text()

        # random split str
        def RandomStr (length):
            import random
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+=@'
            destr = ''.join(random.sample(chars,length))
            return destr

        StartSepstr = RandomStr(11)
        EndSepstr = RandomStr(16)

        # create reg object
        ReFlags = 0
        if SetLetter:
            ReFlags = (ReFlags and [ReFlags|re.I] or [re.I])[0]
        if SetGlobal:
            ReFlags = (ReFlags and [ReFlags|re.S] or [re.S])[0]
        if SetMultiline:
            ReFlags = (ReFlags and [ReFlags|re.M] or [re.M])[0]

        def Getrepl (m):
            if m is None: return
            s = m.group(0)
            s = (SetReplace and [TextReplacer] or [s])[0]
            if not s: return
            return u"%s%s%s" % (StartSepstr, s, EndSepstr)

        def Setrepcolor (s):
            s = s.replace(StartSepstr, "<span style='background-color:#FF0; color:#00A800;'>")
            s = s.replace(EndSepstr, "</span>")
            return s

        htmlCodes = [
            ['<', '&lt;'],
            ['>', '&gt;'],
            ['"', '&quot;'],
            ['\n', '<br>'],
        ]

        def formatHtml (s):
            for code in htmlCodes:
                s = s.replace(code[0], code[1])
            return s

        try:
            pattern = re.compile(r"%s" % TextReg, flags=ReFlags)
            TextStr = pattern.sub(Getrepl, TextStr)
            TextStr = formatHtml(TextStr)
            TextStr = Setrepcolor(TextStr)
        except:
            self.ui.TextResualt.clear()
            self.ui.TextResualt.appendHtml(u"<b style='color:red'>输入的值不是一个规则表达式</b>")
            return

        self.ui.TextResualt.clear()
        self.ui.TextResualt.appendHtml(TextStr)


    def ConnectEvent (self):
        # set replacer
        self.ui.SetReplace.toggled.connect(self.ui.TextReplacer.setEnabled)
        # reg match
        self.connect(self.ui.TextCode, QtCore.SIGNAL("textChanged()"), self.DoMatch)
        self.connect(self.ui.TextMatch, QtCore.SIGNAL("textChanged()"), self.DoMatch)
        self.ui.SetLetter.toggled.connect(self.DoMatch)
        self.ui.SetGlobal.toggled.connect(self.DoMatch)
        self.ui.SetMultiline.toggled.connect(self.DoMatch)
        self.ui.SetReplace.toggled.connect(self.DoMatch)
        # replace
        self.connect(self.ui.TextReplacer, QtCore.SIGNAL("textChanged(const QString)"), self.DoMatch)

class DetailsDialog(QtGui.QDialog):
    def __init__(self, title, parent):
        super(DetailsDialog, self).__init__(parent)

        self.items = ("T-shirt", "Badge", "Reference book", "Coffee cup")

        nameLabel = QtGui.QLabel("Name:")
        addressLabel = QtGui.QLabel("Address:")
        addressLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.nameEdit = QtGui.QLineEdit()
        self.addressEdit = QtGui.QTextEdit()
        self.offersCheckBox = QtGui.QCheckBox("Send information about "
                "products and special offers:")

        self.setupItemsTable()

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.verify)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameEdit, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0)
        mainLayout.addWidget(self.addressEdit, 1, 1)
        mainLayout.addWidget(self.itemsTable, 0, 2, 2, 1)
        mainLayout.addWidget(self.offersCheckBox, 2, 1, 1, 2)
        mainLayout.addWidget(buttonBox, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        self.setWindowTitle(title)

    def setupItemsTable(self):
        self.itemsTable = QtGui.QTableWidget(len(self.items), 2)

        for row, item in enumerate(self.items):
            name = QtGui.QTableWidgetItem(item)
            name.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.itemsTable.setItem(row, 0, name)
            quantity = QtGui.QTableWidgetItem('1')
            self.itemsTable.setItem(row, 1, quantity)

    def orderItems(self):
        orderList = []

        for row in range(len(self.items)):
            text = self.itemsTable.item(row, 0).text()
            quantity = int(self.itemsTable.item(row, 1).data(QtCore.Qt.DisplayRole))
            orderList.append((text, max(0, quantity)))

        return orderList

    def senderName(self):
        return self.nameEdit.text()

    def senderAddress(self):
        return self.addressEdit.toPlainText()

    def sendOffers(self):
        return self.offersCheckBox.isChecked()

    def verify(self):
        if self.nameEdit.text() and self.addressEdit.toPlainText():
            self.accept()
            return

        answer = QtGui.QMessageBox.warning(self, "Incomplete Form",
                "The form does not contain all the necessary information.\n"
                "Do you want to discard it?",
                QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if answer == QtGui.QMessageBox.Yes:
            self.reject()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Regularapp = RegularUI()
    Regularapp.show()
    sys.exit(app.exec_())

