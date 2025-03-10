import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Layout:
    def identitas(label):
        return QLabel(label)

    def vertical_layout():
        groupVBox = QGroupBox("Identitas")
        v_layout = QVBoxLayout()
        v_layout.addWidget(Layout.identitas("Nama  : Muhammad Ridho Fahru Rozy"))
        v_layout.addWidget(Layout.identitas("NIM   : F1D022076"))
        v_layout.addWidget(Layout.identitas("Kelas : Pemrograman Visual C"))
        groupVBox.setLayout(v_layout)
        return groupVBox    

    def horizontal_layout():
        groupHBox = QGroupBox("Navigation")
        h_layout = QHBoxLayout()
        h_layout.addWidget(QPushButton("Home"))
        h_layout.addWidget(QPushButton("About"))
        h_layout.addWidget(QPushButton("Contact"))
        groupHBox.setLayout(h_layout)
        return groupHBox

    def form_layout():
        groupForm = QGroupBox("User Registration")  
        form_layout = QFormLayout()
        form_layout.addRow("Full Name:", QLineEdit())
        form_layout.addRow("Email:", QLineEdit())
        form_layout.addRow("Phone:", QLineEdit())

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(QRadioButton("Male"))
        radio_layout.addWidget(QRadioButton("Female"))
        form_layout.addRow("Gender:", radio_layout)

        country_combo = QComboBox()
        country_combo.addItems(["Select Country", "Indonesia", "England", "Iran", "Iraq", "Afghanistan"])
        form_layout.addRow("Country:", country_combo)
        
        groupForm.setLayout(form_layout)
        return groupForm

    def action():
        groupAction = QGroupBox("Action")
        action_Hlayout = QHBoxLayout()
        action_Hlayout.addWidget(QPushButton("Submit"))
        action_Hlayout.addWidget(QPushButton("Cancel"))
        groupAction.setLayout(action_Hlayout)
        return groupAction

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Registration Form")
        self.setFixedSize(400, 450)
        layout_utama = QVBoxLayout()
        layout_utama.setAlignment(Qt.AlignTop)
        layout_utama.setSpacing(10)
        layout_utama.addWidget(Layout.vertical_layout())
        layout_utama.addWidget(Layout.horizontal_layout())
        layout_utama.addWidget(Layout.form_layout())
        layout_utama.addWidget(Layout.action())
        self.setLayout(layout_utama)
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
