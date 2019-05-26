# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot

from source.watchlist_globals import *

class WatchlistCommandWidget(QWidget):
    
    def __init__(self, parent, manager, table_widget):
        
        super(QWidget, self).__init__(parent)
        
        self._wg = WatchlistGlobals()
        
        self._manager = manager
        
        self._tw = table_widget
        
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
        
        self.layout.setAlignment(Qt.AlignTop)
        
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def promoteStock(self):
        print("Promote button is working!")
        
    @pyqtSlot()
    def addStock(self):
        print("Add button is working!")
        ticker, okPressed = QInputDialog.getText(self, 
                                               "Add a stock","Ticker:", 
                                               QLineEdit.Normal, 
                                               "")
        
        if okPressed and ticker == '':
            print("Error: This field is empty")
            return
        elif okPressed and ticker != '':
            self._manager.addStock(ticker)
            
        self._tw.updateTable()
            
    @pyqtSlot()
    def removeStock(self):
        print("Removing a stock")
        
        #get ticker.
        try:
            ticker = self._tw.getTable1().item(self._tw.getSelectedRow(),0).text()
            #print('Ticker: %s, selected row: %d' % (ticker, self._selected_row))
        except AttributeError:
            print("Error: Select a table row first!")
            return
        
        self._manager.removeStock(ticker)
        
        self._tw.updateTable()


    @pyqtSlot()
    def promoteStock(self):
        print("Promoting this stock")
        
        #get ticker.
        try:
            ticker = self._tw.getTable1().item(self._tw.getSelectedRow(),0).text()
            #print('Ticker: %s, selected row: %d' % (ticker, self._selected_row))
        except AttributeError:
            print("Error: Select a table row first!")
            return
        
        self._manager.promoteStock(ticker)
        
        self._tw.updateTable()
        
    @pyqtSlot()
    def demoteStock(self):
        print("Demoting this stock")
        
        #get ticker.
        try:
            ticker = self._tw.getTable1().item(self._tw.getSelectedRow(),0).text()
            #print('Ticker: %s, selected row: %d' % (ticker, self._selected_row))
        except AttributeError:
            print("Error: Select a table row first!")
            return
        
        self._manager.demoteStock(ticker)
        
        self._tw.updateTable()
    
    @pyqtSlot() 
    def saveSheet(self):
        print("Saving table...")
        self._manager.saveToDatabase()
    
    @pyqtSlot()
    def loadSheet(self):
        print('Testing load feature')
        self._manager.loadFromDatabase(self._wg._DB_NAME)
        
        self._tw.updateTable()