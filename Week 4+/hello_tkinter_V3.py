from tkinter import *
from classFile import *

#Global Variables
board = []
entity_list = []
turn_value = 0
















"""
Start of the tkinter loop
"""
root = Tk()
root.geometry("800x600")

#------------------Functions---------------#

#passes (obj & int(0/1)) zero on first call to store player, then 1 on 2nd call to set player on new tile
def player_select(obj,num):
    if(num == 0):
        pass;

#Changes the color of the given tiles, obj is tile class
def changeColor(obj):
    obj.color = 'blue'
    board_square = obj
    board_square.coords = [obj.coords[0],obj.coords[1],obj.coords[2],obj.coords[3]]
    board.insert(obj.id,board_square)
    painting.create_rectangle(obj.coords[0],obj.coords[1],obj.coords[2],obj.coords[3],fill=obj.color)
    

#Click manager on board
def TileSelect(e):
    x = e.x
    y = e.y
    for obj in board:
        if(obj.coords[0]<e.x and obj.coords[1]<e.y and obj.coords[2]>e.x and obj.coords[3]>e.y): #Finds selected tile

            if(turn_value == 0):
                print("hypothetical player select")
                #player_select(obj, 0)
            break

""" Decommissioned due to lack of use
#User provides starting postion by x,y, we know tiles by id, so this returns the id of the addressed tile
def convertCoords(x,y):
    #check inputs
    if ((x > 26 or y > 19) or (x < 0 or y < 0)):
        print("Bad coordinate input")
    else:
        if(y != 1):
            id = y*26 + x
        else:
            id = x
        for obj in board:
            if(obj.getID() == id):
                return(obj)
            else:
                pass
"""

        
        


painting = Canvas(root, width = 785, height = 580)
painting.pack()

x1 = 5
x2 =35
y1=5
y2=35


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
                        print("End")
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



#load game board
for j in range(0,19):
        
    for i in range(0,26):
        #
        board_square = tile()
        board_square.coords = [x1,y1,x2,y2]
        board.append(board_square)

        for creature in entity_list:            
            if(i == (creature.location[0] - 1) and j == (creature.location[1] - 1)):
                print(f"Tile infested: {board_square.getID()}")
                print(f"Conditional: {(creature.location[0] - 1)}, {(creature.location[1] - 1)}")
                board_square.entity = creature
                board_square.color = board_square.getEntityColor()
            else:
                pass
        
        square = painting.create_rectangle(x1,y1,x2,y2,fill=board_square.color) 
        board_square.printInfo()
       
        x1 = x1 + 30
        x2 = x2 + 30
        

    y1 = y1 + 30
    y2 = y2 + 30 
    x1 = 5
    x2 = 35


root.bind("<Button 1>",TileSelect)
root.mainloop()





