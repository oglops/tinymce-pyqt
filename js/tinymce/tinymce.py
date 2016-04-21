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
        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        webView = QtWebKit.QWebView()

        webInspector = QtWebKit.QWebInspector(self)
        page = webView.page()
        page.settings().setAttribute(
            QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
        webInspector.setPage(page)
        webInspector.setVisible(True)

        splitter = QtGui.QSplitter(self)
        splitter.addWidget(webView)
        splitter.addWidget(webInspector)
        splitter.setSizes([3, 0])

        layout.addWidget(splitter)

        self.setLayout(layout)

        webView.load(
            QtCore.QUrl(os.path.join(os.path.dirname(__file__), 'index.html')))

        self.resize(950, 500)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
