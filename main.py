import requests
city = "Moscow,RU"
appid = "ccbcced32f61229d3cd1ae641af0afbc"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
        params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
