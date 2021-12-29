from tkinter import *
from tkinter.font import Font
from classFile import *
from random import *
#Global Variables
board = []
dead_entity_list = []
entity_list = []
turn_value = 0
player_select = []
Mode = 0
maxId = 0
#importBoard = input("Please input name of the file you want to import")
importBoard = "defaultBoard"
#importBoard = ""

"""
Start of the tkinter loop
"""

root = Tk()
root.geometry("800x700")
painting = Canvas(root, width = 785, height = 580)
painting.pack()

x1 = 5
x2 =35
y1=5
y2=35
#------------------Functions---------------#
# Takes entity(NOT TILE), checks if the creatures turn is over, and increments the turn value if so.    
def Turn_Manager(creature):
    global turn_value
    global dead_entity_list
    global maxId
    #print(f"Turn manager ac {creature.actionCount}")
    if(creature.actionCount == 0 and creature.rM == 0): 
        turn_value += 1
        #skips dead characters turns
        for creature in dead_entity_list:
            if (entity.id == turn_value):
                turn_value += 1
        #Loops the id values
        if turn_value > maxId :
            turn_value = 0
            print(f"maxId reached {maxId}")

def Move(destination):
    if(len(player_select) == 0):
        print("Select a player first")
    else:
        destination.entity = player_select[0].entity
        destination.entity.selected = 0
        player_select[0].entity = None
        update()
        player_select.clear()


#Takes target tile, uses player select for attacker
def Attack(obj):
    if(obj.entity.hp > 5):
        obj.entity.hp -= 5
        player_select[0].entity.actionCount -= 1
    #kills target situation
    else:
        dead_entity_list.append(obj.entity)
        player_select[0].entity.actionCount -= 1
        obj.entity = player_select[0].entity
        player_select[0].entity = None
        player_select.clear()
    


    
def Mode_Select():
    global Mode 
    if Mode == 1:
        Mode = 0
    else:
        Mode = 1
    print(f"Mode change: {Mode}")
    update()
    
    #if(num == 0 ):

def EndTurn():
    if(len(player_select) == 1):
        player_select[0].entity.rM = 0 
        player_select[0].entity.actionCount = 0
        Turn_Manager(player_select[0].entity)
        player_select[0].entity.selected = 0
        update()
        player_select.clear()
        
        
    else:
        print("Select character first")

def Move_Range(player_tile,obj):
    MathID = player_tile.id
    counter = 0
    if(abs(player_tile.id - obj.id) > 25 ):
        if(obj.id > player_tile.id):
            #MathID = player_tile.id
            while(abs(MathID - obj.id)>25):
                MathID += 26
                counter += 1
        else:
            #MathID = player_tile.id
            while(abs(MathID - obj.id)>25):
                MathID -= 26
                counter += 1
    counter = abs(MathID - obj.id) + counter
    print(f"distance counter is : {counter}")
    if(counter > player_tile.entity.rM):

        return 1
    else:
        player_tile.entity.rM -= counter
        print(f"{player_tile.entity.name} Rm : {player_tile.entity.rM}")
        if(player_tile.entity.rM == 0):
            Turn_Manager(player_tile.entity)
        return 0


