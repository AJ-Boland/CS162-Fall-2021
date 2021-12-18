from tkinter import *
from classFile import *


turn_value = 0




#passes (obj & int(0/1)) zero on first call to store player, then 1 on 2nd call to set player on new tile
def player_select(obj,num):
    if(num == 0):
        pass;












"""
Below is the Tkinter visual making

"""
root = Tk()

root.geometry("800x600")

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
        
        


painting = Canvas(root, width = 785, height = 580)
painting.pack()

x1 = 5
x2 =35
y1=5
y2=35

board = []




for j in range(0,19):
        
    for i in range(0,26):
        #
        board_square = tile(0)
        board_square.coords = [x1,y1,x2,y2]
        board.append(board_square)
        square = painting.create_rectangle(x1,y1,x2,y2,fill=tile.color) 
       
        x1 = x1 + 30
        x2 = x2 + 30
        

    y1 = y1 + 30
    y2 = y2 + 30 
    x1 = 5
    x2 = 35

#load entities
file_object = open("scenario_0.txt")
print(file_object.readline())







root.bind("<Button 1>",TileSelect)
root.mainloop()





