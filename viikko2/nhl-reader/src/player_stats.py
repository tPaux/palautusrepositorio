from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):

        sorted_players = sorted(self.reader.players, key=lambda player: player.points, reverse=True)

        # print(f"Players from {nationality} \n")
        return [player for player in sorted_players if player.nationality == nationality]

    def nationalities(self):
        self.setnationalities= set()

        for player in self.reader.players:
            self.setnationalities.add(player.nationality)

        self.list_nationalities = sorted(self.setnationalities)

        return "[" + " / ".join(self.list_nationalities) + "]"


