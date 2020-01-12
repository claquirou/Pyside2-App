from PySide2 import QtWidgets, QtGui, QtCore
from functools import partial


class MainWindow(QtWidgets.QWidget):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.modify_widgets()
        self.setup_connections()
        self.setupShortcut()

    def create_widgets(self):
        self.le_result = QtWidgets.QLineEdit("")

        self.btn_c = QtWidgets.QPushButton("C")
        self.btn_bracket1 = QtWidgets.QPushButton("(")
        self.btn_bracket2 = QtWidgets.QPushButton(")")

        self.btn_div = QtWidgets.QPushButton("/")
        self.btn_plus = QtWidgets.QPushButton("+")
        self.btn_moins = QtWidgets.QPushButton("-")
        self.btn_multi = QtWidgets.QPushButton("*")
        self.btn_point = QtWidgets.QPushButton(".")
        self.btn_egale = QtWidgets.QPushButton("=")

        self.btn_1 = QtWidgets.QPushButton("1")
        self.btn_2 = QtWidgets.QPushButton("2")
        self.btn_3 = QtWidgets.QPushButton("3")
        self.btn_4 = QtWidgets.QPushButton("4")
        self.btn_5 = QtWidgets.QPushButton("5")
        self.btn_6 = QtWidgets.QPushButton("6")
        self.btn_7 = QtWidgets.QPushButton("7")
        self.btn_8 = QtWidgets.QPushButton("8")
        self.btn_9 = QtWidgets.QPushButton("9")
        self.btn_0 = QtWidgets.QPushButton("0")
        self.btn_00 = QtWidgets.QPushButton("00")

    def modify_widgets(self):

        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

        font = QtGui.QFont()
        font.setBold(True)

        self.le_result.setText("0")
        self.le_result.setReadOnly(True)
        self.le_result.setFixedHeight(40)
        self.le_result.setFont(font)
        self.le_result.setAlignment(QtCore.Qt.AlignRight)
        self.le_result.setFrame(False)

        self.main_layout.setSpacing(0)
        # self.main_layout.setContentsMargins(0, 0, 0, 0)

        for btn in self.get_button:
            btn.setMinimumSize(30, 50)
            btn.setFlat(True)
            btn.setFont(font)

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.le_result, 0, 1, 1, 4)

        self.main_layout.addWidget(self.btn_c, 1, 1, 1, 1)
        self.main_layout.addWidget(self.btn_bracket1, 1, 2, 1, 1)
        self.main_layout.addWidget(self.btn_bracket2, 1, 3, 1, 1)
        self.main_layout.addWidget(self.btn_div, 1, 4, 1, 1)

        self.main_layout.addWidget(self.btn_7, 2, 1, 1, 1)
        self.main_layout.addWidget(self.btn_8, 2, 2, 1, 1)
        self.main_layout.addWidget(self.btn_9, 2, 3, 1, 1)
        self.main_layout.addWidget(self.btn_multi, 2, 4, 1, 1)

        self.main_layout.addWidget(self.btn_4, 3, 1, 1, 1)
        self.main_layout.addWidget(self.btn_5, 3, 2, 1, 1)
        self.main_layout.addWidget(self.btn_6, 3, 3, 1, 1)
        self.main_layout.addWidget(self.btn_moins, 3, 4, 1, 1)

        self.main_layout.addWidget(self.btn_1, 4, 1, 1, 1)
        self.main_layout.addWidget(self.btn_2, 4, 2, 1, 1)
        self.main_layout.addWidget(self.btn_3, 4, 3, 1, 1)
        self.main_layout.addWidget(self.btn_plus, 4, 4, 1, 1)

        self.main_layout.addWidget(self.btn_0, 5, 1, 1, 1)
        self.main_layout.addWidget(self.btn_00, 5, 2, 1, 1)
        self.main_layout.addWidget(self.btn_point, 5, 3, 1, 1)
        self.main_layout.addWidget(self.btn_egale, 5, 4, 1, 1)

    @property
    def get_button(self):
        digit_button = []

        for i in range(self.main_layout.count()):
            widget = self.main_layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                digit_button.append(widget)

        return digit_button

    def setup_connections(self):

        for btn in self.get_button:
            if btn.text().isdigit():
                btn.clicked.connect(partial(self.numberPressed, btn.text()))


        self.btn_plus.clicked.connect(partial(self.operationPressed, self.btn_plus.text()))
        self.btn_moins.clicked.connect(partial(self.operationPressed, self.btn_moins.text()))
        self.btn_multi.clicked.connect(partial(self.operationPressed, self.btn_multi.text()))
        self.btn_div.clicked.connect(partial(self.operationPressed, self.btn_div.text()))


        self.btn_bracket1.clicked.connect(partial(self.operationPressed, self.btn_bracket1.text()))
        self.btn_bracket2.clicked.connect(partial(self.operationPressed, self.btn_bracket2.text()))
        self.btn_point.clicked.connect(partial(self.operationPressed, self.btn_point.text()))


        self.btn_egale.clicked.connect(self.calculOperation)
        self.btn_c.clicked.connect(self.deleteResult)

    def numberPressed(self, bouton):

        result = str(self.le_result.text())

        if result == "0":
            self.le_result.setText(bouton)
        else:
            self.le_result.setText(result + bouton)

    def operationPressed(self, operation):
        result = str(self.le_result.text())

        self.le_result.setText(result + operation)

    def calculOperation(self):
        result = str(self.le_result.text())

        self.le_result.setText(result)

        try:
            resultOperation = eval(str(self.le_result.text()))
            self.le_result.setText(str(resultOperation))

        except ZeroDivisionError:
            self.le_result.setText("Error")

        except SyntaxError:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setText("Operation invalide")
            msg_box.exec_()

    def deleteResult(self):
        self.le_result.setText("0")

    def setupShortcut(self):
        for btn in range(0, 10):
            QtWidgets.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.numberPressed, str(btn)))

        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_moins.text())), self, partial(self.operationPressed, str(self.btn_moins.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_plus.text())), self, partial(self.operationPressed, str(self.btn_plus.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_multi.text())), self, partial(self.operationPressed, str(self.btn_multi.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_div.text())), self, partial(self.operationPressed, str(self.btn_div.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_point.text())), self, partial(self.operationPressed, str(self.btn_point.text())))
        
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_bracket1.text())), self, partial(self.operationPressed, str(self.btn_bracket1.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_bracket2.text())), self, partial(self.operationPressed, str(self.btn_bracket2.text())))

        QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self, self.calculOperation)
        QtWidgets.QShortcut(QtGui.QKeySequence("Del"), self, self.deleteResult)
        QtWidgets.QShortcut(QtGui.QKeySequence("Esc"), self, self.close)