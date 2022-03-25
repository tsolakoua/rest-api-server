import falcon
import json 
from amadeus import Client


class TestAmadeus:
    def on_get(self, req, resp):
        amadeus = Client(
            client_id= "",
            client_secret= ""
        )

        response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MAD',
        destinationLocationCode='ATH',
        departureDate='2022-11-01',
        adults=1)

        resp.text = json.dumps(response.data)
        print(resp.status)

app = falcon.App()
app.add_route('/test_amadeus', TestAmadeus())

    

