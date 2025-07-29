import requests
from bot import send_telegram


message = ""
url = "https://google-flights2.p.rapidapi.com/api/v1/searchFlights"

dates = ['2025-08-05', '2025-08-06', '2025-08-07', '2025-08-08', '2025-08-09', '2025-08-10']

def cheapest_flight(flight_list):
    cheapest = None
    for flight in flight_list:
        if cheapest is None:
            cheapest = flight
        elif cheapest['price'] > flight['price']:
            cheapest = flight
    return cheapest

for date in dates:

    querystring = {
        "departure_id": "EZS",
        "arrival_id": "SAW",
        "outbound_date": date,
        "travel_class": "ECONOMY",
        "adults": "1",
        "show_hidden": "1",
        "currency": "TRY",
        "language_code": "tr",
        "country_code": "TR",
        "search_type": "cheap"
    }

    headers = {
	    "x-rapidapi-key": "8712ef1c65mshed7b035de88471fp131e9fjsnb8f4c4d87d88",
	    "x-rapidapi-host": "google-flights2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_data = response.json()
    flights = json_data['data']['itineraries']['otherFlights']

    direct_flights = [
        flight for flight in flights
        if len(flight['flights'])==1
    ]

    cheapest = cheapest_flight(direct_flights)

    if cheapest and cheapest['price']<=2000:
        message += f"{date} için uçuş:\n Kalkış: {cheapest['departure_time']}\n Varış: {cheapest['arrival_time']} \n Fiyat: {cheapest['price']} \n"
    else:
        message += f"{date} için uçuş bulunamadı \n"


send_telegram(message)

