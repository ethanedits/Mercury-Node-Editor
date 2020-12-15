import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from mercuryeditor.mercury.calc_window import CalculatorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #print(QStyleFactory.keys())
    app.setStyle('Fusion')

    wnd = CalculatorWindow()
    wnd.show()
    app.setWindowIcon(QtGui.QIcon('icons/mercury.png'))

    sys.exit(app.exec_())
