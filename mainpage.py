
#---start import section-------------------
import time
import math
import random

from tkinter import Canvas, Frame, StringVar, Tk, Label, Button, Scale, HORIZONTAL,Text
from tkinter import ttk

from mergesort import mergeSort
from quicksort import quickSort
from bubblesort import bubbleSort
from selectionsort import selectionSort
from heapsort import heapSort
import matplotlib.pyplot as plt
import numpy as np

#---end import section---------------------


root = Tk()
root.title('Sorting Algorithms Visualizer')
root_width = 1200
root_height = 700
root.maxsize(root_width,root_height)   #(width,height)
root.config(bg='white')

#----GLOBAL VARIABLES---------
allAlgos = (
    'Bubble Sort','Merge Sort','Quick Sort','Selection Sort', 'Heap Sort',
)
allTypes = (
    'Bar Chart','Scatter Chart','Stem Chart',
)
selectedAlgo = StringVar()
pauseBool = True
arr = []


#-----------------------------

def generateRandomArray():
    #random array of non-repeating n elements
    global arr
# if inputtxt.get(1.0,)=='':

   
    n = int(dataSize.get())
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    arrayColor = ['red']  * n

    swapCount = 0
    
    displayArray(arr,arrayColor,swapCount)
 #else:
  #  s=0
   # for i in inputtxt.get(1.0,).split(","):
    #  s=+1
     
   #   n = s
    #  arr = list(range(1, n + 1))
    #  print(i[0])   
     #  arrayColor = ['red']  * n
      

    #swapCount = 0

def normalizeArray(arr):
    m = max(arr)
    return [i / m for i in arr]

def displayArray(arr,arrayColor,opCount):
    outputCanvas.delete('all')
    
    if algoCombo1.get()=='Bar Chart':
       
     n = len(arr)

     outputCanvasHeight = 300 - 10
     outputCanvasWidth = 950 - 20

     barWidth = outputCanvasWidth/(n+1)
     barspace = 5
     initialspace = 10
     normalizedArr = normalizeArray(arr)

     for i,h in enumerate(normalizedArr):
        #top - left                                           #|(x0,y0)-------------|
        x0 = i*barWidth+initialspace+barspace                 #|                    |
        y0 = outputCanvasHeight - h*350                       #|                    |
                                                              #|                    |
        #bottom-left                                          #|                    |
        x1 = (i+1)*barWidth+initialspace                      #|                    |
        y1 = outputCanvasHeight                               #|-------------(x1,y1)|

        outputCanvas.create_rectangle(x0,y0,x1,y1, fill = arrayColor[i])

     swapCountLabel = Label(outputCanvas,text = '#Swap Count : '+str(opCount),fg = 'white',bg = 'black',font = ('Comic Sans MS',12))
     outputCanvas.create_window(80,20,window = swapCountLabel)

     root.update()

    elif algoCombo1.get()=='Scatter Chart':
        
    
        #print(algoCombo1.get())
        


        np.random.seed(42)
        x = np.random.rand(50)
        y = np.random.rand(50)
        colors = np.random.rand(50)
        sizes = 1000 * np.random.rand(50)


        plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')


        plt.xlabel('X Ekseni')
        plt.ylabel('Y Ekseni')
        plt.title('Scatter Grafiği')


        plt.colorbar()
        plt.show()
        
    elif algoCombo1.get()=='Stem Chart':
     
   
         def stem_sort(arr):
           n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                arr = [5, 2, 8, 1, 6, 3, 9, 4, 7]
                stem_sort(arr)
                plt.clf()
                plt.stem(range(len(arr)), arr, use_line_collection=True)
                plt.xlabel('Index')
                plt.ylabel('Value')
                plt.title('Stem Sort')
                plt.pause(0.1)


            plt.clf()
            plt.stem(range(len(arr)), arr, use_line_collection=True)
            plt.xlabel('Index')
            plt.ylabel('Value')
            plt.title('Stem Sort - Sorted')
            plt.show()


            


            


    

