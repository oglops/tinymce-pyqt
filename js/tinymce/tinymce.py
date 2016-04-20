#!/usr/bin/env python

import sys
import os
from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4 import uic

# enable ctrl-c to kill the app
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class MyWindow(QtGui.QDialog):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.layout = QtGui.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.webview = QtWebKit.QWebView()
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)

        self.webview.load(
            QtCore.QUrl(os.path.join(os.path.dirname(__file__), 'index.html')))

        self.resize(950, 500)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
