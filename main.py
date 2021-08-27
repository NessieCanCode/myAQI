import sys
import requests

user_zip = sys.argv[1]
api_key = sys.argv[2]


def get_parse(arg, arg1):
    url = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + arg + "&distance=25" \
                                                                                                    "&API_KEY=" + arg1
    response = requests.get(url)
    data = response.json()

    aqi_index = data[0]['AQI']
    return aqi_index


if __name__ == '__main__':
    print(get_parse(user_zip, api_key))