# Map from string to sorting function
lookup = {
    'Bubble Sort': bubbleSort,
    'Selection Sort': selectionSort,
    'Merge Sort': mergeSort,
    'Quick Sort': quickSort,
    'Heap Sort': heapSort,
}




def startSort():
   
    global arr
    
    fn = lookup[algoCombo.get()]
    fn(arr, displayArray, sortSpeed.get, pauseBool)
   
    

    
     
   


#----User Interface Section---------------------------------------------------------------------------------------------
inputFrame = Frame(root,height = 200,width = 950,bg = 'blue')
inputFrame.grid(row = 0,column = 0,padx = 10,pady = 10)

outputCanvas = Canvas(root,height = 400,width = 950,bg = '#99ffff')
outputCanvas.grid(row = 1,column = 0,padx = 10,pady = 10)

#--input frame-------------------------------------------------------
head = Label(inputFrame,text = 'Select Algorithm -> ',fg = 'black',bg = '#ffff00',height = 1,width = 15,font = ('Comic Sans MS',14))
head.grid(row = 0,column = 0,padx = 5,pady = 5)

algoCombo = ttk.Combobox(inputFrame,values = allAlgos,width = 15,font = ('Comic Sans MS',14))
algoCombo.grid(row = 0,column = 1,padx = 5,pady = 5)
algoCombo.current()
# type
head1 = Label(inputFrame,text = 'Select Type -> ',fg = 'black',bg = '#ffff00',height = 1,width = 15,font = ('Comic Sans MS',14))
head1.grid(row = 1,column = 0,padx = 5,pady = 5)

algoCombo1 = ttk.Combobox(inputFrame,values = allTypes,width = 15,font = ('Comic Sans MS',14))
algoCombo1.grid(row = 1,column = 1,padx = 5,pady = 5)
algoCombo1.current()

generate = Button(inputFrame,text = 'Generate',fg = 'black',bg = '#ff0000',height = 1,width = 10,font = ('Comic Sans MS',14),command = generateRandomArray )
generate.grid(row = 0,column = 2,padx = 5,pady = 5)

dataSize = Scale(inputFrame,from_ = 3,to = 100,resolution = 1,length = 400,width = 15,orient = HORIZONTAL,label = 'Data Size [n]',font = ('Comic Sans MS',10))
dataSize.grid(row = 2,column = 0,padx = 5,pady = 5,columnspan = 2)

sortSpeed = Scale(inputFrame,from_ = 1,to = 100,resolution = 0.1,length = 400,width = 15,orient = HORIZONTAL,label = 'Sorting Speed [s]',font = ('Comic Sans MS',10))
sortSpeed.grid(row = 3,column = 0,padx = 5,pady = 5,columnspan = 2)

#input
head = Label(inputFrame,text = 'Data Input -> ',fg = 'black',bg = '#ffff00',height = 1,width = 15,font = ('Comic Sans MS',14))
head.grid(row = 4,column = 0,padx = 5,pady = 5)

inputtxt = Text(inputFrame, height=1, width=30,
                bg = "white",
                font = ('Comic Sans MS',18),
                
         )
inputtxt.grid(row = 4,column = 1,padx = 5,pady = 5,columnspan = 2)



play = Button(inputFrame,text = 'Play',fg = 'black',bg = '#00ff00',height = 5,width = 10,font = ('Comic Sans MS',14),command = startSort )
play.grid(row = 1,column = 2,padx = 5,pady = 5,rowspan = 2)



#--output frame------------------------------------------------------

root.mainloop()




     
#def main():
#    print("It’s time !")

#if __name__ == "__main__":
#    print("press ctrl-c to stop")
 #   loop_forever = True
 #   while loop_forever:
 #       main()
  #      try:
   #         time.sleep(10)
   #     except KeyboardInterrupt:
   #         loop_forever = False