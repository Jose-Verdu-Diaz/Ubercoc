'''
Copyright (C) 2022 José Verdú-Díaz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/
'''

import sys
import pandas as pd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

from models import Patient

class AboutWindow(qtw.QMainWindow):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)

        self.setWindowTitle("Ubercoc 0.1.0 - About")
        self.label = qtw.QLabel(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur dignissim enim eget ipsum lacinia feugiat. Vestibulum dignissim elit neque, nec tempor sapien fermentum sit amet. Duis est massa, mollis quis justo non, sagittis faucibus orci. Etiam posuere luctus quam, vel congue turpis vehicula vel. Aliquam pellentesque lacus in nulla accumsan hendrerit. Nulla urna metus, tempus id auctor id, lobortis non arcu. Pellentesque ligula justo, tristique eget tellus vitae, suscipit tempus libero. Nulla pretium nulla non arcu consectetur facilisis. Aliquam gravida aliquam justo, nec interdum elit auctor id. Aliquam non auctor erat, id lacinia lacus. Suspendisse dignissim vestibulum neque, et commodo dui consectetur facilisis. Vivamus vel nibh ut erat vehicula pharetra at vel ex. Aliquam ut magna vehicula, congue ante interdum, volutpat ex. Donec in ex vitae massa commodo bibendum eu et velit. Donec placerat tortor vitae erat consequat posuere.',
            self)
        self.label.setWordWrap(True)
        self.label.setMargin(12)
        self.setCentralWidget(self.label)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ubercoc 0.1.0")
        self.setWindowIcon(qtg.QIcon('rsc/img/logo.svg'))
        self.setGeometry(100, 100, 500, 300)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        tools_menu = menu_bar.addMenu('Tools')
        help_menu = menu_bar.addMenu('Help')
        
        self.text_edit = qtw.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        file_menu.addAction('New', lambda: self.text_edit.clear())
        file_menu.addAction('Open', lambda: self.select_file())

        self.dialog = AboutWindow(self)
        help_menu.addAction('About', lambda: self.dialog.show())

        # Toolbar
        toolbar = qtw.QToolBar('Toolbar')
        self.addToolBar(toolbar)

        # Statusbar
        self.status_bar = qtw.QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Ubercoc 0.1.0')

        self.show()


    def select_file(self) -> str:
        file , check = qtw.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "Microsoft Excel Worksheet  (*.xlsx)",
        )
        if check:
            print(file)
            return file
        else: 
            return None


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())