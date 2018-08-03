# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 13:42:42 2018

@author: Sriram
"""
import math
def m_conversion(Lat1,Lat2,Lon1,Lon2):
    latMid = (Lat1+Lat2)/2.0
    m_per_deg_lat = 111132.954 - 559.822 * math.cos( 2.0 * latMid ) + 1.175 * math.cos( 4.0 * latMid);
    m_per_deg_lon = (3.14159265359/180 ) * 6367449 * math.cos(latMid);
    deltaLat = abs(Lat1 - Lat2);
    deltaLon = abs(Lon1 - Lon2);
    dist_m = math.sqrt(  pow( deltaLat * m_per_deg_lat,2) + pow( deltaLon * m_per_deg_lon , 2) );
    return dist_m
