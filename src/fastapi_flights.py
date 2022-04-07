from urllib import response
from fastapi import FastAPI
from amadeus import Client

# uvicorn fastapi_flights:app --reload
app = FastAPI()

@app.get("/")
async def root():
        
    amadeus = Client()
    response = amadeus.shopping.flight_offers_search.get(
    originLocationCode='MAD',
    destinationLocationCode='ATH',
    departureDate='2022-11-01',
    adults=1,
    max=1)

    return {"data": response.data}