import falcon
import json 

class SportsResource:
    def on_get(self, req, resp):
        sports = [
                {'id': 1, 'name': 'football', 'players': '22', 'origin': 'england'}, 
                {'id': 2, 'name': 'tennis', 'players': '2', 'origin': 'england'},
                {'id': 3, 'name': 'padel', 'players': '4', 'origin': 'mexico'},
                {'id': 4, 'name': 'basketball', 'players': '10', 'origin': 'usa',
                'id': 4, 'name': 'ping pong', 'players': '4', 'origin': 'england'}
            ]
        resp.text = json.dumps(sports)
        print(resp.status)
app = falcon.App()
app.add_route('/sports', SportsResource())