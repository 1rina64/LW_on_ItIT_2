import requests
s_city = "Moscow,RU"
appid = "2ff6194148535b8851ac105973bcf018"
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'], "°C")
print("Минимальная температура:", data['main']['temp_min'], "°C")
print("Максимальная температура:", data['main']['temp_max'], "°C")
print("Скорость ветра:", data['wind']['speed'], "метр/сек")
print("Видимость:", data['visibility'], "метр")
