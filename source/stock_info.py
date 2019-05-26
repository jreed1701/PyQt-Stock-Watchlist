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
        
        self.ticker = ""
        self.name = ""
        self.price = ""
        self.fifty_two_week_high = ""
        self.fifty_two_week_low = ""
        self.marketcap = ""
        self.volume = ""
        self.sales = ""
        self.net_profit_margin = ""
        self.cash = ""
        self.debt = ""
        self.sales_per_share = ""
        self.cashflow_per_share = ""
        self.earnings_per_share = ""
        self.dividend_yield = ""
        self.insider_buy = ""
        self.insider_own = ""
        self.buyback = ""
        
        self.eps_rank = ""
        self.rps_rank = ""
        self.five_year_sales = ""
        self.five_year_price = ""
        self.projected_sales = ""
        self.projected_high = ""
        self.projected_low = ""
        self.time_safe = ""
        self.stars_fair_value = ""
        self.current_price_to_expense = ""
        self.average_price_to_expense = ""
        self.price_to_sales = ""
        self.price_to_book = ""
        self.current_ratio = ""
        self.price_to_cashflow = ""
        self.sma = ""
        self.macd = ""
        self.rsi = ""
        
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
             
    def getDataFrame1(self):
            
        stock_info = {
                
                # First tab info
                'Ticker' : self.ticker,
                'Rank'   : str(self._rank),
                'Name'   : self.name,
                'Price'  : self.price,
                '52 Wk High' : self.fifty_two_week_high,
                '52 Wk Low' : self.fifty_two_week_low,
                'Market Cap' : self.marketcap,
                'Volume' : self.volume,
                'Sales' : self.sales,
                'Net Profit Marget' : self.net_profit_margin,
                'Cash' : self.cash,
                'Debt' : self.debt,
                'S/S' : self.sales_per_share,
                'CFl/S' : self.cashflow_per_share,
                'E/S' : self.earnings_per_share,
                'Div Yield' : self.dividend_yield,
                'Insider Buy' : self.insider_buy,
                'Insider Own' : self.insider_own,
                'Buyback' : self.buyback      
            }
        
        df = pd.DataFrame(data=stock_info, index=[0])
        
        return df
    
    def getDataFrame2(self):
            
        stock_info = {
                
                #Second tab info
                'Ticker' : self.ticker,
                'Rank'   : str(self._rank),
                'EPS' : self.eps_rank, 
                'RPS' : self.rps_rank, 
                '5Yr Sales' : self.five_year_sales,
                '5Yr Price' : self.five_year_price, 
                'Proj Sales' : self.projected_sales, 
                'Proj High' : self.projected_high,
                'Proj Low' : self.projected_low, 
                'Time Safe' : self.time_safe, 
                'STARS Fair Val' : self.stars_fair_value,
                'Cur P/E': self.current_price_to_expense,
                'Avg P/E': self.average_price_to_expense, 
                'P/S' : self.price_to_sales, 
                'P/B' : self.price_to_book, 
                'Cur Ratio' : self.current_ratio, 
                'P/Cfl' : self.price_to_cashflow,
                'SMA' : self.sma, 
                'MACD' : self.macd, 
                'RSI' : self.rsi 
            }
        
        df = pd.DataFrame(data=stock_info, index=[0])
        
        return df
    
    def __str__(self):
            
        string = "[ " + self.name + " ]"
        
        return string