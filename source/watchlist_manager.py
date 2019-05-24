# -*- coding: utf-8 -*-
import pandas as pd

from source.stock_info_aggregator import StockInfoAggregator

class WatchlistManager:
    
    def __init__(self):
        
        print('Created Watchlist Manager')
        
        self.watchlist = dict()
        
        self.aggregator = StockInfoAggregator()
        
    #def updateStockInfo():
        #Loop   
        
    def addStock(self, ticker):
        
        if ticker in self.watchlist.keys():
            print('Error: That item is already in the list')
        else:
            
            stock = self.aggregator.getStockInfo(ticker)
            
            #If this dicionary is empty this is the first stock and it by
            # default is the highest ranking stock. 
            if self.watchlist == {}:
                stock.setRank(1)
            else:
                #otherwise it's added as the lowest ranking stock by defualt
                size = len(self.watchlist)
                stock.setRank(size)
            
            self.watchlist[ticker] = stock
            
    def removeStock(self, ticker):
        
        if ticker not in self.watchlist.keys():
            print('Error: That stock is not in the list!')
        else:
            del self.watchlist[ticker]
            
    def buildDataFrame(self):
        
        df = pd.DataFrame()
        
        for key in self.watchlist.keys():
            
            df = df.append(self.watchlist[key].getDataFrame())
        
        #df = df.set_index('ticker')
        
        return df
        
    def showList(self):
        
        if len(self.watchlist.keys()) == 0:
            print('Error: No stocks on the watchlist')
        
        for item in self.watchlist.keys():
            print('Stock Name: %s' % item)
            print(self.watchlist[item])
            
    def showStockDf(self):
        df = self.buildDataFrame()
        print(df)
            