from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, sqlite3

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("static/ui/ui.ui", self)
        self.teacher.clicked.connect(self.signin_section_teacher)
        self.student.clicked.connect(self.signin_section_student)
        self.save_question.clicked.connect(self.add_question)
        self.both.clicked.connect(self.signin_section_both)
        self.none.clicked.connect(self.signin_section_none)
        self.signin.clicked.connect(self.signin_section)
        self.signup.clicked.connect(self.signup_section)
        self.create.clicked.connect(self.create_account)
        self.question.clicked.connect(self.new_question)
        self.enter.clicked.connect(self.enter_account)
        self.back.clicked.connect(self.home)
        self.back1.clicked.connect(self.home)
        self.back2.clicked.connect(self.home)

    def signin_section_teacher(self):
        global status
        status = "teacher"
        self.stackedWidget.setCurrentIndex(1)
    def signin_section_student(self):
        global status
        status = "student"
        self.stackedWidget.setCurrentIndex(1)
    def signin_section_both(self):
        global status
        status = "both"
        self.stackedWidget.setCurrentIndex(1)
    def signin_section_none(self):
        global status
        status = "none"
        self.stackedWidget.setCurrentIndex(1)
    def signin_section(self):
        self.stackedWidget.setCurrentIndex(1)
    def signup_section(self):
        self.stackedWidget.setCurrentIndex(2)
    def home(self):
        self.fill_all.clear()
        self.q_list.clear()
        self.label_16.clear()
        self.email_create.clear()
        self.username_enter.clear()
        self.password_enter.clear()
        self.username_create.clear()
        self.username_create.clear()
        self.stackedWidget.setCurrentIndex(0)
    def create_account(self):
        connection = sqlite3.connect("Database/user.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS User(Username text, Email text, Password text, Status text)''')
        cursor.execute('''INSERT INTO User VALUES(?, ?, ?, ?)''', (self.username_create.text(), self.email_create.text(), self.password_create.text(), status))
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(3)
    def enter_account(self):
        title = self.q_title.text()
        answer = self.q_answer.text()
        lesson = self.q_lesson.text()
        grade = self.q_grade.text()
        connection = sqlite3.connect("Database/question.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Question(Title text, answer text, lesson text, grade text)''')
        cursor.execute('''INSERT INTO Question VALUES(?, ?, ?, ?)''', (title, answer, lesson, grade))
        all_questions = cursor.execute('''SELECT Title FROM Question''')
        self.q_list.clear()
        for question in all_questions:
            self.q_list.addItem(question[0])

        self.stackedWidget.setCurrentIndex(3)
        connection.commit()
        connection.close()
        
        connection = sqlite3.connect("Database/user.db")
        cursor = connection.cursor()
        username = self.username_enter.text()
        password = self.password_enter.text()
        user_entered_container = (username, password, status)
        all_users = cursor.execute('''SELECT Username, Password, Status FROM USER''')
        for user in all_users:
            if (user == user_entered_container):
                self.stackedWidget.setCurrentIndex(3)
            else:
                self.label_16.setText("حساب یافت نشد")
    def new_question(self):
        self.q_title.clear()
        self.q_answer.clear()
        self.q_lesson.clear()
        self.q_grade.clear()
        self.stackedWidget.setCurrentIndex(4)

    def add_question(self):
        title = self.q_title.text()
        answer = self.q_answer.text()
        lesson = self.q_lesson.text()
        grade = self.q_grade.text()
        if (title != "" and answer != "" and lesson != "" and grade != ""):
            connection = sqlite3.connect("Database/question.db")
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Question(Title text, answer text, lesson text, grade text)''')
            cursor.execute('''INSERT INTO Question VALUES(?, ?, ?, ?)''', (title, answer, lesson, grade))
            all_questions = cursor.execute('''SELECT Title FROM Question''')
            self.q_list.clear()
            for question in all_questions:
                self.q_list.addItem(question[0])

            self.stackedWidget.setCurrentIndex(3)
            connection.commit()
            connection.close()
        else:
            self.fill_all.setText("تمامی موارد را پر کنید")

main = QApplication(sys.argv)
app = Main()
app.show()
main.exec_()
