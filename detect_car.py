import cv2
import datetime
import pandas as pd
from OCR import read_license_plate

# Function to grab the license plate picture
def capture_plate(video_path):
    cap = cv2.VideoCapture(video_path)
    df = pd.read_csv("lookup_table.csv")

    # Detects moving objects from stationary camera
    detect_objects = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

    # Keep track of the number of cars that pass by
    cars = 0
    licenses = []
    names = []

    while True:
        # Extract frames from video
        ret, frame = cap.read()

        # Detect objects only on the right 
        try:
            height, width, _ = frame.shape
        except AttributeError:
            break

        right_side = frame[180: 360, 320: 600]
    
        # Extract only vehicles
        mask = detect_objects.apply(right_side)
        _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draws red contours
        for cnt in contours:

            # Remove noise by only drawing on big objects
            size = cv2.contourArea(cnt)
            
            if size > 100:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(right_side, (x, y), (x + w, y + h), (0, 0, 255), 3)

                # For every passing car pass an image of a license plate 
                if (y == 1):
                    cars += 1

                    # Function that uses machine learning to read the license plate
                    licenses.append(read_license_plate(f"Resources/Images/{cars}.jpg", datetime.datetime.now()))
                    
                    # Matches license plate to owner
                    for i in range(len(df)):
                        if df.iloc[i]['License Plate'] == licenses[-1][0]:
                            df.loc[i, 'Most Recent Date'] = str(licenses[-1][1])
                            if (df.iloc[i]['Owner'] not in names):
                                print(f"Charging {df.iloc[i]['Owner']}...")
                                names.append(df.iloc[i]['Owner'])
                
                
        #cv2.imshow("Right Side of Highway", right_side)
        #cv2.imshow("Mask", mask)
        cv2.imshow("Frame", frame)

        #out.write(frame)

        # 33 ms delay between frames
        cv2.waitKey(33) 
        
        # Click the "X" icon to close window
        if cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1: 
            break


    cap.release()
    cv2.destroyAllWindows()

    # Saves the time to the csv
    df.to_csv("lookup_table.csv", index=False)
