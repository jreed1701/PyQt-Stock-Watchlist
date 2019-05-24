# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidget, QTabWidget, QWidget, QVBoxLayout, \
QHBoxLayout, QPushButton, QLabel, QLineEdit, QSplitter, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot

class WatchlistAppTableWidget(QWidget):
    
        def __init__(self, parent, manager):
            
            super(QWidget, self).__init__(parent)
            
            self._manager = manager
            
            #for testing
            self._manager.addStock("ABC")
            self._manager.addStock("123")
            self._manager.addStock("XYZ")
            self._manager.addStock("456")
            
            self._selected_row = 0
            
            self.initUi()
            
        def initUi(self):
            
            self.layout = QHBoxLayout()
            
            self.tabs = QTabWidget()
            
            self.tab1 = QWidget()
            self.tab2 = QWidget()
            
            self.table1 = QTableWidget()
            self.table2 = QTableWidget()
                        
            self.tab1.layout = QVBoxLayout()
            self.tab1.layout.addWidget(self.table1)
            self.tab1.setLayout(self.tab1.layout)
            
            self.tab2.layout = QVBoxLayout()
            self.tab2.layout.addWidget(self.table2)
            self.tab2.setLayout(self.tab2.layout)
            
            self.tabs.addTab(self.tab1, "Info 1")
            self.tabs.addTab(self.tab2, "Info 2")
            
            self.layout.addWidget(self.tabs)
            
            self.action_layout = QVBoxLayout()

            label = QLabel()
            label.setText("Stock Ticker")
            self.action_layout.addWidget(label)
            
            self.ticker_textbox = QLineEdit()
            self.action_layout.addWidget(self.ticker_textbox)
            
            self.add = QPushButton("Add Stock")
            self.remove = QPushButton("Remove Stock")
            self.promote = QPushButton("Promote Stock")
            self.demote = QPushButton("Demote Stock")
            self.save = QPushButton("Save")
            
            self.action_layout.addWidget(self.add)
            self.action_layout.addWidget(self.remove)
            self.action_layout.addWidget(self.promote)
            self.action_layout.addWidget(self.demote)
            self.action_layout.addWidget(self.save)
                     
            self.action_layout.setAlignment(Qt.AlignTop)
            
            # Make Callbacks
            
            self.add.clicked.connect(self.addStock)
            self.remove.clicked.connect(self.removeStock)
            self.promote.clicked.connect(self.promoteStock)
            self.demote.clicked.connect(self.demoteStock)
            self.table1.clicked.connect(self.selectRow)
            self.table2.clicked.connect(self.selectRow)

            vsplitter = QSplitter(Qt.Vertical)            
            self.layout.addWidget(vsplitter)
            
            self.layout.addLayout(self.action_layout)
            
            self.setLayout(self.layout)
            
            self.updateTable()
            
        @pyqtSlot()
        def addStock(self):
            print("Adding a stock")
            
            ticker = self.ticker_textbox.text()
            
            if ticker == "":
                print("Error: This field is empty")
                return
            else:
                self._manager.addStock(ticker)
                
            self.updateTable()
            
        @pyqtSlot()
        def removeStock(self):
            print("Removing a stock")
            
            #get ticker.
            try:
                ticker = self.table1.item(self._selected_row,0).text()
                #print('Ticker: %s, selected row: %d' % (ticker, self._selected_row))
            except AttributeError:
                print("Error: Select a table row first!")
                return
            
            self._manager.removeStock(ticker)
            
            self.updateTable()
            
        @pyqtSlot()
        def promoteStock(self):
            print("Promoting this stock")
            
            #get ticker.
            try:
                ticker = self.table1.item(self._selected_row,0).text()
                #print('Ticker: %s, selected row: %d' % (ticker, self._selected_row))
            except AttributeError:
                print("Error: Select a table row first!")
                return
            
            self._manager.promoteStock(ticker)
            
            self.updateTable()
            
        @pyqtSlot()
        def demoteStock(self):
            print("Demoting this stock")
            
            #get ticker.
            try:
                ticker = self.table1.item(self._selected_row,0).text()
                #print('Ticker: %s, selected row: %d' % (ticker, self._selected_row))
            except AttributeError:
                print("Error: Select a table row first!")
                return
            
            self._manager.demoteStock(ticker)
            
            self.updateTable()
        
        @pyqtSlot()
        def selectRow(self):
            
            for item in self.table1.selectedItems():
                self._selected_row = item.row()    
            
        def updateTable(self):
            
            df = self._manager.buildDataFrame()
            
            #if df.empty:
            #    return
                        
            # Add one extra because the dataframe index is not counted as a
            # columns but on the table it will be
            num_cols = len(df.columns) 
            num_rows = len(df.index)
        
            self.table1.setRowCount(num_rows)
            self.table1.setColumnCount(num_cols)
            
            self.table2.setRowCount(num_rows)
            self.table2.setColumnCount(num_cols)
            
            labels = df.columns.tolist()
            
            self.table1.setHorizontalHeaderLabels(labels)
            
            for r in range(0, num_rows):
                for c in range(0, num_cols):
                    self.table1.setItem(r,c, QTableWidgetItem(df.iloc[r,c]))