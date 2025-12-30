import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("API key not set")
        return

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no"
    }

    response = requests.get(url, params)
    data = response.json()

    city = data["location"]["name"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"City: {city}, Temperature: {temp}, Condition: {condition}")


if __name__ == "__main__":
    get_weather()
