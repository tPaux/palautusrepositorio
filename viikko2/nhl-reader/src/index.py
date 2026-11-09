from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print as rprint
from rich.console import Console
from rich.table import Table

def main():

    available_seasons = " 2018-19 / 2019-20 / 2020-21 / 2021-22 / 2022-23 / 2023-24 / 2024-25 / 2025-26 / 2026-27 "
    season = input(f"Season: {available_seasons}")

    if season not in available_seasons:
        print("invalid season, please try again.")
        season = input(f"Season: {available_seasons}:  ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = input(f"Nationality: {stats.nationalities()}:  ")
    print()
    rprint(f"[italic] Season {season} players from {nationality} \n")

    players = stats.top_scorers_by_nationality(nationality)

    console = Console()

    table = Table()
    table.add_column("Released")
    table.add_column("teams")
    table.add_column("goals")
    table.add_column("assists")
    table.add_column("points")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
            )
    console.print(table)

if __name__ == "__main__":
    main()