#Click manager on board
def TileSelect(e):
    #vars
    global player_select
    x = e.x
    y = e.y
    tileSelected = None

    # prints clicked coordinates and len of player list
    print(x,y)
    print(e)
    print(f"click! Player_Select_Length: {len(player_select)}, Turn Value: {turn_value}")

    #finds what and if a tile was clicked
    for obj in board:
        if(obj.coords[0]<e.x and obj.coords[1]<e.y and obj.coords[2]>e.x and obj.coords[3]>e.y):
            tileSelected = obj
            break
    
    #Clicked off the board
    #if (e):
     #   print("clicked off board")
      #  return
            
    tileSelected.printInfo()#tells me about the tile

    #_________________________________________Click Scenarios Below_____________________________________________#

    #Clicked tile has entity
    if(obj.entity != None): #entity on tile
        #no player selected
        if(obj.entity.id == turn_value and len(player_select) == 0): 
            print(f"{obj.entity.name} selected.")
            obj.entity.selected = 1
            player_select.append(obj)
        #player deselect
        elif(len(player_select) == 1 and obj.entity.id == player_select[0].entity.id):
            if(obj.entity.id == player_select[0].entity.id):
                obj.entity.selected = 0
                player_select.clear()
        #player attack
        elif(len(player_select) == 1 and obj.entity.team != player_select[0].entity.team and Mode == 1):
            print(f"Attack event occurred. {player_select[0].entity.name} versus {obj.entity.name}")
            Attack(obj) 
        elif(Mode == 0 and len(player_select) == 1 ):#Moving onto occupied tile
            print(f"Entity present, cannot move there")

                
    #player selected ready to move 
   
   #Move Scenarios--------------------------------------------------------------------------------------
    elif(Mode == 0 and obj.entity == None and len(player_select) == 1):#Normal Move scenario #3
        if(Move_Range(player_select[0],obj) == 0):
            obj.entity = player_select[0].entity
            obj.entity.selected = 0
            board[player_select[0].id].entity = None
            player_select.clear()
        else:
            print("Out of movement range")
           
        
    

    elif(Mode == 1 and len(player_select) == 1):#Attack nothing 
        obj.entity = player_select[0].entity
        obj.entity.selected = 0
        board[player_select[0].id].entity = None
        player_select.clear()
        print(f"That tile is empty, cannot attack there")

    else:
        print("Unknown Scenario")
        print(f"{obj.id} obj id")


    #Dungeon Master Monster Move and Attack Scenarios
    
    print(f"End of click event")
    print(f"______________________________________________________________________________")
    if(len(player_select)==1):
        Turn_Manager(player_select[0].entity)
    update()

#click bind

painting.bind("<Button 1>",TileSelect)

def update():
    for board_square in board:
        board_square.update()
        if(board_square.entity != None):
                if(board_square.entity.selected == 1):
                    painting.create_rectangle(board_square.coords[0],board_square.coords[1],board_square.coords[2],board_square.coords[3],fill="yellow")
                else:
                    painting.create_rectangle(board_square.coords[0],board_square.coords[1],board_square.coords[2],board_square.coords[3],fill=board_square.color)
        else:
            painting.create_rectangle(board_square.coords[0],board_square.coords[1],board_square.coords[2],board_square.coords[3],fill=board_square.color)

#load entities
file_object = open("scenario_0.txt")

for line in file_object:   
    #skips file comments :)
    if (line[0] == "#"):
        pass
    else:
        #input_check_Counter
        ICCounter = 0
        #Proper input check
        for i in line:
            if(i == ","):
                ICCounter += 1
        if (ICCounter != 4):
            print("bad input check file, or check me cause that is possible 2")
            break

        else:
            #Variables to be stored in entity object
            name =""
            movement = 0
            team = ""
            x = 0
            y = 0
            #Helper variables            
            comma_counter = 0
            digit_holder = 0
            loop_counter = -1 #value starts at negative one so loop counter starts at zero
            for i in line:
                loop_counter += 1

                #print(f" i:{i} counter: {comma_counter}")#Info check

                #indicates what variable is being looked at
                if(i == ","):
                    comma_counter += 1
                    pass

                #Name == 0 Movement == 1 Team == 2 [x==3,y==4]
                elif comma_counter == 0 :
                    name = name + i

                #movement
                elif comma_counter == 1:
                    if line[loop_counter+1] != ",":
                        digit_holder += 1
                        pass
                    else:
                        while digit_holder >= 0:
                            movement = int(line[loop_counter - digit_holder]) * (10 ** digit_holder) + movement
                            digit_holder -= 1
                        digit_holder = 0

                #team
                elif comma_counter == 2:
                    team = team + i

                #x
                elif comma_counter == 3:
                    if i == "[":
                        pass
                    elif line[loop_counter+1] != ",":
                        digit_holder += 1
                        pass
                    else:
                        while digit_holder >= 0:
                            x = int(line[loop_counter - digit_holder]) * (10 ** digit_holder) + x
                            digit_holder -= 1
                        digit_holder = 0

                #y
                elif comma_counter == 4:
                    if i == "]":
                        break
                    elif line[loop_counter+1] != "]":
                        digit_holder += 1
                        pass
                    else:
                        while digit_holder >= 0:
                            y = int(line[loop_counter - digit_holder]) * (10 ** digit_holder) + int(y)
                            digit_holder -= 1
                        digit_holder = 0
            #post line loop            
            Holder = entity(name,movement,team,[x,y])
            entity_list.append(Holder)
            maxId = Holder.id

