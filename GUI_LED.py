from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Red LED
GPIO.setup(13, GPIO.OUT)  # Blue LED
GPIO.setup(15, GPIO.OUT)  # Green LED

def clicked(color):
    if color == "red":
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
    elif color == "blue":
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
    elif color == "green":
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)

def ALL_OFF():
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("LED Controller with GUI")

    redbutton = QtWidgets.QPushButton(win)
    redbutton.setText("RED")
    redbutton.clicked.connect(lambda: clicked("red"))
    redbutton.move(0, 50)

    bluebutton = QtWidgets.QPushButton(win)
    bluebutton.setText("BLUE")
    bluebutton.clicked.connect(lambda: clicked("blue"))
    bluebutton.move(0, 100)

    greenbutton = QtWidgets.QPushButton(win)
    greenbutton.setText("GREEN")
    greenbutton.clicked.connect(lambda: clicked("green"))
    greenbutton.move(0, 150)

    win.show()
    win.closeEvent = lambda event: ALL_OFF()
    sys.exit(app.exec_())

window()
