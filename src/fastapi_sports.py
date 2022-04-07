from fastapi import FastAPI

# uvicorn fastapi_sports:app
# http://127.0.0.1:8000/sports
# http://127.0.0.1:8000/docs
app = FastAPI()

sports = [
            {'id': 1, 'name': 'football', 'players': '22', 'difficulty': 'medium'}, 
            {'id': 2, 'name': 'tennis', 'players': '2', 'difficulty': 'hard'},
            {'id': 3, 'name': 'padel', 'players': '4', 'difficulty': 'easy'},
            {'id': 4, 'name': 'basketball', 'players': '10', 'difficulty': 'medium'},
            {'id': 5, 'name': 'ping pong', 'players': '2','difficulty': 'easy'}
        ]


@app.get("/sports/")
async def read_item(id: int, players: int):
    return sports
    