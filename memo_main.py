from memo_card_layout import (
    app, layout_card,
    lb_Question, lb_Correct, lb_Result,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_question, show_result
)
from PyQt5.QtWidgets import QWidget
from random import shuffle
from memo_app import app
from memo_data import Form, FormView
from memo_main_layout import (layout_main, btn_card, btn_form,
                              wdgt_card, wdgt_edit)
from memo_edit_layout import (txt_Question, txt_Answer,
                              txt_Wrong1, txt_Wrong2, txt_Wrong3)

card_width, card_height = 800, 450
text_wrong = '''<font color="red">Невірно</font>'''
text_correct = '''<font color="green">Вірно</font>'''

frm = Form("Як буде яблоко по англійськи?", "apple", "application", "apricot", "banana")

radi_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radi_list)
frm_card = FormView(frm, lb_Question, radi_list[0], radi_list[1], radi_list[2], radi_list[3])
frm_edit = FormView(frm, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)

def check_result():
    correct = frm_card.answer.isChecked()

    if correct:
        lb_Result.setText(text_correct)
        lb_Correct.setText(frm_card.answer.text())
        show_result()
    else:
        incorrect = frm_card.wrong_answer1.isChecked() or frm_card.wrong_answer2.isChecked() or frm_card.wrong_answer3.isChecked()
        if incorrect:
            lb_Result.setText(text_wrong)
            lb_Correct.setText(frm_card.answer.text())
            show_result()

def click_OK(self):
    if btn_OK.text() != 'Наступне питання':
        check_result()

def show_card():
    wdgt_edit.hide()
    wdgt_card.show()

def show_form():
    wdgt_card.hide()
    wdgt_edit.show()

btn_card.clicked.connect(show_card)
btn_form.clicked.connect(show_form)
btn_OK.clicked.connect(click_OK)

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_main)
frm_card.show()
frm_edit.show()
show_question()
show_card()

win_card.show()
app.exec_()
