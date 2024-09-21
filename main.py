import requests
import os
from twilio.rest import Client
# print(os.environ)


# OpenWeather credentials
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")

#  twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

weather_parameters = {
    "lat": 33.77,
    "lon": -118.19,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
# print(response.status_code)
# print response code to see if things are running smoothly
response.raise_for_status()

weather_data = (response.json())
# print(weather_data)

will_rain = False

for i in range(4):
    print(weather_data["list"][i]["weather"][0]["id"])  # we are looking for the id of the first item in the weather list
    if weather_data["list"][i]["weather"][0]["id"] < 700:  # if the id is less than 700, it will rain
        will_rain = True
        break  # without the break statement the loop would check all four weather ids, but will_rain would only reflect the condition based on the last id processed in the loop


if will_rain:
    print("Bring an umbrella today!")
else:
    print("Forecast says no rain, no need for an umbrella!")


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_="+18555421359", body="Bring an umbrella today!☔️", to=os.getenv("PHONE_NUM"))
    print(f"SID: {message.sid} STATUS: {message.status}")
