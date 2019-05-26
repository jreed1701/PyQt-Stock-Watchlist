# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidget, QTabWidget, QWidget, QVBoxLayout, \
QTableWidgetItem, QAbstractScrollArea
QAbstractScrollArea
from PyQt5.QtCore import pyqtSlot

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
            
            self.tabs.addTab(self.tab1, "Fundamentals")
            self.tabs.addTab(self.tab2, "Technicals")
            
            self.layout.addWidget(self.tabs)
            
            self.table1.clicked.connect(self.selectRow)
            self.table2.clicked.connect(self.selectRow)
            
            self.table1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            self.table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            
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
            
            df1 = self._manager.buildDataFrame1()
            df2 = self._manager.buildDataFrame2()

            if df1 is None or df2 is None:              
                self.table1.setRowCount(0)
                self.table1.setColumnCount(0)
                
                self.table2.setRowCount(0)
                self.table2.setColumnCount(0)
                return
                                   
            num_cols1 = len(df1.columns) 
            num_rows1 = len(df1.index)
            
            num_cols2 = len(df2.columns) 
            num_rows2 = len(df2.index)

        
            self.table1.setRowCount(num_rows1)
            self.table1.setColumnCount(num_cols1)
            
            self.table2.setRowCount(num_rows2)
            self.table2.setColumnCount(num_cols2)
            
            labels1 = df1.columns.tolist()
            self.table1.setHorizontalHeaderLabels(labels1)

            labels2 = df2.columns.tolist()
            self.table2.setHorizontalHeaderLabels(labels2)
            
            for r in range(0, num_rows1):
                for c in range(0, num_cols1):
                    self.table1.setItem(r,c, QTableWidgetItem(df1.iloc[r,c]))
            
            for r in range(0, num_rows2):
                for c in range(0, num_cols2):
                    self.table2.setItem(r,c, QTableWidgetItem(df2.iloc[r,c]))
            
            self.table1.resizeColumnsToContents()
            self.table2.resizeColumnsToContents()