
# Solving 8 Puzzle problem using BFS

For a given state consisting of a 3x3 matrix with 9 elements, we find the optimal path to the node using BFS algorithm which explores the neighbouring nodes and also their children.

The data to be fed in the matrix is supposed to be a column wise addition,
so for example we have the goal matrix is [[1,4,7 ],[2,5,8],[3,6,0]]
It is to written as [[1,2,3], [4,5,6], [7,8,6]] i.e the rows become coumns.

![Screenshot from 2023-03-05 01-32-33](https://user-images.githubusercontent.com/102131442/222945730-69e4e6a2-2b86-495b-bee0-8e7f9bdc461e.png)



## How to run the code:

To execute the code;

When you the run the program it prompts you to enter the initial state,

In my environment I used the following execution to obtain the output.

python3 8_puzzle.py 470128356

python3 directory of the saved code (Initial test case)

You can modify the specified goal state in the code to the desired value


## Understanding the Output
Your Output should generate 3 files which are:

![Screenshot from 2023-03-05 01-34-51](https://user-images.githubusercontent.com/102131442/222945687-67804168-c4ab-4291-bfcd-69067ae537f2.png)



