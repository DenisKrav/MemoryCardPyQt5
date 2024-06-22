from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QSpinBox)
from memo_qss import * # подгружаем "таблицы стилей"
from memo_app import app

from memo_edit_layout import layout_form
from memo_card_layout import layout_card

class CompounWidget(QWidget):
    def __init__(self, layout, parent=None, flags=Qt.WindowFlags):
        super().__init__(parent=parent, flags=flags)
        self.setLayout(layout)

wdgt_card = CompounWidget(layout_card)
wdgt_edit = CompounWidget(layout_form)
btn_card = QPushButton("Задати питання")
btn_form = QPushButton("Редагування питання")

main_line = QVBoxLayout()
main_line.addWidget(btn_card)
main_line.addWidget(btn_form)

layout_main = QVBoxLayout()
layout_main.addWidget(wdgt_card)
layout_main.addWidget(wdgt_edit)
layout_main.addWidget(main_line)
