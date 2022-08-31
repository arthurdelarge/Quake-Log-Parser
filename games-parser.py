import json
from models.game import Game

def read_games(games_log):
    games = []

    for i in range(len(games_log) - 1):
        games.append(Game(i + 1))
        # print('Game {}'.format(games[i].id))
        updates = games_log[i].split('\n')

        for j in range(len(updates)):
            if 'ClientUserinfoChanged' in updates[j]:
                id = int(updates[j].split(' n\\')[0][-1]) - 1
                name = updates[j].split(' n\\')[1].split('\\t')[0]
                # print('UPDATE ID {} | NAME {}'.format(id,name))
                games[i].set_player(id, name)

            elif 'ClientDisconnect' in updates[j]:
                id = int(updates[j].split(' ')[-1]) - 1
                # print('DELETE ID {}'.format(id))
                games[i].delete_player(id)

            elif 'Kill' in updates[j]:
                killer = int(updates[j].split('Kill: ')[1].split(' ')[0]) - 1
                killed = int(updates[j].split('Kill: ')[1].split(' ')[1]) - 1
                # print('KILL {} -> {}'.format(killer, killed))
                games[i].set_total_kills(killer, killed)

        # for player in games[i].players:
        #     print("ID: {} NAME: {} KILLS: {} OLD NAMES: {}".format(player.id, player.name, player.kills,
        #                                                           player.old_names))
        # print()

    return games

def games_to_json(games, output):
    json_array = []
    for game in games:
        players_array = []
        for player in game.players:
            players_dict = {'id':player.id, 'name':player.name, 'kills':player.kills, 'old_names':player.old_names}
            players_array.append(players_dict)

        status_dict = {'total_kills':game.total_kills, 'players':players_array}
        games_dict = {'game':game.id, 'status':status_dict}
        json_array.append(games_dict)

    json.dump(json_array, output, indent=2)

if __name__ == '__main__':
    log = open("games.log", "r").read()
    games_log = log.replace('-', '').split('ShutdownGame:')

    games = read_games(games_log)

    output = open('log.json', 'w')
    games_to_json(games, output)
    output.close()
