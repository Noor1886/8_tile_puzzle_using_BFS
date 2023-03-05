import numpy as np
import sys

# Creating a main class 
class PuzzleSolution():
  
    # Creating a puzzle solution class
    # Defining and declaring values in the function.
    # Specifying the target state and also the iterations along with the name of files to store data
    # Basically creating a map with node coordinates to define positions within a matrix.
    # Elements are meant to be read column wise.
    # init method for the class

    def __init__(self, maps):
        self.nodesFile = open("Nodes.txt", "w")
        self.nodePathFile = open("nodePath.txt", "w")
        self.nodesInfoFile = open("NodesInfo.txt", "w")
        self.maps = maps
        self.goalmaps = np.array([[1,2,3],[4,5,6],[7,8,0]])
        self.leftMove = 1
        self.upMove = 2
        self.rightMove = 3
        self.downMove = 4

    #  Results stored in nodes.txt

    def WriteToFile(self, array):
        data = ""
        for col in range(0, array.shape[1]):
            for row in range(0, array.shape[0]):
                data = data + str(array[row][col]) + " "
        data = data + "\n"
        self.nodesFile.write(data)

    # Nodes path in nodePath.txt

    def WriteToPathFile(self, array):
        data = ""
        for col in range(0, array.shape[1]):
            for row in range(0, array.shape[0]):
                data = data + str(array[row][col]) + " "
        data = data + "\n"
        self.nodePathFile.write(data)

    # Map to string conversion

    def mapsToString(self, array):
        data = str("")
        for col in range(0, array.shape[1]):
            for row in range(0, array.shape[0]):
                data = data + str(array[row][col]) + " "
        return data

    # blank Tile is denoted by 0

    def TileLocation(self):
        TileRow, TileCol = np.where(self.maps == 0)
        if (len(TileRow) > 0 and len(TileCol) > 0):
            return (TileRow[0], TileCol[0])
        else:
            return (-1, -1)

    # Condition for a step to take place or not

    def ValidMove(self, TileRow, TileCol, numRows, numCols):
        if ((TileRow >= 0 and TileRow < numRows) and (TileCol >= 0 and TileCol < numCols)):
            return True
        else:
            return False

    # Function for moving Tile to the left
    def ActionMoveLeft(self, TileRow, TileCol):
        newmaps = self.maps.copy()

        # moving left
        var = newmaps[TileRow][TileCol]
        newmaps[TileRow][TileCol] = newmaps[TileRow][TileCol - 1]
        newmaps[TileRow][TileCol - 1] = var
        return newmaps

    # Function for moving Tile to the right
    def ActionMoveRight(self, TileRow, TileCol):
        newmaps = self.maps.copy()

        # moving right
        var = newmaps[TileRow][TileCol]
        newmaps[TileRow][TileCol] = newmaps[TileRow][TileCol + 1]
        newmaps[TileRow][TileCol + 1] = var
        return newmaps

    # Function for moving Tile upwards

    def ActionMoveUp(self, TileRow, TileCol):
        newmaps = self.maps.copy()

        # moving up
        var = newmaps[TileRow][TileCol]
        newmaps[TileRow][TileCol] = newmaps[TileRow - 1][TileCol]
        newmaps[TileRow - 1][TileCol] = var
        return newmaps

    # Function for moving Tile downwards
    def ActionMoveDown(self, TileRow, TileCol):
        newmaps = self.maps.copy()

        # moving down
        var = newmaps[TileRow][TileCol]
        newmaps[TileRow][TileCol] = newmaps[TileRow + 1][TileCol]
        newmaps[TileRow + 1][TileCol] = var
        return newmaps

    # Checking target state function
    def CheckGoalState(self):
        return ((self.maps == self.goalmaps).all() and (self.maps.shape == self.goalmaps.shape))

    # comparing maps
    def Comparemaps(self, maps1, maps2):
        return ((maps1 == maps2).all() and (maps1.shape == maps2.shape))

    # update maps with values
    def Updatemaps(self, newmaps):
        self.maps = newmaps

    # Backtracking function to find the path to reach from target to initial
    def GeneratePath(self, Node_State_i, numberOfMoves, lastMove):
        finalmaps = []
        self.Updatemaps(self.goalmaps)
        finalmaps.append((self.goalmaps, -1))

        if (lastMove == self.leftMove):
            newmaps = self.ActionMoveRight(2, 2)
        elif (lastMove == self.upMove):
            newmaps = self.ActionMoveDown(2, 2)
        elif (lastMove == self.rightMove):
            newmaps = self.ActionMoveLeft(2, 2)
        else:
            newmaps = self.ActionMoveUp(2, 2)

        numberOfMoves = numberOfMoves - 1
        while (len(Node_State_i[numberOfMoves]) > 0):
            for index in range(0, len(Node_State_i[numberOfMoves])):
                if (self.Comparemaps(newmaps, Node_State_i[numberOfMoves][index][0])):
                    finalmaps.append((newmaps, lastMove))
                    self.Updatemaps(newmaps)
                    (currTileRow, currTileCol) = self.TileLocation()
                    lastMove = Node_State_i[numberOfMoves][index][1]

                    # updating newly created maps
                    if (lastMove == self.leftMove):
                        newmaps = self.ActionMoveRight(currTileRow, currTileCol)
                    elif (lastMove == self.upMove):
                        newmaps = self.ActionMoveDown(currTileRow, currTileCol)
                    elif (lastMove == self.rightMove):
                        newmaps = self.ActionMoveLeft(currTileRow, currTileCol)
                    else:
                        newmaps = self.ActionMoveUp(currTileRow, currTileCol)
                    numberOfMoves = numberOfMoves - 1
                    break

        # Reversing the map paths
        finalmaps = finalmaps[::-1]
        return finalmaps

    # BFS logic using the flow chart
    def solve(self):
        queue = []
        queue.append((self.maps, -1, 0, 0))
        visitedmaps = {}
        Node_State_i = {}
        moves = []
        prevLevel = -1
        lastMove = -1
        flag = -1
        startIndex = 1

        while (len(queue) > 0):
            (currmaps, prevMove, Node_Index_i, Parent_Node_Index_i) = queue[0]
            self.Updatemaps(currmaps)
            stringmaps = self.mapsToString(currmaps)
            queue.pop(0)

            # writing into nodesInfo.txt and nodes.txt
            data = "" + str(startIndex) + " " + str(Parent_Node_Index_i) + "\n"
            self.nodesInfoFile.write(data)
            self.WriteToFile(currmaps)

            # Defining a Maximum amount of steps
            if (Node_Index_i > 1000):
                lastMove = -1
                break

            # update Node_State_i
            if (prevLevel != Node_Index_i):
                Node_State_i[prevLevel] = moves
                moves = []
                moves.append((currmaps, prevMove))
                prevLevel = Node_Index_i
            else:
                moves.append((currmaps, prevMove))

            # Verify if goal state reached or not
            if (self.CheckGoalState()):
                flag = Node_Index_i
                lastMove = prevMove
                break

            # new nodes visited
            if (visitedmaps.get(str(stringmaps)) is None):
                # updating new values as visited
                visitedmaps[str(stringmaps)] = 1

                # Defining the tile location
                (currTileRow, currTileCol) = self.TileLocation()

                # moving left
                if (prevMove != self.rightMove and self.ValidMove(currTileRow, currTileCol - 1, 3, 3)):
                    leftMovemaps = self.ActionMoveLeft(currTileRow, currTileCol)

                    # check maps visited or not
                    if (visitedmaps.get(str(leftMovemaps)) is None):
                        visitedmaps[str(leftMovemaps)] = 1
                        queue.append((leftMovemaps, self.leftMove, Node_Index_i + 1, startIndex))

                # moving up
                if (prevMove != self.downMove and self.ValidMove(currTileRow - 1, currTileCol, 3, 3)):
                    upMovemaps = self.ActionMoveUp(currTileRow, currTileCol)

                    # check maps visited or not
                    if (visitedmaps.get(str(upMovemaps)) is None):
                        visitedmaps[str(upMovemaps)] = 1
                        queue.append((upMovemaps, self.upMove, Node_Index_i + 1, startIndex))

                # moving right
                if (prevMove != self.leftMove and self.ValidMove(currTileRow, currTileCol + 1, 3, 3)):
                    rightMovemaps = self.ActionMoveRight(currTileRow, currTileCol)

                    # check maps visited or not
                    if (visitedmaps.get(str(rightMovemaps)) is None):
                        visitedmaps[str(rightMovemaps)] = 1
                        queue.append((rightMovemaps, self.rightMove, Node_Index_i + 1, startIndex))

                # moving down
                if (prevMove != self.upMove and self.ValidMove(currTileRow + 1, currTileCol, 3, 3)):
                    downMovemaps = self.ActionMoveDown(currTileRow, currTileCol)

                    # check maps visited or not
                    if (visitedmaps.get(str(downMovemaps)) is None):
                        visitedmaps[str(downMovemaps)] = 1
                        queue.append((downMovemaps, self.downMove, Node_Index_i + 1, startIndex))
            startIndex = startIndex + 1

        # backtracking to find the solution
        numberOfMoves = flag
        lastMoveToReachGoal = lastMove
        if (flag == -1):
            self.nodesFile.close()
            self.nodePathFile.close()
            self.nodesInfoFile.close()
            return ([], -1)
        else:
            finalmaps = self.GeneratePath(Node_State_i, numberOfMoves, lastMove)

            # write to nodePath file
            for array in finalmaps:
                self.WriteToPathFile(array[0])

            self.nodesFile.close()
            self.nodePathFile.close()
            self.nodesInfoFile.close()
            return (finalmaps, numberOfMoves)


# taking Input
# where I define values to the input matrix you enter, reading the string entered to integer values
if (len(sys.argv) > 1 and len(sys.argv[1]) > 8):
    Matrix_pos = str(sys.argv[1])
    Matrix_stdx = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    Matrix_stdx[0][0] = int(Matrix_pos[0])
    Matrix_stdx[1][0] = int(Matrix_pos[1])
    Matrix_stdx[2][0] = int(Matrix_pos[2])
    Matrix_stdx[0][1] = int(Matrix_pos[3])
    Matrix_stdx[1][1] = int(Matrix_pos[4])
    Matrix_stdx[2][1] = int(Matrix_pos[5])
    Matrix_stdx[0][2] = int(Matrix_pos[6])
    Matrix_stdx[1][2] = int(Matrix_pos[7])
    Matrix_stdx[2][2] = int(Matrix_pos[8])

    # solving the problem
    puzzle = PuzzleSolution(Matrix_stdx)
    (array, moves) = puzzle.solve()
    if (moves > -1):
        print("Puzzle solved with moves: " + str(moves))
    else:
        print("Puzzle not solved!")
else:
    print("Enter test case")

