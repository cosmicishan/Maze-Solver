class Agent():

    def __init__(self, node, parent):

        self.node = node
        self.parent = parent


class Stack():

    def __init__(self):
        self.frontier = []
        self.explored = []

    def contains_state(self, state):
        return any(n.node == state for n in self.frontier)

    def add(self, child):

            self.frontier.append(child)

    def remove(self):

        node = self.frontier[-1]
        self.frontier = self.frontier[:-1:]
        return node


class Queue(Stack):

    def remove(self):

        node = self.frontier[0]
        self.frontier = self.frontier[1::]
        return node

class Maze():

    def __init__(self, maze, algo, show_explored = False):

        self.show_explored = show_explored

        self.algo = algo

        self.filename = maze

        with open(self.filename) as f:
            self.maze = f.read().splitlines()

        self.height = len(self.maze)
        self.width = len(max([x for x in self.maze]))

        self.walls = []

        for i in range(self.height):

            for j in range(self.width):

                if self.maze[i][j] == 'A':

                    self.start = (i, j)

                if self.maze[i][j] == 'B':
                    self.goal = (i, j)

    def action(self, position):

        action_dict = {'up': (position[0]-1, position[1]),
                       'down': (position[0]+1, position[1]),
                       'left': (position[0], position[1]-1),
                       'right': (position[0], position[1]+1)}

        possible_actions = []

        for actions in action_dict:

            r = action_dict[actions][0]
            c = action_dict[actions][1]

            if r >= 0 and r < self.height and c >= 0 and c < self.width:

                if self.maze[r][c] != '#':

                    possible_actions.append((r, c))

        return possible_actions

    def solve(self):

        if self.algo == 'stack':

            solver = Stack()

        if self.algo == 'queue':

            solver = Queue()

        agent = Agent(node=self.start, parent=None)

        solver.add(agent)

        self.explored = set()

        while (True):

            child = solver.remove()

            if child.node == self.goal:

                path = []

                while child.parent is not None:

                    path.append(child.node)
                    child = child.parent

                if self.show_explored == True:

                    for i in self.explored:

                        if i == self.start or i == self.goal:

                            continue

                        self.maze[i[0]] = self.maze[i[0]][:i[1]] + '-' + self.maze[i[0]][i[1] + 1:]

                for i in path:

                    if i == self.start or i == self.goal:

                        continue

                    self.maze[i[0]] = self.maze[i[0]][:i[1]] + '*' + self.maze[i[0]][i[1] + 1:]

                n_names = ["{}\n".format(i) for i in self.maze]
                with open('Solution/' + self.filename + '_{}_solution'.format(self.algo), 'w') as fp:
                    fp.writelines(n_names)
                break

            self.explored.add(child.node)

            neighbours = self.action(child.node)

            for i in neighbours:

                if not solver.contains_state(i) and i not in self.explored:

                    child_node = Agent(node=i, parent=child)
                    solver.add(child_node)

            if len(solver.frontier) == 0:

                print("No solution")
                break

algo = Maze(maze='maze3', algo = 'queue')
algo.solve()
