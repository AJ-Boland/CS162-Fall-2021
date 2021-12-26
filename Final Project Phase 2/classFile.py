

#contains all non-sentient being on the game board
class entity:
    #player id for if there is multiple players
    id = -1

    def __init__(self, name, movement, team, location):
        #Defining chacteristics
        entity.id += 1;
        self.id = entity.id
        self.name = name
        self.movement = movement
        self.team = team
        #color
        if(team == "enemy"):
            self.color = "red"
        if(team == "ally"):
            self.color = "blue"
        else:
            self.color = "black"
        self.location = location

        #Manipulated Values
        self.selected = 0 # 0 means not selected, 1 means selected
        self.rM = movement #remaining movement available to player
        self.hp = 20
        self.actionCount = 1
        #dice system to be implemented
        """"
        self.attackDice = 1 
        self.defenceDice = 1
        self.Mind = 1 
        self.body = 1
        """


    
    def getID(self):
        #print(f"ID: {self.id}")
        return self.id

    def getColor(self):
        #print(f"ID: {self.id}")
        return self.color
    def printInfo(self):
        print(f"Name: {self.name}, Movement: {self.movement}, Team: {self.team}, Current_pos: {self.location}")








#represents each tile on the board
class tile:
    id = -1
    """
    try:
    
    if(occupied):
        occupied.color
    else:
    """
   
    def __init__(self):
        tile.id += 1
        self.id = tile.id
        self.coords = []
        self.entity = None
        self.color = "gray"
        
    
    def getEntityColor(self):
        try:
            if(self.entity==None):
                return "gray"
            else:
                return self.entity.getColor()

        except:
            print("Tile color recovery failure, defaulting")
            return "gray"
    
    def update(self):
        if(self.entity==None):
            self.color = "gray"
        else:
            self.color =  self.entity.getColor()

    def getID(self):
        #print(f"ID: {self.id}")
        return self.id
    def printInfo(self):
        print(f"ID: {self.id}, Color: {self.color}")

     

