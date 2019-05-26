# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot

class WatchlistCommandWidget(QWidget):
    
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        
        self.initUI()
        
    def initUI(self):
        
        self.layout = QVBoxLayout()
        
        promote_button = QPushButton("")
        
        promote_button.setStyleSheet(" \
                                     border: solid transparent; \
                                     padding: 15px; \
                                     border-image: url(resources/triangle_up.png) 100% round; \
                                     ")
        
        promote_button.clicked.connect(self.promoteStock)
        
        add_button = QPushButton("")
        
        add_button.setStyleSheet(" \
                                     border: solid transparent; \
                                     padding: 15px; \
                                     border-image: url(resources/add.png) 100% round; \
                                     ")
        
        add_button.clicked.connect(self.addStock)
        
        remove_button = QPushButton("")
        
        remove_button.setStyleSheet(" \
                                     border: solid transparent; \
                                     padding: 15px; \
                                     border-image: url(resources/remove.png) 100% round; \
                                     ")
        
        remove_button.clicked.connect(self.removeStock)
        
        demote_button = QPushButton("")
        
        demote_button.setStyleSheet(" \
                                     border: solid transparent; \
                                     padding: 15px; \
                                     border-image: url(resources/triangle_down.png) 100% round; \
                                     ")
        
        demote_button.clicked.connect(self.demoteStock)
        
        save_button = QPushButton("")
        
        save_button.setStyleSheet(" \
                                     border: solid transparent; \
                                     padding: 15px; \
                                     border-image: url(resources/save.png) 100% round; \
                                     ")
        
        save_button.clicked.connect(self.saveSheet)
        
        load_button = QPushButton("")
        
        load_button.setStyleSheet(" \
                                     border: solid transparent; \
                                     padding: 15px; \
                                     border-image: url(resources/load.png) 100% round; \
                                     ")
        
        load_button.clicked.connect(self.loadSheet)
        
        self.layout.addWidget(promote_button)
        self.layout.addWidget(add_button)
        self.layout.addWidget(remove_button)
        self.layout.addWidget(demote_button)
        self.layout.addWidget(save_button)
        self.layout.addWidget(load_button)
        
        self.layout.setAlignment(Qt.AlignCenter)
        
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def promoteStock(self):
        print("Promote button is working!")
        
    @pyqtSlot()
    def addStock(self):
        print("Add button is working!")
        text, okPressed = QInputDialog.getText(self, "Add a stock","Ticker:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
        
    @pyqtSlot()
    def removeStock(self):
        print("Remove button is working!")
        
    @pyqtSlot()
    def demoteStock(self):
        print("Demote button is working!")
        
    @pyqtSlot()
    def saveSheet(self):
        print("Save button is working!")
    
    @pyqtSlot()
    def loadSheet(self):
        print("Load button is working!")
        
        
"""
                                   border-top: 10px transparent;  \
                                     border-bottom: 10px transparent; \
                                     border-right: 10px transparent; \
                                     border-left: 10px transparent;  \
"""