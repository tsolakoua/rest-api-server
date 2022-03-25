In this tutorial you are going to build an API using Python and Falcon.

[Falcon](https://falcon.readthedocs.io/en/stable/) is an open-source framework which is designed to build APIs and follows the REST architecture style. 

### Prerequisites
- Python 3
- [virtualenv](https://virtualenv.pypa.io/en/latest/) to build your virtual environment

### Step 1: Create your environment 
In your working directory, create a virtual environment to install and manage your dependencies.  

```
$ virtualenv venv 
$ source venv/bin/activate 
```

Then install the dependancies:
```
pip install falcon
pip install gunicorn
```

You will use gunicorn as a WSGI server to serve the Falcon app.

Step 2: Build the API 

Now that you've setup your environment you are able to write the necessary code to build your API. Create the file `sports.py` and add the following code:

```
import falcon
import json 

class SportsResource:
    def on_get(self, req, resp):
        sports = [
                {'id': 1, 'name': 'football', 'players': '22', 'is_olympic': 'no'}, 
                {'id': 2, 'name': 'tennis', 'players': '2', 'is_olympic': 'yes'},
                {'id': 3, 'name': 'padel', 'players': '4', 'is_olympic': 'yes'},
                {'id': 4, 'name': 'basketball', 'players': '10', 'is_olympic': 'yes',
                { 'id': 4, 'name': 'ping pong', 'players': '4', 'is_olympic': 'yes'},
                { 'id': 4, 'name': 'karate', 'players': '2', 'is_olympic': 'yes'}
            ]
        resp.text = json.dumps(sports)
        print(resp.status)
app = falcon.App()
app.add_route('/sports', SportsResource())
```

The `on_get()` function handles the GET requests. 
As you can see, `Resources` are represented by class instances, in this case SportsResource.

the resp.body = convert to json with dumps and when we call the endpoint we return the result 

Step 3: Call the API 
First start your server with 
```
gunicorn sports:app
```
Then check out the results at http://localhost:8000/sports

Add screenshot 

### Search by query parameters

id 1
difficulty easy

Both the query string and the parsed query string (as a dict) are available on the Request object that falcon passes to your API endpoint.
On your on_get method you can do: print(req.query_string)

and you can access the dict as:
        for key, value in req.params.items():
            print (key, value)

Example:
http://localhost:8000/sports?id=1&difficulty=easy
id=1&difficulty=easy
id 1
difficulty easy
