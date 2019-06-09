# -*- coding: utf-8 -*-

from source.stock_info_collector import  StockInfoCollector

class StockInfoCollectorTest():
    
    def __init__(self):
        
        self.collector = StockInfoCollector()
        
    def runTest(self):
        
        if self.collector.collectSummary("amd") is True:
            print("Successful collection!")
        else:
            print("Bad ticker")
    