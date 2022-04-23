from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)

app=QApplication([])
main_win = QWidget()

class Question():
        def __init__(self,question, right_answer, wrong1,wrong2,wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

q1=Question("In what year was the great fire of London?", "1666", "1999", "1062", "666")
q2=Question("In what year was Moscow founded?", "1047", "1666", "147", "2012")
q3=Question("What is the powerhouse of the cell?", "mytochondria", "heart", "nucleus", "oven")
q4=Question("What is Force divided by mass?", "acceleration", "distance", "power", "speed")
q5=Question("What is the integral of sin(x)?", "-cos(x)", "tan(x)", "cos(x)", "-sin(x)")


q_list = [q1,q2,q3,q4,q5]

def next_qst():
        if len(q_list):
                shuffle(q_list)
                main_win.counter = main_win.counter + 1
                if main_win.counter >= len(q_list):
                        main_win.counter = 0
                q = q_list[main_win.counter]
                ask(q)
                q_list.remove(q)
        else:   
                label2.setText("There aren't anymore questions")
                but1.setText("Quit")


def show_ans():
        questionbox.hide()
        answerbox.show()
        but1.setText("Next question")
        if b_list[0].isChecked():
                label2.setText("Correct!")
        else:
                label2.setText("Incorrect. The correct answer was:")
                main_win.wrong += 1
        label4.setText("Correct answers: " + str(main_win.correct))
        label5.setText("User rating: " + str(rating) + " %")

def show_qst():
        questionbox.show()
        answerbox.hide()
        but1.setText("Answer")
        RadioGroup.setExclusive(False)
        b1.setChecked(False)
        b2.setChecked(False)
        b3.setChecked(False)
        b4.setChecked(False)
        RadioGroup.setExclusive(True)

def test():
        if but1.text() == "Quit":
                quit()
        elif but1.text() == "Answer":
                show_ans()
        else:
                next_qst()



def ask(q : Question):
        shuffle(b_list)
        label1.setText(q.question)
        b_list[0].setText(q.right_answer)
        b_list[1].setText(q.wrong1)
        b_list[2].setText(q.wrong2) 
        b_list[3].setText(q.wrong3) 
        label3.setText(q.right_answer)
        show_qst()


questionbox = QGroupBox("Answer options:")
answerbox = QGroupBox("Test Result :")

label2 = QLabel('Are you correct or not?')
label3 = QLabel('The answer will be here!')

vline1.addWidget(label4)
vline1.addWidget(label5)
vline4 = QVBoxLayout()
vline4.addWidget(label2)
vline4.addWidget(label3)
answerbox.setLayout(vline4)

main_win.setWindowTitle('Memory card')
main_win.counter = -1

label1 = QLabel('Which nationality does not exist?')
b1=QRadioButton("Enets")
b2=QRadioButton("Chulyms")
b3=QRadioButton("Smurfs")
b4=QRadioButton("Aleuts")
but1 = QPushButton("Answer")

b_list=[b1,b2,b3,b4]
RadioGroup=QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
vline3 = QVBoxLayout()

hline1 = QHBoxLayout()

vline1.addWidget(label1)
vline1.addWidget(questionbox)
vline1.addWidget(answerbox)
vline1.addWidget(but1)

vline2.addWidget(b1)
vline2.addWidget(b2)
vline3.addWidget(b3)
vline3.addWidget(b4)

hline1.addLayout(vline2)
hline1.addLayout(vline3)
questionbox.setLayout(hline1)

next_qst
but1.clicked.connect(test)
main_win.setLayout(vline1)
answerbox.hide()
main_win.show()
app.exec()

