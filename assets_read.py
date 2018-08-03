# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:54:27 2018

@author: Sriram
"""

import pandas as pd
import piexif
from imutils import paths
from collections import defaultdict
from conv_meters import m_conversion
from conv_deg import convert_to_degress
from clean_srt import clean_srt
import simplekml
kml = simplekml.Kml()

loc_info = clean_srt()
video_data = pd.DataFrame(loc_info, columns = ["Time in 's'",'Latitude','Longitude'])
video_data.to_csv("Solution/Video_data.csv")

pos = []
imgExif = defaultdict(lambda : None)
asset = pd.read_csv("software_dev/assets.csv")
imagePaths = sorted(list(paths.list_images('software_dev/images/')))

#Getting GPS Tag from exif
for img in imagePaths:
    imgExif = piexif.load(img)
    if imgExif['GPS']=={}:
        ##print("{} has no EXIF GPS Tags".format(img))
        continue
    lat = convert_to_degress(imgExif['GPS'][2])
    lon = convert_to_degress(imgExif['GPS'][4])
    img_name = img.split('/')[2]
    pos.append([img_name, lat, lon,(imgExif['GPS'][6][0]/imgExif['GPS'][6][1])])
img_data = pd.DataFrame(pos,columns = ['Image Location', 'Latitude', 'Longitude','Altitude'])
img_data.to_csv("Solution/Images_data.csv")

imgs_loc = []
for data in loc_info:
    img_list = []
    ch = ""
    for imgs in pos:
        if m_conversion(imgs[1],data[1],imgs[2],data[2]) <= 35:
            img_list.append(imgs[0])
    for i in img_list:
        ch = ch + i + ","
    imgs_loc.append([data[0],ch[:-1]])    
drone_loc = pd.DataFrame(imgs_loc,columns = ["Time in 's'","Images"])
drone_loc.to_csv("Solution/Drone_position_images.csv")

#Images of POI
for index,row in asset.iterrows():
    poi_list = []
    ch = ""
    for imgs in pos:
        if m_conversion(imgs[1],row[2],imgs[2],row[1]) <= 50:
            poi_list.append(imgs[0])
    for i in poi_list:
        ch = ch + i + "," 
        asset["image_names"][index] = ch[:-1]
asset.to_csv("Solution/assets_updates.csv")

#KML for Drone Path
for index,row in video_data.iterrows():
    kml.newpoint(name= str(int(row[0])) + 's', coords=[(row[1],row[2])])
kml.save(path = "Solution/Drone_path.kml")