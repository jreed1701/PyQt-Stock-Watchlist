# -*- coding: utf-8 -*-

import copy

from source.stock_info import StockInfo
from source.stock_info_collector import StockInfoCollector

class StockInfoAggregator:
    
    def __init__(self):
        
        self._stock_info = StockInfo()
        
        self.collector = StockInfoCollector()
        
    def  getStockInfo(self, ticker):
        
        #data = self.collector.collectSummary(ticker)
                
        self._stock_info.ticker = ticker
        self._stock_info.name = "ABC Company"
        self._stock_info.price = "$4.25"
        
        return copy.copy(self._stock_info)