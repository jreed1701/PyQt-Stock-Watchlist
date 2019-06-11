# -*- coding: utf-8 -*-
import bs4
import requests
import sys as _sys

from bs4 import BeautifulSoup
from lxml import html


class StockInfoCollector():
    
    def __init__(self):
                
        self.company_name = ""
        self.price = 0
        self.market_cap = ""
        self.fiftytwo_week_low = 0
        self.fiftytwo_week_high = 0
        self.volume = 0
        
        self.page = None
        
    def buildUrl(self, url_type, ticker):
        
        if url_type == "SUMMARY":
            url = "https://finance.yahoo.com/quote/%s" % ticker
        elif url_type == "PROFILE":
            url = "https://finance.yahoo.com/quote/%s/profile" % ticker
        elif url_type == "STATS":
            url = "https://finance.yahoo.com/quote/%s/key-statistics" % ticker
        else:
            print('Error: StockInfoCollector::buildUrl %s was not a URL option' % url_type)
            _sys.exit()
        
        return url
    
    def getPage(self, url):
        
        page = requests.get(url)
        
        return page
    
    def getAllData(self, ticker):
        
        #self.url = "https://wallmine.com/nasdaq/%s" % ticker
        summary_url = self.buildUrl("SUMMARY", ticker)
        profile_url = self.buildUrl("PROFILE", ticker)
        stats_url = self.buildUrl("STATS", ticker)
        
        page1 = self.getPage(summary_url)
        page2 = self.getPage(profile_url)
        page3 = self.getPage(stats_url) 
        
        summary_success = self.collectSummary(page1)
        name_success = self.collectCompanyName(page2)
        stats_success = self.collectStatistics(page3)
        
        if summary_success is False:
            print("Error: StockInfoCollector::getAllData, could not get summary data")
            return False
        if name_success is False:
            print("Error: StockInfoCollector::getAllData, could not get name data")
            return False
        if stats_success is False:
            return False
            print("Error: StockInfoCollector::getAllData, could not get stats data")

        return True           
        
    def collectSummary(self, page):
                  
        try:

            soup = bs4.BeautifulSoup(page.text,'lxml')
    
            data = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
            
        except IndexError:
            return False

        self.price = float(data)
        
        print("Price is: %s" % self.price)
        
        return True
    
    def collectCompanyName(self, page):
            
        try:
            
            soup = bs4.BeautifulSoup(page.text,'lxml')
    
            data = soup.find('div',{'class':'qsp-2col-profile Mt(10px) smartphone_Mt(20px) Lh(1.7)'}).find('h3').text
            
        except IndexError:
            return False
        
        self.company_name = str(data)   
        
        print("Name is: %s" % self.company_name)
        
        return True   
    
    def collectStatistics(self, page):
           
        try:
                        
            soup = bs4.BeautifulSoup(page.text,'lxml')


            #Get STock Price History Table; Table 1   
            data = soup.\
            find('div',{'class':'Mb(10px) Pend(20px) smartphone_Pend(0px)'}). \
            find('table', {'class':'table-qsp-stats Mt(10px)'}).tbody
                        
            valuation_history = list()
            for tr in data:
                valuation_history.append(tr.find('td',{'class':'Fz(s) Fw(500) Ta(end)'}).text)
                
            print(valuation_history)

            #-----------------------------------------------------------------#
                                    
            """
            #Get STock Price History Table; Table 2   
            data = soup.\
            find('div',{'class':'Mb(10px) Pend(20px) smartphone_Pend(0px)'}). \
            find('table', {'class':'table-qsp-stats Mt(10px)'}).tbody
                        
            financial_highlights = list()
            for tr in data:
                financial_highlights.append(tr.find('td',{'class':'Fz(s) Fw(500) Ta(end)'}).text)
                
            print(financial_highlights)
            """

            #-----------------------------------------------------------------#

            #Get STock Price History Table; Table 8       
            data = soup.\
            find('div',{'class':'Pstart(20px) smartphone_Pstart(0px)'}). \
            find('table', {'class':'table-qsp-stats Mt(10px)'}).tbody
            
            stock_price_history = list()
            for tr in data:
                stock_price_history.append(tr.find('td',{'class':'Fz(s) Fw(500) Ta(end)'}).text)
                
            print(stock_price_history)
                        
        except IndexError:
            return False
        
        return True 