# -*- coding: utf-8 -*-
import pandas as pd

from source.stock_info_aggregator import StockInfoAggregator

class WatchlistManager:
    
    def __init__(self):
        
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
                size = len(self.watchlist) + 1
                stock.setRank(size)
            
            self.watchlist[ticker] = stock
            
    def removeStock(self, ticker):
        
        if ticker not in self.watchlist.keys():
            print('Error: That stock is not in the list!')
        else:
            del self.watchlist[ticker]
            
            new_rank = 1
            for i in self.watchlist.keys():
                self.watchlist[i].setRank(new_rank)
                new_rank = new_rank + 1
            
    def promoteStock(self, ticker):
        
        #print('Ticker pass to promotStock: %s' % ticker)
        #print('Stocks in watchlist: %s' % self.watchlist.keys())
        
        if ticker not in self.watchlist.keys():
            print('Error: That stock is not in the list!')
        else:
            cur_stock = self.watchlist[ticker]
            cur_rank = cur_stock.getRank()
            
           # print('Rank of stock: %s' % cur_stock.getRank())
            
            if( cur_rank == 1):
                print('Error: That stock is already at the top!')
                return
            
            #Find the stock with rank - 1 and swap.
            for stock in self.watchlist.keys():
                if self.watchlist[stock].getRank() == cur_rank - 1:
                    #print('Stock that was above %s: is %s' %(ticker, stock))
                    self.watchlist[stock].decreaseRank()
                    
            cur_stock.increaseRank()
            
    def demoteStock(self, ticker):
                    
        if ticker not in self.watchlist.keys():
            print('Error: That stock is not in the list!')
        else:
            cur_stock = self.watchlist[ticker]
            cur_rank = cur_stock.getRank()
            
        if( cur_rank == len(self.watchlist.keys())):
            print('Error: That stock is already lowest ranking stock!')
            return
        
        # Find the stock with rank +1 and swap
        for stock in self.watchlist.keys():
            if self.watchlist[stock].getRank() == cur_rank + 1:
                #print('Stock that was above %s: is %s' %(ticker, stock))
                self.watchlist[stock].increaseRank()
                
        cur_stock.decreaseRank()
            
    def buildDataFrame(self):
        
        df = pd.DataFrame()
        
        for key in self.watchlist.keys():
            
            df = df.append(self.watchlist[key].getDataFrame())
        
        #df = df.set_index('ticker')
        df = df.sort_values(by=['rank'], ascending=True)
        
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
            