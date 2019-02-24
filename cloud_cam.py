import requests
import os
import base64
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('hwy_cam_images')

def get_camera_images(message, context):
  camera_number = base64.b64decode(message['data']).decode('utf-8')
  r = requests.get(f'http://images.drivebc.ca/ReplayTheDay/json/{camera_number}.json')
  image_list = r.json()
  for image_name in image_list:
    image_hour = int(image_name[8:10])
    if image_hour >= 5 or image_hour <= 18:
      url = f'http://images.drivebc.ca/ReplayTheDay/archive/{camera_number}/{image_name}.jpg'
      image = requests.get(url)
      if image.status_code == 200:
        image_bin = image.content
        blob = storage.Blob(f'{image_name}.jpg', bucket)
        blob.upload_from_string(image_bin, content_type='image/jpeg')