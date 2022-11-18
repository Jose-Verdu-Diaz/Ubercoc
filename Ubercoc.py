"""
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
"""

import sys
import pandas as pd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

from models.State import State


class AboutWindow(qtw.QMainWindow):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)

        self.setWindowTitle("Ubercoc 0.1.0 - About")
        text = """
Ubercoc 0.1.0

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
"""
        self.label = qtw.QLabel(
            text,
            self,
        )
        self.label.setWordWrap(True)
        self.label.setMargin(12)
        self.setCentralWidget(self.label)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.state = State()

        self.setWindowTitle("Ubercoc 0.1.0")
        self.setWindowIcon(qtg.QIcon("rsc/img/logo.png"))
        self.setGeometry(100, 100, 500, 300)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        tools_menu = menu_bar.addMenu("Tools")
        help_menu = menu_bar.addMenu("Help")

        self.text_edit = qtw.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        #file_menu.addAction("New", lambda: self.text_edit.clear())
        file_menu.addAction("Open", lambda: self.select_file())

        self.dialog = AboutWindow(self)
        help_menu.addAction("About", lambda: self.dialog.show())

        # Toolbar
        toolbar = qtw.QToolBar("Toolbar")
        self.addToolBar(toolbar)

        # Statusbar
        self.status_bar = qtw.QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ubercoc 0.1.0")

        self.show()

    def select_file(self) -> None:
        file, check = qtw.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "Microsoft Excel Worksheet  (*.xlsx)",
        )
        if check:
            self.state.new(file)
            self.text_edit.setText(F'{len(self.state.patients)} patients have been added!')


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
