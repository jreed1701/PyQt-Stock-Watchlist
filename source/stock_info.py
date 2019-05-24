import pandas as pd

class StockInfo:
    
    def __init__(self):
        """
        This class will define the information contiained for a stock in a 
        watchlist as described by Jason Kelly in his book. 

        Returns
        -------
        None.

        """
        
        self._rank = -1
        
        self.name = ""
        self.ticker = ""
        self.price = ""
        
    def setRank(self, rank):
        self._rank = rank
        
    def getRank(self):
        return self._rank
        
    def increaseRank(self):
        
        self._rank = self._rank - 1
        
    def decreaseRank(self):
        
        self._rank = self._rank + 1
        
        if self._rank < 0:
            self._rank = 0
             
    def getDataFrame(self):
            
        stock_info = {
                'ticker' : self.ticker,
                 'rank'   : str(self._rank),
                'name'   : self.name,
                'price'  : self.price
            }
        
        df = pd.DataFrame(data=stock_info, index=[0])
        
        #df.set_index('ticker')
        
        return df
    
    def __str__(self):
            
        string = "[ " + self.name + " ]"
        
        return string