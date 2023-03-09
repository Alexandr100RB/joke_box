import requests

def get_address_from_coords(coords):
    #заполняем параметры, которые описывались выже. Впиши в поле apikey свой токен!
    PARAMS = {
        "apikey":"3376f45b-80b5-4167-8f1b-92c49a98410c",
        "format":"json",
        "lang":"ru_RU",
        "kind":"house",
        "geocode": coords
    }

    #отправляем запрос по адресу геокодера.
    try:
        r = requests.get(url="https://geocode-maps.yandex.ru/1.x/", params=PARAMS)
        #получаем данные
        json_data = r.json()
        #вытаскиваем из всего пришедшего json строку с полным адресом.
        result = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]

        # распечатываем адрес
        print(result)
        # возвращаем полученный адрес
        return result
    except Exception as e:
        #если не смогли, то возвращаем ошибку
        return "я не смог(("


# my_cords = "37.603716,55.543578"
#
# # даем запрос на получение адреса с координатами
# address_str = get_address_from_coords(my_cords)
