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
import os
import sys
from PyQt5.QtGui import (
    QIcon,
    QPixmap,
)
from PyQt5.QtCore import (
    QSize, Qt
)
from PyQt5.QtWidgets import (
    QLabel,
    QToolBar,
    QStatusBar,
    QApplication,
    QFileDialog,
    QMainWindow,
    QTableView,
    QAbstractItemView,
    QWidget,
    QGridLayout,
    QTabWidget,
    QAction,
    QDialogButtonBox,
    QVBoxLayout,
    QDialog,
    
)

from models.State import State
from models.PandasModel import DataFrameModel

'''
class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

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
        self.label = QLabel(
            text,
            self,
        )
        self.label.setWordWrap(True)
        self.label.setMargin(12)
        self.setCentralWidget(self.label)
'''

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('rsc', 'img', 'ubercoc_banner_400x87.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 0.2.0"))
        layout.addWidget(QLabel("Copyright (C) 2022 José Verdú-Díaz"))
        layout.addWidget(
            QLabel(
                "This program is free software: you can redistribute it and/or modify\n"\
                "it under the terms of the GNU General Public License as published by\n"\
                "the Free Software Foundation, either version 3 of the License, or\n"\
                "(at your option) any later version.\n\n"\
                "This program is distributed in the hope that it will be useful,\n"\
                "but WITHOUT ANY WARRANTY; without even the implied warranty of\n"\
                "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"\
                "GNU General Public License for more details.\n\n"\
                "You should have received a copy of the GNU General Public License\n"\
                "along with this program.  If not, see https://www.gnu.org/licenses/"\
            )
        )

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.state = State()

        self.setWindowTitle("Ubercoc 0.2.0")
        self.setWindowIcon(QIcon("rsc/img/ubercoc_logo.png"))
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.table_view_patients = QTableView()
        self.table_view_patients.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view_patients.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabs.addTab(self.table_view_patients, "Patients")

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        file_menu = self.menuBar().addMenu("File")

        open_action = QAction("Open", self)
        open_action.setStatusTip("Open file")
        open_action.triggered.connect(self.select_file)
        file_menu.addAction(open_action)

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction("About", self)
        about_action.setStatusTip("About Ubercoc")
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        self.show()

    def select_file(self) -> None:
        file, check = QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "Microsoft Excel Worksheet  (*.xlsx)",
        )
        if check:
            self.state.new(file)
            df = self.state.patients_df()
            model = DataFrameModel(df)
            self.table_view_patients.setModel(model)

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
