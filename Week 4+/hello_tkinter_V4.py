from tkinter import *
from classFile import *

#Global Variables
board = []
entity_list = []
turn_value = 0
player_select = []
Mode = 0
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

#passes (obj & int(0/1)) zero on first call to store player, then 1 on 2nd call to set player on new tile
def entity_select(obj,num):
    obj.entity.selected = 1
    update()
    #painting.create_rectangle(obj.coords[0],obj.coords[1],obj.coords[2],obj.coords[3],fill=obj.color,outline="yellow")

#Changes the color of the given tiles, obj is tile class
def changeColor(obj):
    obj.color = 'blue'
    board_square = obj
    board_square.coords = [obj.coords[0],obj.coords[1],obj.coords[2],obj.coords[3]]
    board.insert(obj.id,board_square)
    painting.create_rectangle(obj.coords[0],obj.coords[1],obj.coords[2],obj.coords[3],fill=obj.color)
    
def Turn_Manager(e):
    if(turn_value != 5 and e.x > 0):
        TileSelect(e)
    
def Mode_Select(num):
    global Mode 
    Mode = num
    if(num == 0 ):
        Move



#Click manager on board
def TileSelect(e):
    #vars
    x = e.x
    y = e.y
    global player_select 
    id_holder=0
    tileSelected = board[1] 
    print(f"click! {len(player_select)}")
    #finds clicked tile
    for obj in board:
        if(obj.coords[0]<e.x and obj.coords[1]<e.y and obj.coords[2]>e.x and obj.coords[3]>e.y):
            tileSelected = obj
            break
    tileSelected.printInfo()
    #print(f"Conditonal turn_value {turn_value}, ") 
    #if player turn and clicked tile has an entity on the ally turns 1-4
    if(obj.entity != None and len(player_select) == 0):
        #succesful player select
        if(obj.entity.team == "ally" and obj.entity.id == turn_value):
            print(f"Player {obj.entity.id} selected.")
            obj.entity.selected = 1
            player_select.append(obj)
            
    #player selected ready to move 
    # 4 Scenarios, 1. player clicks themselves or ally 2. player clicks enemy 3. player clicks empty tile 4. player clicks to impossible postion. impassable or out of range
    elif(turn_value != 5 and obj.entity == None and len(player_select) == 1):#Normal Move scenario #3
        obj.entity = player_select[0].entity
        obj.entity.selected = 0
        board[player_select[0].id].entity = None
        player_select.clear()
        
    print(f"Passing")
    update()


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

#Move = Button(root, text="Move" command=Mode_Select(0),width=45,height=20,relief=)
#Move.pack()
root.bind("<Button 1>",TileSelect)
root.mainloop()





