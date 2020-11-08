#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:15:09 2020

@author: babafemiogunyomi
"""
# Python program to Find day of 
# the week for a given date 
import datetime
import calendar 
import smtplib

def sendEmail(sender, receivers, message) :
    
    try :
        smtpObj = smtplib.SMTP('localhost', 25)
        smtpObj.sendmail(sender, receivers, message)
        exe_msg = "Successfully sent email"
    
    except smtplib.SMTPException :
        exe_msg = "Error: unable to send email"
        
    return exe_msg

def findDay(date): 
	born = date.weekday()
    
	return calendar.day_name[born]

def dayDelta(iDate) :
    delta = findDay(iDate)
    if delta.upper() == "SATURDAY" :
        day1_step = 2
        day2_step = -2
    elif delta.upper() == "SUNDAY" :
        day1_step = 2
        day2_step = -2
    elif delta.upper() == "MONDAY" :
        day1_step = 2
        day2_step = -2
    elif delta.upper() == "TUESDAY" :
        day1_step = 2
        day2_step = -2
    elif delta.upper() == "WEDNESDAY" :
        day1_step = 2
        day2_step = -2
    elif delta.upper() == "THURSDAY" :
        day1_step = 2
        day2_step = -2
    elif delta.upper() == "FRIDAY" :
        day1_step = 2
        day2_step = -2   
    
    sDate = iDate - datetime.timedelta(days=day1_step)   
    eDate = iDate - datetime.timedelta(days=day2_step)
    
    return [sDate, eDate]