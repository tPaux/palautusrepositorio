from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()
        self.players = [Player(player_dict) for player_dict in response]

