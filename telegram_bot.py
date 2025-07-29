import requests

BOT_TOKEN = "8316482118:AAE3zdcqL4nON3J_Yv07KgogPgEU24wC48k"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)
print(response.json())
