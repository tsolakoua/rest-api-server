import falcon
import json 

class SportsResource:
    def on_get(self, req, resp):
        sports = [
                {'id': 1, 'name': 'football', 'players': '22', 'first_played': 'england'}, 
                {'id': 2, 'name': 'tennis', 'players': '2', 'first_played': 'england'},
                {'id': 3, 'name': 'padel', 'players': '4', 'first_played': 'mexico'},
                {'id': 4, 'name': 'basketball', 'players': '10', 'first_played': 'usa',
                'id': 4, 'name': 'ping pong', 'players': '2', 'first_played': 'england'}
            ]
        resp.text = json.dumps(sports)
        print(resp.status)
app = falcon.App()
app.add_route('/sports', SportsResource())