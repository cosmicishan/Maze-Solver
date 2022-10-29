# Maze-Solver
Finding the shortest path of the Maze

In this repository I have implemented an algorithm to solve the Maze.

**Method of Searching**

In a search process, data is often stored in a node which is a tuple which holds the position/location of the Maze which is in row and column form.

The code contains following Data:

An Agent object. Which consists two variable. 1. Node and 2. Parent.
The parent is object where the previous agent was generated.

Agent class contain information that makes it very useful for the purposes of search algorithms. It contain a node, which can be checked if it reaches the goal by storing of location of the goal('B') and compares it with the node to check if we reach the goal. If it reaches the goal then we look for the optimal solution. Once the goal is reached we find a path to where it's coming from by using method of recursion and keep going back to it's parent object and getting the node of the project. Through that we trace back every step of the way from the initial state to this node, and this sequence of actions is the optimal path.

For searching, we use the frontier, the mechanism that “manages” the nodes. The frontier starts by containing the starting point('A') and we keep adding new nodes to it until we find the solution.

**Psuedo-Code:**

Repeat:

If the frontier is empty,

Terminate the program and print that there's no Solution.

Remove a node from the frontier. This is the node that will be considered for the next exploration. 

If the node contains the goal.
Return the solution. Stop.

Else,

* Expand the node for the further exploration, and add new resulting nodes to the frontier.
* Add the current node to the explored set.

**Algorithm Used**

*1. Depth-First Search*
*2. Breadth-First Search*


***1. Depth-First Search***

The depth-first algorithm will follow multiple direction at same time. The data structure it uses for the frontier is *stack* To use this algorithm for the solution, you need to pass 'stack' when you define the class of Agent. The stack uses 'last-in last-out' method. Which exlpores all the steps in one direction ebfore it moves to others. Only after it reach the dead-end in one direction, it will move on to explore another direction. It will stop searching one direction and start searching elsewhere only once it's completely exhausted the search in every single neighbours in that position.

***2. Breadth-First Search***

The depth-first algorithm will follow multiple direction at same time. The data structure it uses for the frontier is *queue* To use this algorithm for the solution, you need to pass 'queue' when you define the class of Agent. After new observations are being added to the frontier, the first node will be removed and last one will be added and first node will be set to explore that direction. This results in algorithm that goes as deep as possible in the first direction that gets in its way while leaving all other directions for later. Only after it has exhausted all the locations it will go back to next direction and search in the next location.

**Maze_files**

*The Maze is in text filed:*

'A' - Starting Point.
'B' - The goal the algorithm have to reach.
'#' - Walls which the ALgorithm can't pas through. 

There are 3 Maze files and I have run the code to solve all 3 of those Maze file. The argument of the Agent class takes the location of Maze file and it will return the solution inside the Solution folder with the name of maze and the data structure it uses for the Frontier. 
