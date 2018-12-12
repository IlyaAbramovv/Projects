import sys
import math
from math import cos, sin
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Калькулятор")
        MainWindow.resize(559, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 110, 201, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 1, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)
        self.btn_bcks = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_bcks.setObjectName("btn_bcks")
        self.gridLayout.addWidget(self.btn_bcks, 0, 0, 1, 2)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 1, 2, 1, 1)
        self.btn_unarminus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_unarminus.setObjectName("btn_unarminus")
        self.gridLayout.addWidget(self.btn_unarminus, 0, 3, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 1, 3, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 4, 3, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 2)
        self.btn_mult = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 3, 3, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_sqr = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sqr.setObjectName("btn_sqr")
        self.gridLayout.addWidget(self.btn_sqr, 2, 4, 1, 1)
        self.btn_com = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_com.setObjectName("btn_com")
        self.gridLayout.addWidget(self.btn_com, 4, 2, 1, 1)
        self.btn_reverse = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_reverse.setObjectName("btn_reverse")
        self.gridLayout.addWidget(self.btn_reverse, 3, 4, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 2, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 1, 4, 1, 1)
        self.btn_sqrt_y = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sqrt_y.setObjectName("btn_sqrt_y")
        self.gridLayout.addWidget(self.btn_sqrt_y, 0, 4, 1, 1)
        self.btn_equals = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_equals.setObjectName("btn_equals")
        self.gridLayout.addWidget(self.btn_equals, 4, 4, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 110, 201, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_cos = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_cos.setObjectName("btn_cos")
        self.gridLayout_3.addWidget(self.btn_cos, 1, 1, 1, 1)
        self.btn_sin = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_sin.setObjectName("btn_sin")
        self.gridLayout_3.addWidget(self.btn_sin, 2, 1, 1, 1)
        self.btn_int = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_int.setObjectName("btn_int")
        self.gridLayout_3.addWidget(self.btn_int, 3, 0, 1, 1)
        self.btn_tay = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_tay.setObjectName("btn_tay")
        self.gridLayout_3.addWidget(self.btn_tay, 2, 0, 1, 1)
        self.btn_ctg = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_ctg.setObjectName("btn_ctg")
        self.gridLayout_3.addWidget(self.btn_ctg, 4, 1, 1, 1)
        self.btn_arccos = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_arccos.setObjectName("btn_arccos")
        self.gridLayout_3.addWidget(self.btn_arccos, 1, 2, 1, 1)
        self.btn_pi = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.btn_pi.setFont(font)
        self.btn_tay.setFont(font)
        self.btn_pi.setObjectName("btn_pi")
        self.gridLayout_3.addWidget(self.btn_pi, 0, 1, 1, 1)
        self.btn_e = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_e.setObjectName("btn_e")
        self.gridLayout_3.addWidget(self.btn_e, 1, 0, 1, 1)
        self.btn_arctg = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_arctg.setObjectName("btn_arctg")
        self.gridLayout_3.addWidget(self.btn_arctg, 3, 2, 1, 1)
        self.btn_arcsin = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_arcsin.setObjectName("btn_arcsin")
        self.gridLayout_3.addWidget(self.btn_arcsin, 2, 2, 1, 1)
        self.btn_arcctg = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_arcctg.setObjectName("btn_arcctg")
        self.gridLayout_3.addWidget(self.btn_arcctg, 4, 2, 1, 1)
        self.btn_fkt = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_fkt.setObjectName("btn_fkt")
        self.gridLayout_3.addWidget(self.btn_fkt, 0, 2, 1, 1)
        self.btn_tg = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_tg.setObjectName("btn_tg")
        self.gridLayout_3.addWidget(self.btn_tg, 3, 1, 1, 1)
        self.btn_log = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_log.setObjectName("btn_log")
        self.gridLayout_3.addWidget(self.btn_log, 4, 0, 1, 1)
        self.btn_sqr_y = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_sqr_y.setObjectName("btn_sqr_y")
        self.gridLayout_3.addWidget(self.btn_sqr_y, 0, 0, 1, 1)
        self.LCD_result = QtWidgets.QLineEdit('0', self.centralwidget)
        self.LCD_result.setGeometry(QtCore.QRect(80, 70, 411, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(25)
        font.setPixelSize(25)
        self.LCD_result.setFont(font)
        self.LCD_result.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.LCD_result.setAutoFillBackground(False)
        self.LCD_result.setReadOnly(True)
        self.LCD_result.setObjectName("LCD_result")
        self.LCD_result.setAlignment(Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.rbtn_radians = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_radians.setGeometry(QtCore.QRect(150, 310, 70, 20))
        self.rbtn_radians.setObjectName("rbtn_radians")
        self.rbtn_grads = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_grads.setGeometry(QtCore.QRect(80, 310, 70, 20))
        self.rbtn_grads.setObjectName("rbtn_grads")
        self.btn_memory = QtWidgets.QPushButton(self)
        self.btn_memory.setObjectName("btn_memory")
        self.btn_memory.setGeometry(QtCore.QRect(290, 310, 77, 20))
        self.btn_memory_clear = QtWidgets.QPushButton(self)
        self.btn_memory.setObjectName("btn_memory_clear")
        self.btn_memory_clear.setGeometry(QtCore.QRect(373, 310, 77, 20))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_bcks.setText(_translate("MainWindow", "<----"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_unarminus.setText(_translate("MainWindow", "\u00B1"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_sqr.setText(_translate("MainWindow", "x^2"))
        self.btn_com.setText(_translate("MainWindow", ","))
        self.btn_reverse.setText(_translate("MainWindow", "1/x"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_sqrt.setText(_translate("MainWindow", "√"))
        self.btn_sqrt_y.setText(_translate("MainWindow", "\u221an"))
        self.btn_equals.setText(_translate("MainWindow", "="))
        self.btn_cos.setText(_translate("MainWindow", "cos"))
        self.btn_sin.setText(_translate("MainWindow", "sin"))
        self.btn_int.setText(_translate("MainWindow", "Int"))
        self.btn_tay.setText(_translate("MainWindow", "\u03C4"))
        self.btn_ctg.setText(_translate("MainWindow", "ctg"))
        self.btn_arccos.setText(_translate("MainWindow", "cos^-1"))
        self.btn_pi.setText(_translate("MainWindow", "π "))
        self.btn_e.setText(_translate("MainWindow", "e"))
        self.btn_arctg.setText(_translate("MainWindow", "tg^-1"))
        self.btn_arcsin.setText(_translate("MainWindow", "sin^-1"))
        self.btn_arcctg.setText(_translate("MainWindow", "ctg^-1"))
        self.btn_fkt.setText(_translate("MainWindow", "n!"))
        self.btn_tg.setText(_translate("MainWindow", "tg"))
        self.btn_log.setText(_translate("MainWindow", "ln"))
        self.btn_sqr_y.setText(_translate("MainWindow", "x^y"))
        self.rbtn_radians.setText(_translate("MainWindow", "Радианы"))
        self.rbtn_grads.setText(_translate("MainWindow", "Градусы"))
        self.btn_memory.setText(_translate("MainWindow", "M"))
        self.btn_memory_clear.setText(_translate("MainWindow", "MC"))


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.stack = [0, 0]
        self.showed_number = ''
        self.root_flag = False
        self.degrees_radians = 'radians'
        self.rbtn_radians.toggle()
        self.keyboard_number_flag = False
        self.keyboard_operator_flag = False
        self.memory_input_flag = False
        self.memory = ''

        for i in range(10):
            getattr(self, 'btn_{}'.format(str(i))).clicked.connect(self.numbers)
            # Вызов функции self.numbers при проходе по списку чисел

        self.btn_clear.clicked.connect(self.do_clear)

        self.btn_bcks.clicked.connect(self.do_backspace)

        self.btn_com.clicked.connect(self.do_com)

        self.btn_plus.clicked.connect(self.do_operation)
        self.btn_minus.clicked.connect(self.do_operation)
        self.btn_mult.clicked.connect(self.do_operation)
        self.btn_div.clicked.connect(self.do_operation)

        self.btn_unarminus.clicked.connect(self.do_unarminus)

        self.btn_reverse.clicked.connect(self.do_reverse)

        self.btn_sqr.clicked.connect(self.do_sqr)

        self.btn_sqrt.clicked.connect(self.do_sqrt)

        self.btn_equals.clicked.connect(self.do_equals)

        self.btn_pi.clicked.connect(self.do_pi)

        self.btn_fkt.clicked.connect(self.do_fkt)

        self.btn_cos.clicked.connect(self.do_simple_trig_operation)
        self.btn_sin.clicked.connect(self.do_simple_trig_operation)

        self.btn_tg.clicked.connect(self.do_tg)
        self.btn_ctg.clicked.connect(self.do_ctg)

        self.btn_arcsin.clicked.connect(self.do_arcsin)
        self.btn_arccos.clicked.connect(self.do_arccos)

        self.btn_arctg.clicked.connect(self.do_arctg)
        self.btn_arcctg.clicked.connect(self.do_arcctg)

        self.btn_sqr_y.clicked.connect(self.do_sqr_y)

        self.btn_sqrt_y.clicked.connect(self.do_sqrt_y)

        self.btn_tay.clicked.connect(self.do_tay)

        self.btn_e.clicked.connect(self.do_e)

        self.btn_int.clicked.connect(self.do_int)

        self.btn_log.clicked.connect(self.do_log)

        self.rbtn_grads.clicked.connect(self.changetrig)
        self.rbtn_radians.clicked.connect(self.changetrig)

        self.btn_memory.clicked.connect(self.memory_add)
        self.btn_memory_clear.clicked.connect(self.memory_clear)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.do_equals()

        elif event.key() == Qt.Key_Backspace:
            self.do_backspace()

        elif event.key() == Qt.Key_Comma:
            self.do_com()

        for i in range(10):
            if event.key() == getattr(Qt, 'Key_{}'.format(str(i))):
                self.keyboard_number_flag = True
                self.numbers(str(i))
        for i in ['Plus+', 'Minus-', 'multiply*', 'Slash/']: #!!!!!!!!!!!!!!
            if event.key() == getattr(Qt, 'Key_{}'.format(i[:-1])):
                self.keyboard_operator_flag = True
                self.do_operation(i[-1])

    def memory_add(self):
        if bool(self.showed_number) and not self.memory_input_flag:
            self.memory = self.showed_number
            self.memory_input_flag = True

        elif bool(self.stack[1]) and bool(self.stack[0]) and not self.memory_input_flag:
            self.memory = self.stack[1]
            self.memory_input_flag = True

        elif self.memory_input_flag:
            self.showed_number = self.memory
            self.display()

    def memory_clear(self):
        if self.memory_input_flag:
            self.memory = ''
            self.memory_input_flag = False

    def display(self):  # Выводит в виджет текущее число
        self.LCD_result.setText(self.showed_number)

    def changetrig(self):
        if self.rbtn_grads.isChecked():
            self.degrees_radians = 'degrees'
        elif self.rbtn_radians.isChecked():
            self.degrees_radians = 'radians'


    def error(self):
        self.showed_number = ''
        self.stack = [0, 0]
        self.LCD_result.setText('Ошибка')

    def do_log(self):
        try:
            self.showed_number = str(math.log(float(self.showed_number)))
            self.display()
        except Exception:
            self.error()

    def do_int(self):
        self.showed_number = str(round(float(self.showed_number)))
        self.display()

    def do_e(self):
        self.showed_number = '2.7182818284'
        self.display()

    def do_tay(self):
        self.showed_number = str(3.14159265 * 2)
        self.display()

    def do_sqrt_y(self):
        if not bool(self.stack[1]):
            self.stack[1] = self.showed_number
            self.stack[0] = '**'
            self.showed_number = ''
            self.root_flag = True
        else:
            self.stack[1] = str(eval('{} {} (1/{})'.format(self.stack[1], self.stack[0], self.showed_number)))
            self.stack[0] = '**'
            self.showed_number = ''

    def do_sqr_y(self):
        if not bool(self.stack[1]):
            self.stack[1] = self.showed_number
            self.stack[0] = '**'
            self.showed_number = ''
        else:
            self.stack[1] = str(eval('{} {} {}'.format(self.stack[1], self.stack[0], self.showed_number)))
            self.stack[0] = '**'
            self.showed_number = ''

    def do_arcctg(self):
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(1 / math.atan(float(self.showed_number)))
            else:
                self.showed_number = str(1 / math.atan(math.degrees(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_arctg(self):
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.atan(float(self.showed_number)))
            else:
                self.showed_number = str(math.atan(math.degrees(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_arccos(self):
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.acos(float(self.showed_number)))
            else:
                self.showed_number = str(math.acos(math.degrees(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_arcsin(self):
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.asin(float(self.showed_number)))
            else:
                self.showed_number = str(math.asin(math.degrees(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_tg(self):
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.tan(float(self.showed_number)))
            else:
                self.showed_number = str(math.tan(math.degrees(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_ctg(self):
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(1 / math.tan(float(self.showed_number)))
            else:
                self.showed_number = str(1 / math.tan(math.degrees(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_simple_trig_operation(self):
        sender = self.sender()
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(eval(sender.text() + '(' + self.showed_number + ')'))
            else:
                self.showed_number = str(math.degrees(float(self.showed_number)))
                self.showed_number = str(eval(sender.text() + '(' + self.showed_number + ')'))
            self.display()
        except Exception:
            self.error()

    def do_fkt(self):
        try:
            self.showed_number = str(math.factorial(int(self.showed_number)))
            self.display()
        except Exception:
            self.error()

    def do_pi(self):
        self.showed_number = '3.14159265'
        self.display()

    def do_sqrt(self):
        if bool(self.showed_number):
            if float(self.showed_number) >= 0:
                self.showed_number = str(float(self.showed_number) ** 0.5)
                self.display()
            else:
                self.error()

    def do_sqr(self):
        if bool(self.showed_number):
            self.showed_number = str(float(self.showed_number) ** 2)
            self.display()

    def do_reverse(self):
        if bool(self.showed_number):
            self.showed_number = str(1 / float(self.showed_number.rstrip('.')))
            self.display()

    def do_com(self):
        if '.' not in self.showed_number:
            self.showed_number += '.'
            self.display()

    def numbers(self, number):
        if self.keyboard_number_flag:
            if number == '0' and self.showed_number == '0':
                pass
            else:
                self.showed_number += number
                self.display()
            self.keyboard_number_flag = False
        else:
            sender = self.sender()

            if sender.text() == '0' and self.showed_number == '0':
                pass
            else:
                self.showed_number += sender.text()
                self.display()

    def do_clear(self):
        self.showed_number = ''
        self.LCD_result.setText('0')
        self.stack = [0, 0, 0]

    def do_backspace(self):
        if self.showed_number != ('0' and ''):
            if len(self.showed_number) == 2 and self.showed_number[0] == '-' or len(self.showed_number) == 1:
                self.showed_number = ''
                self.LCD_result.setText('0')
            else:
                self.showed_number = self.showed_number[:-1]
                self.display()

    def do_operation(self, operator):
        try:
            if self.keyboard_operator_flag:
                if not bool(self.stack[1]):
                    self.stack[1] = self.showed_number
                    self.stack[0] = operator
                    self.showed_number = ''
                else:
                    self.stack[1] = str(eval('{} {} {}'.format(self.stack[1], self.stack[0], self.showed_number)))
                    self.stack[0] = operator
                    self.showed_number = ''
                self.keyboard_operator_flag = False
            else:
                sender = self.sender()
                if not bool(self.stack[1]):
                    self.stack[1] = self.showed_number
                    self.stack[0] = sender.text()
                    self.showed_number = ''
                else:
                    self.stack[1] = str(eval('{} {} {}'.format(self.stack[1], self.stack[0], self.showed_number)))
                    self.stack[0] = sender.text()
                    self.showed_number = ''
        except Exception:
            self.error()

    def do_unarminus(self):
        if bool(self.showed_number) and self.showed_number != ('0' or '0.0'):
            if self.showed_number[0] == '-':
                self.showed_number = self.showed_number.replace('-', '')
            else:
                self.showed_number = '-' + self.showed_number
            self.display()

    def do_equals(self):
        try:
            if bool(self.showed_number):
                if bool(self.stack[1]):
                    if self.root_flag:
                        to_show = str(eval('{} {} (1/{})'.format(self.stack[1], self.stack[0], self.showed_number)))
                        if to_show == ('-0' or '-0.0'):
                            to_show = '0'
                        self.LCD_result.setText(to_show)
                        self.stack = [0, 0]
                        self.showed_number = to_show
                        self.root_flag = False
                    else:
                        to_show = str(eval('{} {} {}'.format(self.stack[1], self.stack[0], self.showed_number)))
                        if to_show == ('-0' or '-0.0'):
                            to_show = '0'
                        self.LCD_result.setText(to_show)
                        self.stack = [0, 0]
                        self.showed_number = to_show
        except Exception:
            self.error()


app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec_())
