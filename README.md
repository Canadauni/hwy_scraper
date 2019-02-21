# HWY SCRAPER

The province of BC has webcams on major highways that take images of road conditions ever 5-7mins. A review of the day's images are available on each camera's page which uses a call to: http://images.drivebc.ca/ReplayTheDay/json/{camera_number}.json to get the list of images which calls http://images.drivebc.ca/ReplayTheDay/archive/{camera_number}/{image_name}.jpg for each image listed in the json document previously called.

This is a pipeline to pull the images and save them to google cloud storage.

A couple of assumptions are made here:

1. You are using a google cloud storage service account to use the google cloud services client.
2. You are using at Python 3.6+
3. You aren't being rude and flooding the BC hwys website with requests.