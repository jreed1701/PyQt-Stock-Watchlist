# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidget, QTabWidget, QWidget, QVBoxLayout

from PyQt5 import QtWidgets

class WatchlistAppTableWidget(QWidget):
    
        def __init__(self, parent):
            
            super(QWidget, self).__init__(parent)
            self.layout = QVBoxLayout(self)
            
            self.tabs = QTabWidget()
            
            self.tab1 = QWidget()
            self.tab2 = QWidget()
            
            self.table1 = QTableWidget()
            self.table2 = QTableWidget()
            
            self.table1.setRowCount(4)
            self.table1.setColumnCount(10)
            
            self.table2.setRowCount(4)
            self.table2.setColumnCount(10)
            
            #header = self.table1.horizontalHeader()
            #header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
            #header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            
            self.tab1.layout = QVBoxLayout()
            self.tab1.layout.addWidget(self.table1)
            self.tab1.setLayout(self.tab1.layout)
            
            self.tab2.layout = QVBoxLayout()
            self.tab2.layout.addWidget(self.table2)
            self.tab2.setLayout(self.tab2.layout)
            
            self.tabs.addTab(self.tab1, "Info 1")
            self.tabs.addTab(self.tab2, "Info 2")
            
            self.layout.addWidget(self.tabs)
            self.setLayout(self.layout)