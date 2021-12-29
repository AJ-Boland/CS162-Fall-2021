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
maxWallId = 0

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

def createWalls(tile):
    holderx1 = tile.coords[0]
    holderx2 = tile.coords[2]
    holdery1 = tile.coords[1]
    holdery2 = tile.coords[3]
    holderWalls = tile.walls
    if tile.walls == 1: #top
        tile.coords[3] -= 29
        tile.coords[1] += 1
        painting.create_line(tile.coords,fill="orange")
        print(f"Tile Walls within CreateWalls {tile.walls} Coord: {tile.coords}")
      
    elif tile.walls == 2: #right
        tile.coords[0] += 29
        tile.coords[2] -= 1
        painting.create_line(tile.coords,fill="orange")
        print(f"Tile Walls within CreateWalls {tile.walls} Coord: {tile.coords}")

        
    elif tile.walls == 3: #bottom
        tile.coords[1] += 29
        tile.coords[3] -= 1
        painting.create_line(tile.coords,fill="orange")
        print(f"Tile Walls within CreateWalls {tile.walls} Coord: {tile.coords}")
 
    elif tile.walls == 4: #left
        tile.coords[2] -= 29
        tile.coords[0] += 1
        painting.create_line(tile.coords,fill="orange")
        print(f"Tile Walls within CreateWalls {tile.walls} Coord: {tile.coords}")

    elif tile.walls == 5: #top right
        tile.walls = 1
        createWalls(tile)
        tile.walls = 2
        createWalls(tile)
    elif tile.walls == 6:
        tile.walls = 2
        createWalls(tile)
        tile.walls = 3
        createWalls(tile)
    elif tile.walls == 7:
        tile.walls = 3
        createWalls(tile)
        tile.walls = 4
        createWalls(tile)
    elif tile.walls == 8:
        tile.walls = 4
        createWalls(tile)
        tile.walls = 1
        createWalls(tile)
    #restore values
    tile.coords = [holderx1,holdery1,holderx2,holdery2]
    tile.walls = holderWalls

def Mode_Select():
    global Mode 
    if Mode == 1:
        Mode = 0
    else:
        Mode = 1
    print(f"Mode change: {Mode}")

def SaveBoard():
    print("holder")
    FolderName = input("give me a name for the file:\n")
    newFile = open(FolderName, W)
    for tile in board:
        #newFile.writelines(str(tile.walls)) 
        strholder = tile.outputInfo()
        newFile.write(strholder)



#Click manager on board
def TileSelect(e):
    #vars
    x = e.x
    y = e.y
    tileSelected = None

    # prints clicked coordinates and len of player list
    print(x,y)
    print(e)

    #finds what and if a tile was clicked
    for obj in board:
        if(obj.coords[0]<e.x and obj.coords[1]<e.y and obj.coords[2]>e.x and obj.coords[3]>e.y):
            tileSelected = obj
            break
    
    #Clicked off the board
    #if (e):
     #   print("clicked off board")
      #  return
    if(Mode == 0):
        obj.walls += 1
        if(obj.walls > 8):
            obj.walls = 0      
    tileSelected.printInfo()#tells me about the tile

    #_________________________________________Click Scenarios Below_____________________________________________#
    
    
    print(f"End of click event")
    print(f"______________________________________________________________________________")
    update()

#click bind

painting.bind("<Button 1>",TileSelect)

def update():
    global maxWallId
    for board_square in board:
        board_square.update()
        if(board_square.entity != None):
                if(board_square.entity.selected == 1):
                    painting.create_rectangle(board_square.coords[0],board_square.coords[1],board_square.coords[2],board_square.coords[3],fill="yellow")
                else:
                    painting.create_rectangle(board_square.coords[0],board_square.coords[1],board_square.coords[2],board_square.coords[3],fill=board_square.color)
        else:
            painting.create_rectangle(board_square.coords[0],board_square.coords[1],board_square.coords[2],board_square.coords[3],fill=board_square.color)
        createWalls(board_square)
        if board_square.walls > maxWallId:
            maxWallId = board_square.walls
         

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



#load game board
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
                createWalls(board_square)
            else:
                pass
        else:
            painting.create_rectangle(x1,y1,x2,y2,fill=board_square.color)
            createWalls(board_square) 
        
        
       
        x1 = x1 + 30
        x2 = x2 + 30
        

    y1 = y1 + 30
    y2 = y2 + 30 
    x1 = 5
    x2 = 35


#button stuff
ModeButton = Button(root, text="Create\nWalls", command=Mode_Select,width=5,height=2,borderwidth = 3,bg = "#a9f49f")    
ModeButton.pack(anchor= SW)
EndTurnButton = Button(root, text="Save\nBoard", command=SaveBoard,width=5,height=2,borderwidth = 3,bg = "#eb325b", font=("Times New Roman",10))
EndTurnButton.pack(anchor=SW)

def updateButtons():
    if(Mode == 1):
        ModeButton["relief"] = "sunken"
        ModeButton["text"] = "Create\nDoors"
        ModeButton["bg"] = "#9a1313"
        
    else:
        ModeButton["relief"] = "flat"
        ModeButton["text"] = "Create\nWalls"
        ModeButton["bg"] = "#a9f49f"
    #print(f"Update ran{Mode}")    
    root.after(1000, updateButtons) # run itself again after 1000 ms


# run first time
updateButtons()


root.mainloop()



#Math help received from Drew Willett
