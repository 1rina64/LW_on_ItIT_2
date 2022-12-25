import requests
s_city = "Moscow,RU"
appid = "2ff6194148535b8851ac105973bcf018"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("Скорость ветра:", i['wind']['speed'], "метр/сек")
    print("Видимость:", i['visibility'], "метр")
    print("____________________________")