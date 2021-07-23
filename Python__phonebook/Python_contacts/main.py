import sys

from PyQt5.QtWidgets import QApplication 

from .views import Window

def main():
    """main function of contacts"""
    #create app
    app = QApplication(sys.argv)
    # create main window
    win = Window
    win.show()
    #run event loop
    sys.exit(app.exec())
