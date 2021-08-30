# myAQI
A AWS Lambda function to make custom API for IFTTT, this pulls Air Quality Index (AQI) from AirNow which is a partnership of the U.S. Environmental Protection Agency, National Oceanic and Atmospheric Administration (NOAA), National Park Service, NASA, Centers for Disease Control, and tribal, state, and local air quality agencies. 

This function requires a free API key from AirNow which can be requested here [docs.airnowapi.org](https://docs.airnowapi.org/account/request/).

using AWS Lambda = Python 3.9 and custom layer (Python Package: Requests)

#### Live API for IFTTT
https://ngsbnp3zmg.execute-api.us-west-2.amazonaws.com/live/ifttt/myaqi/current/?users_zip=92131 <--- change the zip code

value1 is Ozone

value2 is PM2.5
