from dataclasses import dataclass

@dataclass
class Player:
    name: str
    score: int

def add_player_score(leaderboard: list[Player], new_player: Player) -> list[Player]:
    leaderboard.append(new_player)

    j = len(leaderboard) - 2

    while j >= 0 and leaderboard[j].score < new_player.score:
        leaderboard[j + 1] = leaderboard[j]
        j -= 1
    leaderboard[j + 1] = new_player

def insertion_sort_batch(players: list[Player]) -> list[Player]:
    for i in range(1, len(players)):
        key = players[i]
        j = i-1
        while j >= 0 and key.score > players[j].score:
            players[j + 1] = players[j]
            j -= 1
        players[j + 1] = key
    return players

if __name__ == "__main__":
    leaderboard = []

    print("Processing Live Stream...")
    live_entries = [
        Player("Alice", 150),
        Player("Bob", 200),
        Player("Charlie", 180),
    ]

    for player in live_entries:
        add_player_score(leaderboard, player)

    for rank, player in enumerate(leaderboard, start=1):
        print(f"Rank {rank}: {player.name} with score {player.score}")