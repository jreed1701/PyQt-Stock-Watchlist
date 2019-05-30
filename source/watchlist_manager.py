# -*- coding: utf-8 -*-
import os
import pandas as pd
from sqlalchemy import create_engine

from source.stock_info_aggregator import StockInfoAggregator
from source.watchlist_globals import WatchlistGlobals

class WatchlistManager:
    
    def __init__(self):
        
        self._wg = WatchlistGlobals()
        
        self.watchlist = dict()
        
        self._aggregator = StockInfoAggregator()
        
        database = 'sqlite:///%s' % self._wg._DB_NAME
        
        self._engine = create_engine(database, echo=False)
        
        exists = os.path.isfile(self._wg._DB_NAME)
                                
        if exists is True:
            self.loadFromDatabase(self._wg._DB_NAME)
        
    #def updateStockInfo():
        #Loop  
        
    def addStockByRank(self, ticker, rank):
        
        if ticker in self.watchlist.keys():
            print('Error: That item is already in the list')
        else:
            
            stock = self._aggregator.getStockInfo(ticker)
            
            stock.setRank(rank)
            
            self.watchlist[ticker] = stock
        
    def addStock(self, ticker):
        
        if ticker in self.watchlist.keys():
            print('Error: That item is already in the list')
        else:
            
            stock = self._aggregator.getStockInfo(ticker)
            
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
        
    def saveToDatabase(self):
        
        df1 = self.buildDataFrame1()
        df2 = self.buildDataFrame2()
        
        df1.to_sql(name=self._wg._TABLE1_NAME, con=self._engine, if_exists='replace')
        df2.to_sql(name=self._wg._TABLE2_NAME, con=self._engine, if_exists='replace')
        
    def loadFromDatabase(self, dbname):
        
        if self._engine is None:
            print("Error: Not connected to any database. Restart the program.")
        
        # Only need one table for this because the info is dynamic.
        # Later if time history is of interest. Do both
        try:
            df = pd.read_sql_table(table_name=self._wg._TABLE1_NAME, con=self._engine, index_col='index')
        except ValueError:
            print("Warning: Table not found.")
            return
                
        # regenerate watchlist dictionary of key ticker and value StockInfo
        # doing this way only need ticker and rank because the aggregator 
        # would have to go get up to date info anyway.
        for index, row in df.head().iterrows():
            self.addStockByRank(row['Ticker'], int(row['Rank']))
            
    def buildDataFrame1(self):
        
        if len(self.watchlist.keys()) == 0:
            return
        
        df = pd.DataFrame()
        
        for key in self.watchlist.keys():
            
            df = df.append(self.watchlist[key].getDataFrame1())
        
        df = df.sort_values(by=['Rank'], ascending=True)
        
        return df
    
    def buildDataFrame2(self):
        
        if len(self.watchlist.keys()) == 0:
            return
        
        df = pd.DataFrame()
        
        for key in self.watchlist.keys():
            
            df = df.append(self.watchlist[key].getDataFrame2())
        
        df = df.sort_values(by=['Rank'], ascending=True)
        
        return df
        
    def showList(self):
        
        if len(self.watchlist.keys()) == 0:
            print('Error: No stocks on the watchlist')
        
        for item in self.watchlist.keys():
            print('Stock Name: %s' % item)
            print(self.watchlist[item])
            
    def showStockDf(self):
        print('Dataframe 1')
        df1 = self.buildDataFrame1()
        print(df1)
        
        print('Dataframe 2')
        df2 = self.buildDataFrame2()
        print(df2)
            