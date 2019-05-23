# -*- coding: utf-8 -*-

import copy

from source.stock_info import StockInfo

class StockInfoAggregator:
    
    def __init__(self):
        
        print(' The aggregator is instantiated')
        
        self._stock_info = StockInfo()
        
    def  getStockInfo(self, ticker):
        
        self._stock_info.ticker = ticker
        self._stock_info.name = "ABC Company"
        self._stock_info.price = "$4.25"
        
        return copy.copy(self._stock_info)