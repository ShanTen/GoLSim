"""
Conway's game of life simulated in python
"""

#Shantanu - April 2020

#---Start of Imports---
from random import randint #to generate random nxn arr for simulation
from os import system, name # import only system and name from os 
from time import sleep # import sleep to show output for some time period 
#---End of Imports---

#----Start of helper Functions-----

# define our clear function to ensure our screen doesnt get messy
def clsBruteForce(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux
    else: 
        _ = system('clear') 

#global vars
board=[]
n=40 #n = 40 => 40 rows, 40 colums, in total 1600 habitable cells

def fillListWithRandLoaded(len): #To generate each row configuration (i.e n for rows)
    arr=[]
    for i in range(len):
        tkn = int(randint(0,8)/8) # a chance of 1/8 that it will be filled
        arr.append(tkn) #Appending 0 or 8 based of true or false

    print (arr) #Prints Bool populated grid
    return arr

def seedTheGrid(size): #To generate each row configuration (i.e n for cols) (I.e stacking rows) => Size 40 rows * ;
    global n,board
    for i in range(n):
        board.append(fillListWithRandLoaded(size))
    return board

def stackPrintAsterix(arr):  #Replacing 0 and 1 with asterix or blank respectively.
    for i in arr:
        for j in i:
            if(j == 1):
                print("* ",end="") 
            else:
                print("  ", end="")
        print("") #end line
        
#typical Getter/Setter Methods
def getGridCordVal(arr,x,y):
    return arr[y][x]

def setGridCordVal(arr,x,y,val):
    arr[y][x]=val
    return arr

def countLiveNeighbours(board,x,y): #Counts total live neighbours of each cell
    sum=0
    for j in range(-1,2):
        for i in range(-1,2):
            sum+=getGridCordVal(board,x+i,y+j)
    sum-=getGridCordVal(board,x,y)
    return sum

#----End of helper Functions-----

#Start of Main Entry Point

def Main(): 
    grid=seedTheGrid(n)
    
    introText = """ 
    Conway's Game of Life Simulated in Python.
    Each cell of an nxn grid represents a habitable area for a being
    Depending on the count of it's neighbours it can either reproduce or it can die.
    In this particular version, 

    1) If lnc* is 3, it reproduces
    2) If lnc* is less than 3 or more than 4, death occurs due to underpopulation and overpopulation respec.
    3) If an ant* hits the grid wall (end of either rows/colums), death occours due to over curiosity

    
    *lnc = live neighbour count
    *ant = Living Cell

    """

    print(introText)
    input ("Press Enter to start")    
    next = grid
    generations = 1000
    for genNumber in range(generations): #Simulates 1000 generations
        
        clsBruteForce() #Clear Screen 
        stackPrintAsterix(grid) #Stack print the 2D Array grid with Asterix 
        
        #Typical X,Y iteration of 2D Grid
        for xAll in range(n):
            for yAll in range(n):
            
                if(xAll==0 or xAll==n-1 or yAll==0 or yAll==n-1):  #isEdge?
                    setGridCordVal(next,xAll,yAll,0)  #Killing if spawn is in edge        
                else:
                    cellValue=getGridCordVal(grid,xAll,yAll)
                    nCount=countLiveNeighbours(grid,xAll,yAll)
                                    
                    if(cellValue==0 and nCount==3): #Populating if three members of society exist
                        setGridCordVal(next,xAll,yAll,1)
                        
                    if(cellValue==1 and (nCount<2 or nCount>3)):#Killing if under or over populated
                        setGridCordVal(next,xAll,yAll,0)
                                
                grid=next #set current grid to next grid and rerurn checks

#End of Main Entry Point

Main() #Calling Main() method