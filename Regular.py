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
from RegularUI import Ui_Dialog

import resource_rc

RegSpliter = "#[##]#"
UserDBFile = "data.idx"

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
        self.NewAction = QtGui.QAction(u"添加", self, triggered=self.OpenDialog, shortcut="Ctrl+N")
        self.saveAction = QtGui.QAction(u"保存当前", self, triggered=self.OpenDialog, shortcut="Ctrl+S")
        self.SelectAction = QtGui.QAction(u"选择", self)
        self.aboutAction = QtGui.QAction(u"关于", self, triggered=self.AboutDialog)

        self.QCMenu.addAction(self.NewAction)
        self.QCMenu.addAction(self.saveAction)
        self.QCMenu.addSeparator()

        self.QCSubMenu = self.QCMenu.addMenu(u"选择")

        # get define regular
        copyDataText = []
        userData = QtCore.QFile.exists(UserDBFile)
        # user data
        newDataFile = QtCore.QFile(UserDBFile)

        if userData:
            DataFile = newDataFile
        else:
            DataFile = QtCore.QFile(":/data/data.idx")

        if (DataFile.open(QtCore.QIODevice.ReadOnly)):
            DataText = QtCore.QTextStream(DataFile)
            while not DataText.atEnd():
                line = DataText.readLine()
                line = unicode(line.toUtf8(),'utf8', 'ignore')
                if line.find(RegSpliter) == -1: continue
                [regName, regStr] = line.split(RegSpliter)
                receiver = (lambda v: lambda: self.UseRegular(v))(regStr)
                self.QCSubMenu.addAction(QtGui.QAction(regName, self, triggered=receiver))
                # copy init data
                copyDataText.append(u"%s" % line)

        DataFile.close()

        if (newDataFile.open(QtCore.QIODevice.WriteOnly)):
            newDataText = QtCore.QTextStream(newDataFile)
            newDataText<<"\n".join(copyDataText)

        newDataFile.close()

        self.QCMenu.addSeparator()
        self.QCMenu.addAction(self.aboutAction)

        self.ui.QCButton.setMenu(self.QCMenu)

    def UseRegular (self, val):
        self.ui.TextCode.setPlainText(val)

    def SaveRegular (self, regName, regCode):
        DataFile = QtCore.QFile(UserDBFile)
        if (DataFile.open(QtCore.QIODevice.Append)):
            DataText = QtCore.QTextStream(DataFile)
            DataText<<u"\n%s%s%s" % (regName, RegSpliter, regCode)

        DataFile.close()
        receiver = (lambda v: lambda: self.UseRegular(v))(regCode)
        self.QCSubMenu.addAction(QtGui.QAction(regName, self, triggered=receiver))

    def OpenDialog(self):
        val = unicode(self.ui.TextCode.toPlainText().toUtf8(),'utf8', 'ignore')
        DialogTitle = (val and [u"保存正则表达式"] or [u"添加正则表达式"])[0]
        Dialog = ShowDialogUI(DialogTitle, val, self)

        if Dialog.exec_() == QtGui.QDialog.Accepted:
            self.SaveRegular(Dialog.senderName(), Dialog.senderCodes())

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
            [' ', '&nbsp;'],
            ['\t', '&nbsp;&nbsp;&nbsp;&nbsp;'],
            ['\r', ' <br>'],
            ['\n', ' <br>'],
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


class ShowDialogUI(QtGui.QDialog):
    def __init__(self, title, val, parent):
        super(ShowDialogUI, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle(title)
        self.ui.RegCode.setPlainText(val)

        self.connect(self.ui.BtnSave, QtCore.SIGNAL("clicked()"), self.verify)
        self.connect(self.ui.BtnCancel, QtCore.SIGNAL("clicked()"), self.reject)

    def senderName(self):
        return self.ui.RegName.text()

    def senderCodes(self):
        return self.ui.RegCode.toPlainText()

    def verify(self):
        RegName = self.ui.RegName.text()
        RegCode = self.ui.RegCode.toPlainText()
        if RegName and RegCode:
            self.accept()
            return

        if not RegName:
            self.ui.RegName.setFocus()
        elif not RegCode:
            self.ui.RegCode.setFocus()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Regularapp = RegularUI()
    Regularapp.show()
    sys.exit(app.exec_())

