from models.player import Player

class Game:
    def __init__(self, id):
        self.id = id
        self.total_kills = 0
        self.players = []

    def set_player(self, id, new_name):
        for player in self.players:
            if player.id == id:
                if player.name == new_name:
                    return
                for name in player.old_names:
                    if name == new_name:
                        return
                player.set_name(new_name)
                return

        new_player = Player(id, new_name)
        self.players.append(new_player)

    def set_total_kills(self, killer, killed):
        if killer == 1021 or killer == killed:
            for player in self.players:
                if player.id == killed:
                    player.set_world_kill()

        else:
            for player in self.players:
                if player.id == killer:
                    player.set_kill()

        self.total_kills = self.total_kills + 1

    def delete_player(self, id):
        for player in self.players:
            if player.id == id:
                self.players.remove(player)
                del player

    def id(self):
        return self.id

    def total_kills(self):
        return self.total_kills

    def player(self):
        return self.players