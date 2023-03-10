import requests
from config import APIKEY_ADDRESS, APIKEY_WEATHER


def get_address_and_weather_from_coords(coords, lon, lat):
    #заполняем параметры
    PARAMS_A = {
        "apikey": APIKEY_ADDRESS,
        "format": "json",
        "lang": "ru_RU",
        "kind": "house",
        "geocode": coords
    }
    PARAMS_W = {
        "appid": APIKEY_WEATHER,
        "format": "json",
        "lang": "ru",
        "exclude": "current",
        "units": "metric",
        "lat": lat,
        "lon": lon
    }

    #отправляем запрос по адресу геокодера.
    try:
        r_a = requests.get(url="https://geocode-maps.yandex.ru/1.x/", params=PARAMS_A)
        r_w = requests.get(url="http://api.openweathermap.org/data/2.5/find", params=PARAMS_W)

        # получаем данные
        json_data_a = r_a.json()
        json_data_w = r_w.json()
        print(json_data_w)

        # вытаскиваем из пришедшего json нужные данные.
        result_a = json_data_a["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]
        result_w = json_data_w["list"][0]["main"]["temp"], json_data_w["list"][0]["main"]["feels_like"], \
                   json_data_w["list"][0]["weather"][0]["description"]
        result = f"Адрес: {result_a}. Cейчас {result_w[0]}°C, ощущается как {result_w[1]}°C, на улице {result_w[2]}."

        # возвращаем адрес и погоду
        return result
    except Exception as e:
        #если не смогли, то возвращаем ошибку
        return "я не смог(("