class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.kills = 0
        self.old_names = []

    def set_kill(self):
        self.kills = self.kills + 1

    def set_world_kill(self):
        self.kills = self.kills - 1

    def set_name(self, new_name):
        self.old_names.append(self.name)
        self.name = new_name

    def id(self):
        return self.id

    def name(self):
        return self.name

    def kill(self):
        return self.kills

    def old_names(self):
        return self.old_names