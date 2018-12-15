import sys
import math
from math import cos, sin
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 405)
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
        self.btn_6.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName("btn_4")
        self.btn_4.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName("btn_2")
        self.btn_2.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_2, 1, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName("btn_5")
        self.btn_5.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName("btn_7")
        self.btn_7.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName("btn_8")
        self.btn_8.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName("btn_1")
        self.btn_1.setStyleSheet(
            "background-color: grey")        
        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)
        self.btn_bcks = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_bcks.setObjectName("btn_bcks")
        self.btn_bcks.setStyleSheet(
            "background-color: lightgrey")          
        self.gridLayout.addWidget(self.btn_bcks, 0, 0, 1, 2)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName("btn_3")
        self.btn_3.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_3, 1, 2, 1, 1)
        self.btn_unarminus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_unarminus.setObjectName("btn_unarminus")
        self.btn_unarminus.setStyleSheet(
            "background-color: lightgrey")           
        self.gridLayout.addWidget(self.btn_unarminus, 0, 3, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_plus.setStyleSheet(
            "background-color: orange")
        self.gridLayout.addWidget(self.btn_plus, 1, 3, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_div.setObjectName("btn_div")
        self.btn_div.setStyleSheet(
            "background-color: orange")        
        self.gridLayout.addWidget(self.btn_div, 4, 3, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName("btn_9")
        self.btn_9.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName("btn_0")
        self.btn_0.setStyleSheet(
            "background-color: grey")            
        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 2)
        self.btn_mult = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_mult.setObjectName("btn_mult")
        self.btn_mult.setStyleSheet(
            "background-color: orange")        
        self.gridLayout.addWidget(self.btn_mult, 3, 3, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_minus.setStyleSheet(
            "background-color: orange")        
        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_sqr = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sqr.setObjectName("btn_sqr")
        self.btn_sqr.setStyleSheet(
            "background-color: peru")          
        self.gridLayout.addWidget(self.btn_sqr, 2, 4, 1, 1)
        self.btn_com = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_com.setObjectName("btn_com")
        self.btn_com.setStyleSheet(
            "background-color: grey")             
        self.gridLayout.addWidget(self.btn_com, 4, 2, 1, 1)
        self.btn_reverse = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_reverse.setObjectName("btn_reverse")
        self.btn_reverse.setStyleSheet(
            "background-color: peru")             
        self.gridLayout.addWidget(self.btn_reverse, 3, 4, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setObjectName("btn_clear")
        self.btn_clear.setStyleSheet(
            "background-color: lightgrey")          
        self.gridLayout.addWidget(self.btn_clear, 0, 2, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.btn_sqrt.setStyleSheet(
            "background-color: peru")          
        self.gridLayout.addWidget(self.btn_sqrt, 1, 4, 1, 1)
        self.btn_sqrt_y = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sqrt_y.setObjectName("btn_sqrt_y")
        self.btn_sqrt_y.setStyleSheet(
            "background-color: peru")          
        self.gridLayout.addWidget(self.btn_sqrt_y, 0, 4, 1, 1)
        self.btn_equals = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_equals.setObjectName("btn_equals")
        self.btn_equals.setStyleSheet(
            "background-color: peru")             
        self.gridLayout.addWidget(self.btn_equals, 4, 4, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 110, 201, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_cos = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_cos.setObjectName("btn_cos")
        self.btn_cos.setStyleSheet(
            "background-color: darksalmon")           
        self.gridLayout_3.addWidget(self.btn_cos, 1, 1, 1, 1)
        self.btn_sin = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_sin.setObjectName("btn_sin")
        self.btn_sin.setStyleSheet(
            "background-color: darksalmon")            
        self.gridLayout_3.addWidget(self.btn_sin, 2, 1, 1, 1)
        self.btn_int = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_int.setObjectName("btn_int")
        self.btn_int.setStyleSheet(
            "background-color: tomato")           
        self.gridLayout_3.addWidget(self.btn_int, 3, 0, 1, 1)
        self.btn_tay = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_tay.setObjectName("btn_tay")
        self.btn_tay.setStyleSheet(
            "background-color: coral")           
        self.gridLayout_3.addWidget(self.btn_tay, 2, 0, 1, 1)
        self.btn_ctg = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_ctg.setObjectName("btn_ctg")
        self.btn_ctg.setStyleSheet(
            "background-color: darksalmon")           
        self.gridLayout_3.addWidget(self.btn_ctg, 4, 2, 1, 1)
        self.btn_arccos = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_arccos.setObjectName("btn_arccos")
        self.btn_arccos.setStyleSheet(
            "background-color: darksalmon")           
        self.gridLayout_3.addWidget(self.btn_arccos, 1, 2, 1, 1)
        self.btn_pi = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.btn_pi.setFont(font)
        self.btn_tay.setFont(font)
        self.btn_pi.setObjectName("btn_pi")
        self.btn_pi.setStyleSheet(
            "background-color: coral")           
        self.gridLayout_3.addWidget(self.btn_pi, 0, 0, 1, 1)
        self.btn_e = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_e.setObjectName("btn_e")
        self.btn_e.setStyleSheet(
            "background-color: coral")           
        self.gridLayout_3.addWidget(self.btn_e, 1, 0, 1, 1)
        self.btn_arctg = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_arctg.setObjectName("btn_arctg")
        self.btn_arctg.setStyleSheet(
            "background-color: darksalmon")           
        self.gridLayout_3.addWidget(self.btn_arctg, 3, 2, 1, 1)
        self.btn_arcsin = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_arcsin.setObjectName("btn_arcsin")
        self.btn_arcsin.setStyleSheet(
            "background-color: darksalmon")               
        self.gridLayout_3.addWidget(self.btn_arcsin, 2, 2, 1, 1)
        self.btn_log = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_log.setObjectName("btn_log")
        self.btn_log.setStyleSheet(
            "background-color: tomato")
        self.gridLayout_3.addWidget(self.btn_log, 4, 1, 1, 1)
        self.btn_fkt = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_fkt.setObjectName("btn_fkt")
        self.btn_fkt.setStyleSheet(
            "background-color: lightgrey")
        self.gridLayout_3.addWidget(self.btn_fkt, 0, 2, 1, 1)
        self.btn_tg = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_tg.setObjectName("btn_tg")
        self.btn_tg.setStyleSheet(
            "background-color: darksalmon")           
        self.gridLayout_3.addWidget(self.btn_tg, 3, 1, 1, 1)
        self.btn_logn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_logn.setObjectName("btn_logn")
        self.btn_logn.setStyleSheet(
            "background-color: tomato")           
        self.gridLayout_3.addWidget(self.btn_logn, 4, 0, 1, 1)
        self.btn_sqr_y = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_sqr_y.setObjectName("btn_sqr_y")
        self.btn_sqr_y.setStyleSheet(
            "background-color: lightgrey")           
        self.gridLayout_3.addWidget(self.btn_sqr_y, 0, 1, 1, 1)
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
        self.btn_memory.setStyleSheet(
            "background-color: rosybrown")               
        self.btn_memory_clear = QtWidgets.QPushButton(self)
        self.btn_memory.setObjectName("btn_memory_clear")
        self.btn_memory_clear.setGeometry(QtCore.QRect(373, 310, 77, 20))
        self.btn_memory_clear.setStyleSheet(
            "background-color: rosybrown")

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
        self.btn_sqrt.setText(_translate("MainWindow", "\u221a"))
        self.btn_sqrt_y.setText(_translate("MainWindow", "\u221an"))
        self.btn_equals.setText(_translate("MainWindow", "="))
        self.btn_cos.setText(_translate("MainWindow", "cos"))
        self.btn_sin.setText(_translate("MainWindow", "sin"))
        self.btn_int.setText(_translate("MainWindow", "Int"))
        self.btn_tay.setText(_translate("MainWindow", "\u03C4"))
        self.btn_ctg.setText(_translate("MainWindow", "ctg"))
        self.btn_arccos.setText(_translate("MainWindow", "cos^-1"))
        self.btn_pi.setText(_translate("MainWindow", "\u03c0"))
        self.btn_e.setText(_translate("MainWindow", "e"))
        self.btn_arctg.setText(_translate("MainWindow", "tg^-1"))
        self.btn_arcsin.setText(_translate("MainWindow", "sin^-1"))
        self.btn_log.setText(_translate("MainWindow", "log10"))
        self.btn_fkt.setText(_translate("MainWindow", "n!"))
        self.btn_tg.setText(_translate("MainWindow", "tg"))
        self.btn_logn.setText(_translate("MainWindow", "ln"))
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
        self.btn_log.clicked.connect(self.do_log)

        self.btn_sqr_y.clicked.connect(self.do_sqr_y)

        self.btn_sqrt_y.clicked.connect(self.do_sqrt_y)

        self.btn_tay.clicked.connect(self.do_tay)

        self.btn_e.clicked.connect(self.do_e)

        self.btn_int.clicked.connect(self.do_int)

        self.btn_logn.clicked.connect(self.do_logn)

        self.rbtn_grads.clicked.connect(self.changetrig)
        self.rbtn_radians.clicked.connect(self.changetrig)

        self.btn_memory.clicked.connect(self.memory_add)
        self.btn_memory_clear.clicked.connect(self.memory_clear)

    def keyPressEvent(self, event):  # Блок обработки нажатий с клавиатуры
        if event.key() == Qt.Key_Enter:
            self.do_equals()

        elif event.key() == Qt.Key_Backspace:
            self.do_backspace()

        elif event.key() == Qt.Key_Comma:
            self.do_com()
            
        elif str(event.key()) == '42':
            self.keyboard_operator_flag = True
            self.do_operation('*')
        

        for i in range(10):
            if event.key() == getattr(Qt, 'Key_{}'.format(str(i))):
                self.keyboard_number_flag = True
                self.numbers(str(i))
        for i in ['Plus+', 'Minus-', 'Slash/']:
            
            if event.key() == getattr(Qt, 'Key_{}'.format(i[:-1])):
                self.keyboard_operator_flag = True
                self.do_operation(i[-1])

    def memory_add(self):  # Добавление соществующего числа в память или его вывод
        if bool(self.showed_number) and not self.memory_input_flag:
            self.memory = self.showed_number
            self.memory_input_flag = True

        elif bool(self.stack[1]) and bool(self.stack[0]) and not self.memory_input_flag:
            self.memory = self.stack[1]
            self.memory_input_flag = True

        elif self.memory_input_flag:
            self.showed_number = self.memory
            self.display()

    def memory_clear(self):  # Очистка памяти
        if self.memory_input_flag:
            self.memory = ''
            self.memory_input_flag = False

    def display(self):  # Выводит в виджет текущее число
        self.LCD_result.setText(self.showed_number)

    def changetrig(self):  # Смена радиан на градусы и наооборот
        if self.rbtn_grads.isChecked():
            self.degrees_radians = 'degrees'
        elif self.rbtn_radians.isChecked():
            self.degrees_radians = 'radians'

    def error(self):  # Вывод ошибки
        self.showed_number = ''
        self.stack = [0, 0]
        self.LCD_result.setText('Ошибка')

    def do_logn(self):  # Блок обработки натурального логарифма
        try:
            self.showed_number = str(math.log(float(self.showed_number)))
            self.display()
        except Exception:
            self.error()

    def do_int(self):   # Целая часть от числа
        self.showed_number = str(int(float(self.showed_number)))
        self.display()

    def do_e(self):     # Вывод на экран константы числа Эйлера
        self.showed_number = '2.7182818284'
        self.display()

    def do_tay(self):   # Вывод на экран константы тау
        self.showed_number = str(3.14159265 * 2)
        self.display()

    def do_sqrt_y(self):    # Блок обработки корня n-ой стеепени для данного числа
        if not bool(self.stack[1]):
            self.stack[1] = self.showed_number
            self.stack[0] = '**'
            self.showed_number = ''
            self.root_flag = True
        else:
            self.stack[1] = str(eval('{} {} (1/{})'.format(self.stack[1], self.stack[0], self.showed_number)))
            self.stack[0] = '**'
            self.showed_number = ''

    def do_sqr_y(self):    # Блок обработки n-ой степени для данного числа
        if not bool(self.stack[1]):
            self.stack[1] = self.showed_number
            self.stack[0] = '**'
            self.showed_number = ''
        else:
            self.stack[1] = str(eval('{} {} {}'.format(self.stack[1], self.stack[0], self.showed_number)))
            self.stack[0] = '**'
            self.showed_number = ''

    def do_log(self):   # Блок обработки логарифма по основанию 10 для данного числа
        try:
            self.showed_number = str(math.log10(float(self.showed_number)))
            self.display()
        except Exception:
            self.error()

    def do_arctg(self):    # Блок обработки арктангенса данного числа
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.atan(float(self.showed_number)))
            else:
                self.showed_number = str(math.atan(math.radians(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_arccos(self):    # Блок обработки арккосинуса данного числа
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.acos(float(self.showed_number)))
            else:
                self.showed_number = str(math.acos(math.radians(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_arcsin(self):    # Блок обработки арксинуса данного числа
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.asin(float(self.showed_number)))
            else:
                self.showed_number = str(math.asin(math.radians(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_tg(self):    # Блок обработки тангенса данного числа
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(math.tan(float(self.showed_number)))
            else:
                self.showed_number = str(math.tan(math.radians(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_ctg(self):    # Блок обработки котангенса данного числа
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(1 / math.tan(float(self.showed_number)))
            else:
                self.showed_number = str(1 / math.tan(math.radians(float(self.showed_number))))
            self.display()
        except Exception:
            self.error()

    def do_simple_trig_operation(self):    # Блок обработки синуса и косинуса данного числа
        sender = self.sender()
        try:
            if self.degrees_radians == 'radians':
                self.showed_number = str(eval(sender.text() + '(' + self.showed_number + ')'))
            else:
                self.showed_number = str(math.radians(float(self.showed_number)))
                self.showed_number = str(eval(sender.text() + '(' + self.showed_number + ')'))
            self.display()
        except Exception:
            self.error()

    def do_fkt(self):    # Вывод факториала данного числа
        try:
            self.showed_number = str(math.factorial(int(self.showed_number)))
            self.display()
        except Exception:
            self.error()

    def do_pi(self):    # Вывод константы числа пи
        self.showed_number = '3.14159265'
        self.display()

    def do_sqrt(self):    # Блок обработки арифметического квадратного корня данного числа
        if bool(self.showed_number):
            if float(self.showed_number) >= 0:
                self.showed_number = str(float(self.showed_number) ** 0.5)
                self.display()
            else:
                self.error()

    def do_sqr(self):    # Блок обработки квадрата данного числа
        if bool(self.showed_number):
            self.showed_number = str(float(self.showed_number) ** 2)
            self.display()

    def do_reverse(self):    # Вывод числа, обратного данному
        if bool(self.showed_number):
            self.showed_number = str(1 / float(self.showed_number.rstrip('.')))
            self.display()

    def do_com(self):    # Преобразовать число в десятичную дробь
        if '.' not in self.showed_number:
            self.showed_number += '.'
            self.display()

    def numbers(self, number):    # Блок обработки нажатий цифр
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

    def do_clear(self):     # Очиска поля вывода
        self.showed_number = ''
        self.LCD_result.setText('0')
        self.stack = [0, 0, 0]

    def do_backspace(self):   # Удалить последний знак данного числа
        if self.showed_number != ('0' and ''):
            if len(self.showed_number) == 2 and self.showed_number[0] == '-' or len(self.showed_number) == 1:
                self.showed_number = ''
                self.LCD_result.setText('0')
            else:
                self.showed_number = self.showed_number[:-1]
                self.display()

    def do_operation(self, operator):     # Блок обработки простых арифметических действий
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

    def do_unarminus(self):     # Сделать число отрицательным/положительным
        if bool(self.showed_number) and self.showed_number != ('0' or '0.0'):
            if self.showed_number[0] == '-':
                self.showed_number = self.showed_number.replace('-', '')
            else:
                self.showed_number = '-' + self.showed_number
            self.display()

    def do_equals(self):    # Вывести получившееся число
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
