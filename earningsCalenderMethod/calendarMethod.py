#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:03:47 2020

@author: babafemiogunyomi
"""
import functions as fs
import datetime
# import yahoofinance as yf
import yfinance as yfin
from yahoo_earnings_calendar import YahooEarningsCalendar as yCal

def getCalendar(intDate) :
    calObject = yCal()
    calData = calObject.earnings_on(intDate)
    
    return calData

def tickDate(calData) :
    repData = {'Tickers':[], 'Date':[]}
    for iter in range(len(calData)) :
        repData['Tickers'].append(calData[iter]['ticker'])
        repData['Date'].append(calData[iter]['startdatetime'])
    
    return repData    

def get_data_with_yahoo_api(ticker, start_date, end_date) :
    data = yfin.download(ticker, start=start_date, end=end_date)
    return data

def getAllReturns(dataDf, rType) :
    if rType.upper() == 'CLOSE' :
        rt = dataDf.Close.pct_change()*100
    
    return rt

def controller() :
    # Read data
    interestDate = datetime.datetime.strptime('Oct 21 2020  11:59PM', '%b %d %Y %I:%M%p')
    # interestDate = datetime.datetime.now().date()
    start_date = fs.dayDelta(interestDate)[0]
    end_date = fs.dayDelta(interestDate)[1]
    # start_date = interestDate - datetime.timedelta(days=2)
    # end_date = interestDate - datetime.timedelta(days=-2)
    
    calendarData = getCalendar(interestDate) 
    tickHistData = tickDate(calendarData)
    pData = get_data_with_yahoo_api(tickHistData['Tickers'], start_date, end_date)
    rtns = getAllReturns(pData, 'Close')
    
    return rtns
    
if __name__ == "__main__" :
    d = controller()
