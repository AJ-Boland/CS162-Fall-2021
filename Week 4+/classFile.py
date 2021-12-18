


class entity:
    #player id for if there is multiple players
    id = 0

    def __init__(self, name, movement, team, starting_postion):
        entity.id += 1;
        self.id = entity.id
        self.name = name
        self.movement = movement
        if(team == "enemy"):
            self.color = "red"
        if(team == "ally"):
            self.color = "blue"
        else:
            self.color = "black"
        self.starting_postion = starting_postion
    
    def getID(self):
        #print(f"ID: {self.id}")
        return self.id









class tile:
    id = 0
    """
    if(occupied):
        occupied.color
    else:
    """
    color = "gray"
    def __init__(self,entity):
        tile.id += 1
        self.id = tile.id
        self.coords = []
        self.entity = entity
    def getID(self):
        #print(f"ID: {self.id}")
        return self.id

     

