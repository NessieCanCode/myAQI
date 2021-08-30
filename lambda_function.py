import json
import requests


def lambda_handler(event, context):
    # TODO: Error catching
    # TODO: Write to Database (cache)

    users_zip = event['queryStringParameters']['users_zip']
    url = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + users_zip + "&distance=25&API_KEY={API KEY HERE}"
    
    response = requests.get(url)
    data = response.json()
    O3aqi = data[0]['AQI']
    PM25aqi = data[1]['AQI']
    
    api_response = {}
    api_response['value1'] = '{0}'.format(O3aqi)
    api_response['value2'] = '{0}'.format(PM25aqi)
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(api_response)
    
    return response_object
