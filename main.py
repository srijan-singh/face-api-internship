import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO


from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

KEY = key

ENDPOINT = endpoint

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

single_face_image_url = 'https://www.thehindu.com/news/national/qg1q0i/article38272961.ece/ALTERNATES/LANDSCAPE_1200/PM-Modi-inaugurates-colleges-in-TN'
single_image_name = 'Narendar Modi'

detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')
if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

print('Detected face ID from', single_image_name, ':')
for face in detected_faces: print (face.face_id)
print()


first_image_face_ID = detected_faces[0].face_id