From: Byomkesh Bakshi <bb@alaudidaeuavs.com>
Subj: Hey, need a quick favour

Hey,
I know you're just joining the company and all, but I really need a quick favour.

So we're showing a demo to the client. We have a video that we've shot over their
site, as well as a set of aerial images. We would like to show them a POC level
app where they can watch the video, and whenever they pause the video to inspect
anything, we will be able to show them the images taken at that point. It will 
add great value to our entire offering.

We had a guy do it last time, but he's basically disappeared off the face of the
earth as far as I know, and he's not left anything... No resignation letter, no
code, no farewell treat, nothing.. Looks like you'll have to start from scratch.

I am sending you all the images that we've taken. The images are geotagged, and 
the latitude and longitude of the image is stored in the metadata. I believe its
called EXIF, but I'm sure you'll be able to look that up easily. The previous dude
was using python, and a library called piexif, if I'm not mistaken, but you can
use whatever you think is best.

For the video, rather than sending the actual video, I'm just going to send you
the SRT file. That's basically like a subtitle file, that has the coordinates of
the drone at all the different times in the video.

What I want from you:
For every second in the video, I want a list of all the images that lie within 35
metres of the drone position. Give it to me in Excel format. First column, time
in seconds. Second column, all the images that lie within 35m. You coders all seem
to love CSVs, so thats fine as well, as long as I can open that shit in Excel.

Along with that, I'll also give you an excel of some points of interest for the
client. I want all images within 50 meters of these POIs. Give that to me in the
same format as above.

Also this is just the first iteration. I'm going to be sending you a LOT of these.
Just write code that you can keep running over all the data sets. This time there's
only the one video, but there might be more next time. Keep that in mind. Also the
35m and 50m values are not fixed. Its 35 and 50 this time because of the flight 
parameters. But if they fly lower next time, the values will be lower and vice versa.
Just keep that in mind.

Also, if possible, give me a KML of the drone path from the video. That would be 
pretty epic. Just do this if its easy. Not a compulsory requirement.
It would help a fair bit in planning.

Cool. 
Oh, and I want this in about half an hour. Took the previous fellow that long.

And again, Welcome to Alaudidae.

PS. If you have any ideas on what to do with this data, let me know.

Warm regards,
Byomkesh Bakshi
Product Ninja
Alaudidae UAVs
bb@alaudidaeuavs.com
