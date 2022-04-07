In this repository we use FastAPI and Falcon in order to
- Call the Amadeus Self-Service flight APIs with the Python SDK. 
- Build a REST API which retrieves sports data


## How to run the project locally

Clone the repository.

```sh
https://github.com/tsolakoua/rest-api-server.git
cd rest-api-server
```

Next create a virtual environment with [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html) and install the dependencies.

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To to run the `fastapi_flights.py` and `falcon_flights.py` you will have to pass the API key and secret to your environmental variables. 

```sh
export AMADEUS_CLIENT_ID=YOUR_API_KEY
export AMADEUS_CLIENT_SECRET=YOUR_API_SECRET
```

How to call the `falcon_sports.py`:

```
gunicorn falcon_sports:app
```

How to call the `fastapi_sports.py`:

```
uvicorn fastapi_sports:app
```

How to call the `falcon_flights.py`:

```
gunicorn falcon_flights:app
```

How to call the `fastapi_flights.py`:

```
uvicorn fastapi_flights:app
```