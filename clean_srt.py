# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 13:48:48 2018

@author: Sriram
"""
import re

def clean_srt():
    #Cleaning the SRT file  
    f = open("software_dev/videos/DJI_0301.SRT",encoding='utf-8')
    srt = f.readlines()
    srt_up=[]
    count=0
    for line in srt:
        if count%4==0:
            pass
        else:
            t = line.split(' --> ')
            for time in t:
                srt_up.append(time.rstrip())
        count+=1
    loc_time = []
    count = 0
    for line in srt_up:
        if count%2==0:
            loc_time.append([line])
        count+=1
    final_lt = []
    time_count = 0
    count = 0
    for i in loc_time:
        if(count%2==0):
            i = list(re.split(":|,",str(i[0])))
            if i[3] == '100':
                loc = loc_time[count+1][0].split(',')
                final_lt.append([time_count,float(loc[1]),float(loc[0])])
                time_count +=1
        count += 1
    return final_lt