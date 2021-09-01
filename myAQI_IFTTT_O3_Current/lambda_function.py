import json
import requests


def lambda_handler(event, context):
#Observed AQI category number:
#1 Good
#2 Moderate
#3 Unhealthy for Sensitive Groups
#4 Unhealthy
#5 Very Unhealthy
#6 Hazardous
#7 Unavailable
    #API_INPUT
    users_zip = event['queryStringParameters']['users_zip']
    url = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + users_zip + "&distance=25&API_KEY={API KEY}"
    response = requests.get(url)
    data = response.json()
    aqi_type = data[0]['ParameterName']
    aqi_value = data[0]['AQI']
    aqi_category = data[0]['Category']['Name']
    
    api_response = {}
    api_response['value1'] = '{0}'.format(aqi_type)
    api_response['value2'] = '{0}'.format(aqi_value)
    api_response['value3'] = '{0}'.format(aqi_category)
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(api_response)
    
    return response_object
