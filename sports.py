import falcon
import json 

class SportsResource:
    def on_get(self, req, resp):
        sports = [
                {'id': 1, 'name': 'football', 'players': '22', 'difficulty': 'medium'}, 
                {'id': 2, 'name': 'tennis', 'players': '2', 'difficulty': 'hard'},
                {'id': 3, 'name': 'padel', 'players': '4', 'difficulty': 'easy'},
                {'id': 4, 'name': 'basketball', 'players': '10', 'difficulty': 'medium'},
                {'id': 5, 'name': 'ping pong', 'players': '2','difficulty': 'easy'}
            ]
        resp.text = json.dumps(sports)
        print(resp.status)
app = falcon.App()
app.add_route('/sports', SportsResource())
app.add_route('/sports?id=1', {'id': 1, 'name': 'football', 'players': '22', 'first_played': 'england'})