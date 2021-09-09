import tkinter as tk
import math


class Cell:
    
    def __init__(self, _parent_i, _parent_j, _f, _g, _h):
        self.parent_i = _parent_i
        self.parent_j = _parent_j
        self.f = _f
        self.g = _g
        self.h = _h


class AStarSearchAlgorithm:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("A* Search Algorithm")
        self.root.geometry("800x800")
        self.root.resizable(False, False)
        self.matrix = [[1 for x in range(80)] for y in range(80)] 
        self.start = [-1,-1]
        self.dest = [-1,-1]
        self.cellSize = 10
        self.cellKind = 0
        self.gridSize = 80

        self.map = {0: "black", 2: "green", 3: "red"}
        tools = tk.Toplevel(self.root)
        tools.title("Tools")
        tools.geometry("420x30")
        tools.resizable(False, False)

        # A Label widget to show in toplevel
        f = tk.Frame(tools, width=800)
        self.b1 = tk.Button(f, text ="Start cell", bg='green', fg = "white",command=self._toStart)
        self.b2 = tk.Button(f, text ="dest cell", bg='red', fg = "white", command=self._toDest)
        self.b3 = tk.Button(f, text ="Obstacle cell", bg='black', fg = "white", command=self._toObstacle)
        self.b3 = tk.Button(f, text ="Obstacle cell", bg='black', fg = "white", command=self._toObstacle)
        self.b4 = tk.Button(f, text ="Run Algorithm", bg='blue', fg = "white", command=self._runAlgorithm)
        self.b1.pack(side = tk.LEFT)
        self.b2.pack(side = tk.LEFT)
        self.b3.pack(side = tk.LEFT)
        self.b4.pack(side = tk.BOTTOM)
        f.pack()
        self.wn=tk.Canvas(self.root, width=800, height=800, bg='white')
        self._initialBoundery()
        self.wn.bind('<Button-1>', self._paint)
        self.wn.bind('<B1-Motion>', self._paint)
        self.wn.pack()
        self.root.mainloop()
    def _initialBoundery(self):
        for x in range(self.gridSize):
            y = 0
            self.matrix[y][x] = 1
            x = x * self.cellSize
            y = y * self.cellSize
            x1, y1 = x, y
            x2, y2 = (x + self.cellSize), (y + self.cellSize)
            self.wn.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")
        for x in range(self.gridSize):
            y = self.gridSize - 1
            self.matrix[y][x] = 1
            x = x * self.cellSize
            y = y * self.cellSize
            x1, y1 = x, y
            x2, y2 = (x + self.cellSize), (y + self.cellSize)
            self.wn.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")
        for y in range(self.gridSize):
            x = 0
            self.matrix[y][x] = 1
            x = x * self.cellSize
            y = y * self.cellSize
            x1, y1 = x, y
            x2, y2 = (x + self.cellSize), (y + self.cellSize)
            self.wn.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")
        for y in range(self.gridSize):
            x = self.gridSize - 1
            self.matrix[y][x] = 1
            x = x * self.cellSize
            y = y * self.cellSize
            x1, y1 = x, y
            x2, y2 = (x + self.cellSize), (y + self.cellSize)
            self.wn.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")

    def _toObstacle(self):
        self.cellKind = 0
    def _toStart(self):
        self.cellKind = 2
    def _toDest(self):
        self.cellKind = 3



    def _isValid(self, y, x):
        return (y >= 0) and (y < self.gridSize) and (x >= 0) and (x < self.gridSize)

    def _isUnBlocked(self, y, x):
        if self.matrix[y][x] == 1:
            return True
        return False

    def _isDestination(self, y, x):
        if (y == self.dest[0] and x == self.dest[1]):
            return True
        return False
    
    def _calculateHValue(self, y, x):
        return math.sqrt((y - self.dest[0])**2 + (x - self.dest[1])**2)

    def _tracePath(self, cellDetails):
        y = self.dest[0]
        x = self.dest[1]

        path = []

        while(not((cellDetails[y][x].parent_i == y and cellDetails[y][x].parent_j == x))):
            path.append([y,x])
            temp_y = cellDetails[y][x].parent_i;
            temp_x = cellDetails[y][x].parent_j;
            y = temp_y;
            x = temp_x;
        path.append([y, x])
        color = "blue"
        maxVal = len(path)
        while(len(path) > 0):
            p = path.pop()
            yy, xx = p
            yy *= self.cellSize
            xx *= self.cellSize
            if len(path) > 0 and len(path) < maxVal -1:
                self.wn.create_rectangle(xx, yy, xx + self.cellSize, yy + self.cellSize, fill=color, outline=color)
    
    def _aStarSearch(self):
        if not self._isValid(self.start[0], self.start[1]):
            print("Source is invalid\n")
            return
        if not self._isValid(self.dest[0], self.dest[1]):
            print("Destination is invalid\n")
            return
        if self._isUnBlocked(self.start[0], self.start[1]) == False or self._isUnBlocked(self.dest[0], self.dest[1]) == False:
            print("Source or the destination is blocked\n")
            return
        if self._isDestination(self.start[0], self.start[1]):
            print("We are already at the destination\n")
            return
        closedList = [[False for x in range(self.gridSize)] for y in range(self.gridSize)] 
        cellDetails = [[Cell(-1, -1, math.inf, math.inf, math.inf) for x in range(self.gridSize)] for y in range(self.gridSize)] 

        i, j = self.start[0], self.start[1]

        cellDetails[i][j].f = 0.0
        cellDetails[i][j].g = 0.0
        cellDetails[i][j].h = 0.0
        cellDetails[i][j].parent_i = i
        cellDetails[i][j].parent_j = j

        openList = set()

        openList.add((0.0, i, j))

        foundDest = False

        while len(openList) > 0:
            p = openList.pop()
            i = p[1]
            j = p[2]
            closedList[i][j] = True
            
            gNew, hNew, fNew = 0, 0, 0

            if self._isValid(i - 1, j):
                if self._isDestination(i - 1, j):
                    cellDetails[i - 1][j].parent_i = i
                    cellDetails[i - 1][j].parent_j = j
                    print("The destination cell is found")
                    self._tracePath(cellDetails)
                    foundDest = True
                    return
                elif closedList[i - 1][j] == False and self._isUnBlocked(i - 1, j) == True:
                    gNew = cellDetails[i][j].g + 1.0;
                    hNew = self._calculateHValue(i - 1, j)
                    fNew = gNew + hNew
                    if cellDetails[i - 1][j].f == math.inf or cellDetails[i - 1][j].f > fNew:
                        openList.add((fNew, i - 1, j))
                        cellDetails[i - 1][j].f = fNew
                        cellDetails[i - 1][j].g = gNew
                        cellDetails[i - 1][j].h = hNew
                        cellDetails[i - 1][j].parent_i = i
                        cellDetails[i - 1][j].parent_j = j
            if self._isValid(i + 1, j):
                if self._isDestination(i + 1, j):
                    cellDetails[i + 1][j].parent_i = i
                    cellDetails[i + 1][j].parent_j = j
                    print("The destination cell is found")
                    self._tracePath(cellDetails);
                    foundDest = True;
                    return;
                elif closedList[i + 1][j] == False and self._isUnBlocked(i + 1, j) == True:
                    gNew = cellDetails[i][j].g + 1.0
                    hNew = self._calculateHValue(i + 1, j)
                    fNew = gNew + hNew
                    if cellDetails[i + 1][j].f == math.inf or cellDetails[i + 1][j].f > fNew:
                        openList.add((fNew, i + 1, j))
                        cellDetails[i + 1][j].f = fNew
                        cellDetails[i + 1][j].g = gNew
                        cellDetails[i + 1][j].h = hNew
                        cellDetails[i + 1][j].parent_i = i
                        cellDetails[i + 1][j].parent_j = j
            if self._isValid(i, j + 1):
                if self._isDestination(i, j + 1):
                    cellDetails[i][j + 1].parent_i = i
                    cellDetails[i][j + 1].parent_j = j
                    print("The destination cell is found")
                    self._tracePath(cellDetails)
                    foundDest = True
                    return;
                elif closedList[i][j + 1] == False and self._isUnBlocked(i, j + 1) == True:
                    gNew = cellDetails[i][j].g + 1.0
                    hNew = self._calculateHValue(i, j + 1)
                    fNew = gNew + hNew
                    if cellDetails[i][j + 1].f == math.inf and cellDetails[i][j + 1].f > fNew:
                        openList.add((fNew, i, j + 1))
                        cellDetails[i][j + 1].f = fNew
                        cellDetails[i][j + 1].g = gNew
                        cellDetails[i][j + 1].h = hNew
                        cellDetails[i][j + 1].parent_i = i
                        cellDetails[i][j + 1].parent_j = j
            if self._isValid(i, j - 1):
                if self._isDestination(i, j - 1):
                    cellDetails[i][j - 1].parent_i = i
                    cellDetails[i][j - 1].parent_j = j
                    print("The destination cell is found")
                    self._tracePath(cellDetails)
                    foundDest = True
                    return;
                elif closedList[i][j - 1] == False and self._isUnBlocked(i, j - 1) == True:
                    gNew = cellDetails[i][j].g + 1.0;
                    hNew = self._calculateHValue(i, j - 1)
                    fNew = gNew + hNew;
                    if cellDetails[i][j - 1].f == math.inf or cellDetails[i][j - 1].f > fNew:
                        openList.add((fNew, i, j - 1))
                        cellDetails[i][j - 1].f = fNew
                        cellDetails[i][j - 1].g = gNew
                        cellDetails[i][j - 1].h = hNew
                        cellDetails[i][j - 1].parent_i = i
                        cellDetails[i][j - 1].parent_j = j
            if self._isValid(i - 1, j + 1):
                if self._isDestination(i - 1, j + 1):
                    cellDetails[i - 1][j + 1].parent_i = i
                    cellDetails[i - 1][j + 1].parent_j = j
                    print("The destination cell is foundW")
                    self._tracePath(cellDetails)
                    foundDest = True
                    return
                elif closedList[i - 1][j + 1] == False and self._isUnBlocked(i - 1, j + 1) == True:
                    gNew = cellDetails[i][j].g + 1.414;
                    hNew = self._calculateHValue(i - 1, j + 1)
                    fNew = gNew + hNew
                    if cellDetails[i - 1][j + 1].f == math.inf or cellDetails[i - 1][j + 1].f > fNew:
                        openList.add((fNew, i - 1, j + 1))
                        cellDetails[i - 1][j + 1].f = fNew
                        cellDetails[i - 1][j + 1].g = gNew
                        cellDetails[i - 1][j + 1].h = hNew
                        cellDetails[i - 1][j + 1].parent_i = i
                        cellDetails[i - 1][j + 1].parent_j = j
            if self._isValid(i - 1, j - 1):
                if self._isDestination(i - 1, j - 1):
                    cellDetails[i - 1][j - 1].parent_i = i
                    cellDetails[i - 1][j - 1].parent_j = j
                    print("The destination cell is found")
                    self._tracePath(cellDetails)
                    foundDest = True
                    return
                elif closedList[i - 1][j - 1] == False and self._isUnBlocked(i - 1, j - 1) == True:
                    gNew = cellDetails[i][j].g + 1.414
                    hNew = self._calculateHValue(i - 1, j - 1)
                    fNew = gNew + hNew
                    if cellDetails[i - 1][j - 1].f == math.inf or cellDetails[i - 1][j - 1].f > fNew:
                        openList.add((fNew, i - 1, j - 1))
                        cellDetails[i - 1][j - 1].f = fNew
                        cellDetails[i - 1][j - 1].g = gNew
                        cellDetails[i - 1][j - 1].h = hNew
                        cellDetails[i - 1][j - 1].parent_i = i
                        cellDetails[i - 1][j - 1].parent_j = j
            if self._isValid(i + 1, j + 1):
                if self._isDestination(i + 1, j + 1):
                    cellDetails[i + 1][j + 1].parent_i = i
                    cellDetails[i + 1][j + 1].parent_j = j
                    print("The destination cell is found")
                    self._tracePath(cellDetails)
                    foundDest = True
                    return
                elif closedList[i + 1][j + 1] == False and self._isUnBlocked(i + 1, j + 1) == True:
                    gNew = cellDetails[i][j].g + 1.414
                    hNew = self._calculateHValue(i + 1, j + 1)
                    fNew = gNew + hNew
                    if cellDetails[i + 1][j + 1].f == math.inf or cellDetails[i + 1][j + 1].f > fNew:
                        openList.add((fNew, i + 1, j + 1))
                        cellDetails[i + 1][j + 1].f = fNew
                        cellDetails[i + 1][j + 1].g = gNew
                        cellDetails[i + 1][j + 1].h = hNew
                        cellDetails[i + 1][j + 1].parent_i = i
                        cellDetails[i + 1][j + 1].parent_j = j
            if self._isValid(i + 1, j - 1):
                if self._isDestination(i + 1, j - 1):
                    cellDetails[i + 1][j - 1].parent_i = i
                    cellDetails[i + 1][j - 1].parent_j = j
                    print("The destination cell is found")
                    self._tracePath(cellDetails)
                    foundDest = True
                    return
                elif closedList[i + 1][j - 1] == False and self._isUnBlocked(i + 1, j - 1) == True:
                    gNew = cellDetails[i][j].g + 1.414;
                    hNew = self._calculateHValue(i + 1, j - 1);
                    fNew = gNew + hNew;
                    if cellDetails[i + 1][j - 1].f == math.inf or cellDetails[i + 1][j - 1].f > fNew:
                        openList.add((fNew, i + 1, j - 1))
                        cellDetails[i + 1][j - 1].f = fNew
                        cellDetails[i + 1][j - 1].g = gNew
                        cellDetails[i + 1][j - 1].h = hNew
                        cellDetails[i + 1][j - 1].parent_i = i
                        cellDetails[i + 1][j - 1].parent_j = j
        if not foundDest:
            print("Failed to find the Destination Cell")
        return


    def _runAlgorithm(self):
        print("Runing...")
        self.matrix[self.start[0]][self.start[1]] = 1
        self.matrix[self.dest[0]][self.dest[1]] = 1
        print(self.start)
        print(self.dest)
        self._aStarSearch()




    def _paint(self, event):
        x,y = event.x,event.y
        xm = (x * 80)//800
        ym = (y * 80)//800
        x = xm * self.cellSize
        y = ym * self.cellSize
        if xm >= 0 and xm <= 79 and ym >= 0 and ym <= 79:

            x1, y1 = (x), (y)
            x2, y2 = (x + self.cellSize), (y + self.cellSize)
            color = self.map[self.cellKind]

            if self.cellKind == 2:
                if self.start[0] == -1 and self.start[1] == -1:
                    self.start = [ym, xm]
                    self.wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
                else:
                    self.wn.create_rectangle(self.start[1]*self.cellSize,self.start[0]*self.cellSize,self.start[1]*self.cellSize + self.cellSize,self.start[0]*self.cellSize + self.cellSize, fill="white", outline="white")
                    self.start = [ym, xm]
                    self.wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            elif self.cellKind == 3:
                if self.dest[0] == -1 and self.dest[1] == -1:
                    self.dest = [ym, xm]
                    self.wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
                else:
                    self.wn.create_rectangle(self.dest[1]*self.cellSize,self.dest[0]*self.cellSize,self.dest[1]*self.cellSize + self.cellSize,self.dest[0]*self.cellSize + self.cellSize, fill="white", outline="white")
                    self.dest = [ym, xm]
                    self.wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            else:
                self.matrix[ym][xm] = 0
                self.wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

            #self.wn.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

a = AStarSearchAlgorithm()