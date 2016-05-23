Python - 2016 - S1 - Scripting Languages - Assignment 2:
Jack Della - s3529497 - RMIT

Stage 1:
Run in command line:
python stage1.py station {date} time
Calculates time and station info to generate a weather report using online API.
Returns report to terminal.

Stage 2:
Run in command line:
python stage2.py
(no arguments)
Initializes local webserver at address localhost:34567
Using dropdown optioning, time and station info is gathered, and using script from stage1.
Generates report, returns webpage.

Stage 3:
NOT run in command line, scripts are used from stage2.
Implemented and 'served up' as part of the webserver.
ONLY 3 stations were implemented, as going thru 200 stations for each pixel coordinate would take too long.
To evalutate, please select either Eltham, Sunbury or Werribie stations please. :)

Stage 4:
NOT run in command line, scripts are used from stage2.
Implemented and 'served up' as part of the webserver.
TAKES ABOUT 10 SECS to read info from large stop_times.txt file
