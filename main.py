import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.uic import loadUi


class FormApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("form.ui", self)

        self.pushButton.clicked.connect(self.save_data)
        self.pushButton_2.clicked.connect(self.clear_fields)

        quit_shortcut = QShortcut(QKeySequence("Q"), self)
        quit_shortcut.activated.connect(self.close)

    def save_data(self):
        name = self.lineEdit.text().strip()
        email = self.lineEdit_2.text().strip()
        age = self.lineEdit_3.text().strip()
        phone = self.lineEdit_4.text().strip()
        address = self.textEdit.toPlainText().strip()
        gender = self.comboBox.currentText().strip()
        education = self.comboBox_2.currentText().strip()

        if not name or not email or not age or not phone or not address or gender == "" or education == "":
            QMessageBox.warning(self, "Input Error", "Semua field harus diisi.")
            return

        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            QMessageBox.warning(self, "Input Error", "Format email tidak valid.")
            return

        if not age.isdigit() or int(age) <= 0:
            QMessageBox.warning(self, "Input Error", "Usia harus berupa angka positif.")
            return

        if not re.fullmatch(r"\+62 \d{3} \d{4} \d{4}", phone):
            QMessageBox.warning(self, "Input Error", "Nomor telepon harus dalam format: +62 812 3456 7890.")
            return

        if gender not in ["Male", "Female"]:
            QMessageBox.warning(self, "Input Error", "Pilih jenis kelamin yang sesuai.")
            return

        valid_edu = [
            "Taman Kanak-Kanak", "Sekolah Dasar", "Sekolah Menengah Pertama",
            "Sekolah Menengah Atas", "Diploma", "Sarjana 1", "Sarjana 2"
        ]
        if education not in valid_edu:
            QMessageBox.warning(self, "Input Error", "Pilih jenjang pendidikan yang sesuai.")
            return

        QMessageBox.information(self, "Success", "Data berhasil disimpan.")
        self.clear_fields()

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.setText("+62 ")
        self.textEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormApp()
    window.show()
    sys.exit(app.exec_())
