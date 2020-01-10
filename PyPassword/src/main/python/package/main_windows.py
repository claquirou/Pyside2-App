from PySide2 import QtWidgets, QtGui
from package.api import *

class MainWindow(QtWidgets.QWidget):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setFixedSize(500, 180)
        self.move(1366 / 2 - 350 / 2, 768 / 2 - 350 / 2)
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.ch_upper = QtWidgets.QCheckBox("Ajouter des lettres majuscules")
        self.ch_lower = QtWidgets.QCheckBox("Ajouter des lettres minuscules")
        self.ch_digit = QtWidgets.QCheckBox("Ajouter des chiffres")
        self.ch_character = QtWidgets.QCheckBox("Ajouter des caractères spéciaux")

        self.ch_upper.setChecked(True)
        self.ch_lower.setChecked(True)

        self.lab_lenght = QtWidgets.QLabel("Longueur du mot de passe:")
        self.spin_lenght = QtWidgets.QSpinBox()
        self.lab_password = QtWidgets.QLabel("Mot de passe:")
        self.le_password = QtWidgets.QLineEdit()

        self.le_password.setReadOnly(True)
        self.le_password.setPlaceholderText("Le mot de passe s'affichera ici")
        self.spin_lenght.setMinimum(8)
        self.spin_lenght.setMaximum(45)

        self.btn_generer = QtWidgets.QPushButton("Generer le mot de passe")
        self.btn_clipboard = QtWidgets.QPushButton("Copier le mot de passe")


    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

    def create_layouts(self):
        self.layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.layout.addWidget(self.ch_upper, 0, 0, 1, 1)
        self.layout.addWidget(self.ch_lower, 0, 1, 1, 1)
        self.layout.addWidget(self.ch_digit, 1, 0, 1, 1)
        self.layout.addWidget(self.ch_character, 1, 1, 1, 1)

        self.layout.addWidget(self.lab_lenght, 2, 0, 1, 1)
        self.layout.addWidget(self.spin_lenght, 2, 1, 1, 1)
        self.layout.addWidget(self.lab_password, 3, 0, 1, 1)
        self.layout.addWidget(self.le_password, 3, 1, 1, 1)

        self.layout.addWidget(self.btn_clipboard, 4, 0, 1, 1)
        self.layout.addWidget(self.btn_generer, 4, 1, 1, 2)

    def setup_connections(self):
        self.btn_generer.pressed.connect(self.getPassword)
        self.btn_clipboard.clicked.connect(self.clipBoard)

        QtWidgets.QShortcut(QtGui.QKeySequence("Space"), self, self.getPassword)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+C"), self, self.clipBoard)
        QtWidgets.QShortcut(QtGui.QKeySequence("Esc"), self, self.close)

    def getPassword(self):
        majuscule = upper_letter()
        minuscule = lower_letter()
        chiffre = digit_number()
        caractere = special_character()

        letter = []
        try:
            if self.ch_upper.isChecked():
                letter.append(majuscule)

            if self.ch_lower.isChecked():
                letter.append(minuscule)

            if self.ch_digit.isChecked():
                letter.append(chiffre)

            if self.ch_character.isChecked():
                letter.append(caractere)

            password = generatePassword(letters=letter, length=self.spin_lenght.value())
            self.le_password.setText(password)
        except IndexError:
            self.show_message("Merci de cocher une case avant de generé le mot de passe")

    def clipBoard(self):
        cl_board = QtWidgets.QApplication.clipboard()
        text = self.le_password.text()

        if text is not None and text:
            cl_board.clear()
            cl_board.setText(text)
            message = "Le mot de passe a été bien copier"
        else:
            message = "Aucun mot de passe à copier"

        self.show_message(message)

    def show_message(self, text):
        info = QtWidgets.QMessageBox()
        info.setWindowTitle("PyPassword")
        info.setText(text)
        info.exec_()