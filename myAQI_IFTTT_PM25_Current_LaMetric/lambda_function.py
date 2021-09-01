import json
import requests


def lambda_handler(event, context):
#Observed AQI category:
#0 - 50 1 Good
#51 - 100 2 Moderate
#101 - 150 3 Unhealthy for Sensitive Groups
#151 - 200 4 Unhealthy
#201 - 300 5 Very Unhealthy
#301 - 500 6 Hazardous
#7 Unavailable
    #API_INPUT
    users_zip = event['queryStringParameters']['users_zip']
    url = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + users_zip + "&distance=25&API_KEY={API KEY}"
    
    response = requests.get(url)
    data = response.json()
    aqi_type = data[1]['ParameterName']
    aqi_value = data[1]['AQI']    
    aqi_category = data[1]['Category']['Number']
    if aqi_category == 1:
        aqi_icon = 6620
    elif aqi_category == 2:
        aqi_icon = 6623
    elif aqi_category == 3:
        aqi_icon = 6624
    elif aqi_category == 4:
        aqi_icon = 6625
    elif aqi_category == 5:
        aqi_icon = 6626
    elif aqi_category == 6:
        aqi_icon = 6627
    else:
        aqi_icon = 6622
    api_response = {
    "frames": [
        {
            "text": "Hourly "+ str(aqi_type) + " air quality index is currently " + str(aqi_value),
            "icon": aqi_icon
        }
    ]
}
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(api_response)

    return response_object
