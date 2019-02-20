import requests
import os
import datetime as dt
from google.cloud import storage

def get_image_list(camera_number):
  r = requests.get(f'http://images.drivebc.ca/ReplayTheDay/json/{camera_number}.json')
  return r.json()

def save_to_gcloud(image_name, image_bin):
  client = storage.Client.from_service_account_json('service_creds.json')
  bucket = client.get_bucket('hwy_cam_images')
  blob = storage.Blob(f'{image_name}.jpg', bucket)
  blob.upload_from_string(image_bin, content_type='image/jpeg')

def get_images(camera_number):
  image_list = get_image_list(camera_number)
  for image_name in image_list:
    image_hour = dt.datetime.strptime(image_name, '%Y%m%d%H%M').hour
    if image_hour >= 5 or image_hour <= 18:
      url = f'http://images.drivebc.ca/ReplayTheDay/archive/{camera_number}/{image_name}.jpg'
      image = requests.get(url)
      if image.status_code == 200:
        image_bin = image.content
        save_to_gcloud(image_name, image_bin)

get_images(354)