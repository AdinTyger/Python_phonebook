from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    
    
)


class Window(QMainWindow):
    ## Main window
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Python contacts')
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.setupUI()

    def setupUI(self):
        '''set up the main GUI'''
        #table view widget
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        #create the button
        self.addButton = QPushButton('Add...')
        self.deleteButton = QPushButton('Delete...')
        self.clearAllButton = QPushButton('Clear All')
        #layout GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        layout.addWidget(self.table)
        self.layout.addLayout(layout)

    

