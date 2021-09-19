import io
import os
import datetime
from google.cloud import vision # Imports the Google Cloud client library

# Authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionAPI_Service_Account.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()


def read_license_plate(img, date):
    # Loads the image into memory
    with io.open(img, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # OCR detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Filter out to get only the license plate number
    texts = texts[0].description.split("\n")
    del texts[-1]  # Cleaning process
    del texts[-1]
    del texts[0]
    for text in texts:  # Remove element if it has no numbers
        if not any(char.isdigit() for char in text):
            texts.remove(text)
    for text in texts:  # Remove element if it has less than 6 characters
        if len(text) < 6:
            texts.remove(text)
    for i in range(len(texts)):  # Remove spaces
        texts[i] = texts[i].replace(' ', '')
        texts[i] = texts[i].replace('-', '')
    
    return [texts[0], date]