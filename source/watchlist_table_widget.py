# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidget, QTabWidget, QWidget, QVBoxLayout, \
QHBoxLayout, QPushButton, QLabel, QLineEdit, QSplitter, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot

class WatchlistTableWidget(QWidget):
    
        def __init__(self, parent, manager):
            
            super(QWidget, self).__init__(parent)
            
            self._manager = manager
                        
            self._selected_row = 0
                    
            self.initUi()
            
        def initUi(self):
            
            self.layout = QVBoxLayout()
                        
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
            
            self.table1.clicked.connect(self.selectRow)
            self.table2.clicked.connect(self.selectRow)
            
            self.setLayout(self.layout)
            
            self.updateTable()
        
        @pyqtSlot()
        def selectRow(self):
            
            for item in self.table1.selectedItems():
                self._selected_row = item.row()   
                
        def getSelectedRow(self):
            return self._selected_row

        def getTable1(self):
            return self.table1
        
        def getTable2(self):
            return self.table2
            
        def updateTable(self):
            
            df = self._manager.buildDataFrame()

            if df is None:              
                self.table1.setRowCount(0)
                self.table1.setColumnCount(0)
                
                self.table2.setRowCount(0)
                self.table2.setColumnCount(0)
                return
                        
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