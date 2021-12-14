In this blog article we will create an endpoint with sports and we will perform GET requests to get the data. 

We are going to use Falcon, an open-source framework which is designed to build APIs and follows the REST architecture style. 

Prerequisites
- Python
- Falcon
- gunicorn: as a WSGI server in order to serve a Falcon app
- virtualenv

Step 1: Create your environment 
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

Step 2: 
Create a Python file sports.py 
In this file you will create a list of sports. The on_get() function handles the GET requests. 
As you can see, Resoirces are represented by class instances, in this case SportsResource. 

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

the resp.body = convert to json with dumps and when we call the endpoint we return the result 

Step 3: Call the API 
First start your server with 
```
gunicorn sports:app
```
Then check out the results at http://localhost:8000/sports

Add screenshot 