import falcon
import json 
from amadeus import Client

# gunicorn falcon_flights:app
# http://127.0.0.1:8000/search/flights

class FlightOffers:
    def on_get(self, req, resp):
        amadeus = Client()

        response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MAD',
        destinationLocationCode='ATH',
        departureDate='2022-11-01',
        adults=1,
        max=1)

        resp.text = json.dumps(response.data)

app = falcon.App()
app.add_route('/search/flights', FlightOffers())

    

