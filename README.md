# myAQI
A simple python script to scrap Air Quality Index (AQI) from AirNow which is a partnership of the U.S. Environmental Protection Agency, National Oceanic and Atmospheric Administration (NOAA), National Park Service, NASA, Centers for Disease Control, and tribal, state, and local air quality agencies. This script requires an Free API key from AirNow which can be requested here [docs.airnowapi.org](https://docs.airnowapi.org/account/request/).

Python 3.9 and Requests Package

Usage Format: main.py zip_code api_key

this was a personal project that turned into IFTTT Webhook.
My Current Applet
Date and Time Trigger
with Make a web request <-- Webhook
Then Display Sticky Notification <--lametric

https://ngsbnp3zmg.execute-api.us-west-2.amazonaws.com/live/ifttt/myaqi/current/?users_zip=92131 <--- change the zip code

value1 is Ozone

value2 is PM2.5

These are not cached values and should be hourly observered values.

Date and Time Trigger

with Make a web request <-- Webhook

Then Display Sticky Notification <--lametric