def appender(obj,counter,word):
    print(f"appender counter:{counter}, word: {word}")
    if(counter == 0):
        obj.id == int(word)
    elif(counter == 1):
        obj.coords == word.split(",")
    elif(counter == 2):
        obj.color == word
    elif(counter == 3):
        obj.walls == int(word)
    elif(counter == 4):
        if(word == "None"):
            obj.entity = None
        else:
            obj.entity = entity(0,0,0,0)
            obj.entity.id = int(word)
    elif(counter == 5):
        obj.entity.name = word
    elif(counter == 6):
        obj.entity.movement = int(word)
    elif(counter == 7):
        obj.entity.team = word
    elif(counter == 8):
        obj.entity.location =  word.split(",")
    
        

#load game board
if(importBoard == ""):      
    for j in range(0,19):
            
        for i in range(0,26):
            #
            board_square = tile()
            board_square.coords = [x1,y1,x2,y2]
            board.append(board_square)

            for creature in entity_list:            
                if(i == (creature.location[0] - 1) and j == (creature.location[1] - 1)):
                    #print(f"Tile infested: {board_square.getID()}")
                    #print(f"Conditional: {(creature.location[0] - 1)}, {(creature.location[1] - 1)}")
                    board_square.entity = creature
                    board_square.color = board_square.getEntityColor()
                else:
                    pass
            else:
                painting.create_rectangle(x1,y1,x2,y2,fill=board_square.color) 
            
            
        
            x1 = x1 + 30
            x2 = x2 + 30
            

        y1 = y1 + 30
        y2 = y2 + 30 
        x1 = 5
        x2 = 35
else:
    board_square = tile()
    strholder = ""
    counter = 0
    with open(importBoard) as textFile:
        while True:
            c = textFile.read(1)
            if(c == "|"):
                appender(board_square,counter,strholder)
                counter +=1
                strholder = ""
            else:
                strholder = strholder + c

    """boardFile = open(importBoard)
    
    for line in boardFile:
        print(f"Current Line: {line}")
        counter = 0
        board_square = tile()
        strholder = ""
        str3 = str()
        for word in line:
            print(f"word: {word} strholder: {str3}")
            if(word == "|"):
                appender(board_square,counter,str3)
                strholder = ""
                counter +=1
            else:
                if(word == "[" or "]"):
                    pass
                else:
                    str3 = "".join[strholder,word]
                    #strholder = strholder + word
                """




#button stuff
ModeButton = Button(root, text="Move", command=Mode_Select,width=5,height=2,borderwidth = 3,bg = "#a9f49f")    
ModeButton.pack(anchor= SW)
EndTurnButton = Button(root, text="End \nTurn", command=EndTurn,width=5,height=2,borderwidth = 3,bg = "#eb325b", font=("Times New Roman",10))
EndTurnButton.pack(anchor=SW)

def updateButtons():
    if(Mode == 1):
        ModeButton["relief"] = "sunken"
        ModeButton["text"] = "Attack"
        ModeButton["bg"] = "#9a1313"
        
    else:
        ModeButton["relief"] = "flat"
        ModeButton["text"] = "Move"
        ModeButton["bg"] = "#a9f49f"
   # print(f"Update ran{Mode}")    
    root.after(1000, updateButtons) # run itself again after 1000 ms


# run first time
updateButtons()


root.mainloop()



#Math help received from Drew Willett
