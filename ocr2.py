import io
import os
from google.cloud import vision # Imports the Google Cloud client library

# Authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionAPI_Service_Account.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()


def detectText(img):
    # Loads the image into memory
    with io.open(img, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    for text in texts:
        print(text.local)
    


file_name = os.path.abspath('Plate1.jpg')
detectText(file_name)