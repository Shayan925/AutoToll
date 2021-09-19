# Hack the North 2021 Project

## Inspiration
Toll booths are inefficient. They create congestion in traffic and waste people's time. This inspired us to create an automatic tolling system where cars can use toll roads without the need to stop at a toll booth.

## What it does
Automatic tolling takes a video as input and uses object detection to identify cars and grab their license plates. From there it uses optical character recognition to read the license plate and lookup information about the vehicle owner in a database and charge them the toll fee.

<a href="https://github.com/Shayan925/AutomaticTolling/blob/main/Resources/Videos/Output.mp4" title="Object Detector"><img src="https://github.com/Shayan925/AutomaticTolling/blob/main/Resources/Images/Thumbnail.jpg" alt="Alternate Text" /></a>

## How we built it
We used the opencv library in python to detect the moving cars in the video, Google's Vision API to perform the optical character recognition, and reading and writing to CSV file was done with the pandas library in python.

## Challenges we ran into
Our group does not possess a camera that can take high quality pictures of the license plates on moving cars. We were forced to find videos of cars driving on the highway, but the issue with this is there were no videos were the license plates were visible. Our solution was for every passing vehicle we would send a random picture of a license plate to the optical character recognition function.

## What we learned
Learned how to interact with Google's vision API as it was our first time using it. Also, tracking moving objects using computer vision is more difficult than we initially thought.

## What's next for Automatic Tolling
-Implement Google's object detection API alongside a camera hung above the highway to gather more accurate results. 
-And use a larger database and host it in the cloud.
