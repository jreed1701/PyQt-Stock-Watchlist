# -*- coding: utf-8 -*-
import requests

from lxml import html


class StockInfoCollector():
    
    def __init__(self):
        
        self.url = ""
        
        self.price = 0
        self.market_cap = ""
        self.fiftytwo_week_low = 0
        self.fiftytwo_week_high = 0
        
    def buildUrl(self, url_type, ticker):
        
        if url_type == "SUMMARY":
            url = "https://finance.yahoo.com/quote/%s" % ticker
        
        return url
        
    def collectSummary(self, ticker):
    
        #self.url = "https://wallmine.com/nasdaq/%s" % ticker
        self.url = self.buildUrl("SUMMARY", ticker)
        
        try:
        
            print(self.url)
            
            page = requests.get(self.url)
            
            doc = html.fromstring(page.content)
            
            print(doc)
            
            info = doc.xpath('//td[@data-test="PREV_CLOSE-value"]')[0]
            
            print(info)
            
            data = info.xpath('//span[@class="Trsdu(0.3s) "]/text()')
            
        except IndexError:
            print("Error: %s is not a valid ticker. " % ticker)
            return False
        
        print(data)
        
        self.price = float(data[0])

        self.market_cap = data[6]       
        
        year_range_str = data[5]
        
        print(year_range_str)
        
        
        
        return True