'''
Created on 23 apr. 2021 y.
todo: a lot :DDDDD
I just need to transfer all the timer functionality in here
(while making it less shit)
@author: RX-79
'''
import os
from datetime import datetime as dt
import logger

class Record(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def  get_records(self, activity_name):
        hours = {'date' : [],
                 'duration' : [],
                }
        try:
            with open(os.path.dirname(os.path.realpath(__file__))+"\\data\\" + activity_name , 'r') as infile:
                for line in infile:
                    data = line.split(',') #0th  is the day, 1st is the comment, 2nd is duration
                    date = dt.strptime(data[0], '%d/%m/%Y %H:%M:%S')
                    duration = dt.strptime(data[2], '%H:%M:%S\n')
                    hours['date'].append(date.day) #pick what to show at graph making
                    hours['duration'].append(duration.hour + duration.minute/60 + duration.second/3600)
        except FileNotFoundError:
                logger.logging.error("get_records: no file for ", activity_name)
        logger.logging.info(hours)
        return (hours)

    def time_parse(self, time_string):
        pass

    def update_clock(self):
        timer_output = dt.now() - self.start            
        seconds_output = int (timer_output.total_seconds()) 
        hours_output = (self.secOutput // 3600)
        minutes_output = (self.secOutput % 3600) //60
        seconds_output = seconds_output - hours_output*3600 - minutes_output * 60
        #self.timerAnnounce.config(text = ( hours_output,':',  minutes_output,':', seconds_output))
        #self.handleTimer = self.window.after(1000, self.update_clock)
        return hours_output, minutes_output, seconds_output;
    #hours_output, minutes_output, seconds_output = update_clock(self)  