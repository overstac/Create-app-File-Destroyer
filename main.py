from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():                               #QFileDialog = let the app browse in the pc for files
    global filenames                            #global = you can acces the variable in all the code
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select the files to TERMINATE")
    message.setText("\n".join(filenames))

def destroy_files():
    for filename in filenames:
        path= Path(filename)
        with open(path, "wb") as file:
            file.write(b"")
        path.unlink()
    message.setText("All the files are  <font color = 'red'> TERMINATED !!! </font>")

app= QApplication([])
window= QWidget()
window.setWindowTitle("File TERMINATOR")
layout= QVBoxLayout()

description= QLabel('Select the files you want to destroy. The files will be <font color = "red"> FOREVER </font> deleted!')
layout.addWidget(description)
layout.addWidget(description, alignment=Qt.AlignmentFlag.AlignCenter)


open_btn= QPushButton("Open Files")
open_btn.setToolTip("Open Files")               #when the mouse arrow get close pop up the title inside ()
open_btn.setFixedWidth(200)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn= QPushButton("TERMINATE")
destroy_btn.setToolTip("TERMINATE")               #when the mouse arrow get close pop up the title inside ()
destroy_btn.setFixedWidth(200)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message= QLabel()
layout.addWidget(message)
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()