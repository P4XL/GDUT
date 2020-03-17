from PyQt5.QtWidgets import QWidget, QTextBrowser, QPushButton, QVBoxLayout, QFileDialog, QApplication
from PyQt5.QtCore import Qt
from sys import argv
import wc


class Gui(QWidget):
    def __init__(self, wc_exe, args):
        self.wc_exe = wc_exe
        self.args = args
        super().__init__()
        self.setGeometry(800, 300, 500, 350)
        self.setWindowTitle('WC.exe')
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.textbox = QTextBrowser(self)
        self.btn = QPushButton('Choose File', self)
        self.btn.clicked.connect(self.choose_file)
        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)
        self.show()

    def choose_file(self):
        # Get select file
        self.files, files_type = QFileDialog.getOpenFileNames()
        if len(self.files) > 0:
            # When select single file
            if len(self.files) == 1:
                self.wc_exe.args.directory = self.files[0]
            # When select dual file
            else:
                self.wc_exe.flag = False
                self.wc_exe.args.directory = self.files[0]
                for file in self.files:
                    self.wc_exe.file_list.append(file)
            info = self.wc_exe.main()
            # Clear previous chosen file to avoid twice-detection   
            self.wc_exe.file_list.clear()
            self.textbox.setText("\n".join(info))
        else:
            self.textbox.setText("File not selected")


def GUI(args):
    app = QApplication(argv)
    Wc = wc.WC(args)
    ex = Gui(Wc, args)
    app.exit(app.exec_())
