import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "b94b263758b15f5052e91371563530ba"
account_sid = "AC1081fcbe62c45236beb1ff1910645eed"
auth_token = "5fe135310eee344d387eef6a592eeccd"

weather_params = {
    "lat": 35.117500,
    "lon": -89.971107,
    "appid": api_key,
    "exclude": "current,minute,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    conditiion_code = hour_data["weather"][0]["id"]
    if int(conditiion_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "Looks like it'll rain today. You may want to bring an umbrella.",
        from_ = "+12292354092",
        to ="+19166223458"
    )
    print(message.status)
