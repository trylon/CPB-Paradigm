import sys
from PySide.QtCore import *
from PySide.QtGui import *
from Robot import Robot
from WorldModel import WorldModel

robot = Robot()
world = WorldModel()

PerceptionTestingGUI = QApplication(sys.argv)

class PerceptionsGUI(QWidget):
    def __init__(self):
        self.perceptions = []
        # set title and min width
        QWidget.__init__(self)
        self.setWindowTitle('Perceptions')
        self.setMinimumWidth(400)

        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        # my booleans
        self.booleans = ['True', 'False']

        # boolean0
        self.boolean0 = QComboBox(self)
        self.boolean0.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('LOW_BATTERY:', self.boolean0)

        # boolean1
        self.boolean1 = QComboBox(self)
        self.boolean1.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('MEDICATION_REMINDER_TIME:', self.boolean1)

        # boolean2
        self.boolean2 = QComboBox(self)
        self.boolean2.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('REMINDED:', self.boolean2)

        # boolean3
        self.boolean3 = QComboBox(self)
        self.boolean3.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('REFUSED_MEDICATION:', self.boolean3)

        # boolean4
        self.boolean4 = QComboBox(self)
        self.boolean4.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('FULLY_CHARGED:', self.boolean4)

        # boolean5
        self.boolean5 = QComboBox(self)
        self.boolean5.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('NO_INTERACTION:', self.boolean5)

        # boolean6
        self.boolean6 = QComboBox(self)
        self.boolean6.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('WARNED:', self.boolean6)

        # boolean7
        self.boolean7 = QComboBox(self)
        self.boolean7.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('PERSISTENT_IMMOBILITY:', self.boolean7)

        # boolean8
        self.boolean8 = QComboBox(self)
        self.boolean8.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('ENGAGED:', self.boolean8)

        # boolean9
        self.boolean9 = QComboBox(self)
        self.boolean9.addItems(self.booleans)
        # Add it to the form layout with a label
        self.form_layout.addRow('AT_CHARGING_STATION:', self.boolean9)

        self.layout.addLayout(self.form_layout)

        # separate form layout from button
        self.layout.addStretch(1)

        # holds the button
        self.button_box = QHBoxLayout()

        # floats button to the right
        self.button_box.addStretch(1)

        # Create the build button with its caption
        self.build_button = QPushButton('Update Perceptions', self)
        # Add it to the button box
        self.button_box.addWidget(self.build_button)
        # Add the button box to the bottom
        self.layout.addLayout(self.button_box)
        # attach the perceptions function
        self.build_button.clicked.connect(self.get_perceptions)
        self.setLayout(self.layout)

    def get_perceptions(self):
        self.perceptions = []
        self.perceptions.append(self.get_boolean(str(self.boolean0.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean1.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean2.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean3.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean4.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean5.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean6.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean7.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean8.currentText())))
        self.perceptions.append(self.get_boolean(str(self.boolean9.currentText())))
        robot.performActions(self.perceptions)

        print world.generateWorld(self.perceptions)

    def get_boolean(self, perception_string):
        if "TRUE" == perception_string.upper():
            return True
        else:
            return False

    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        PerceptionTestingGUI.exec_()
