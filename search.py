def genericSearch(problem, frontier):
    
    node = getStartNode(problem)

    frontier.push(node)
    states_expanded = set()
    
    while not frontier.isEmpty():
        node = frontier.pop()
        
        if problem.isGoalState(node.state):
            return node.getActionPlan()
        
        if node.state not in states_expanded:
            states_expanded.add(node.state)
            
            for new_state, action, cost in problem.expand(node.state):
                child_node = node.getChildNode(new_state, action, cost)
                frontier.push(child_node)
    
    return []

def depthFirstSearch(problem):
    return genericSearch(problem, frontier=Stack())

def breadthFirstSearch(problem):
    return genericSearch(problem, frontier=Queue())
  
def aStarSearch(problem, heuristic):
    return genericSearch(problem, frontier=PriorityQueueWithFunction(heuristic))

def uniformCostSearch(problem):
    return genericSearch(problem, frontier=PriorityQueueWithFunction(nullHeuristic))

def nullHeuristic(problem, state):
  return 0

class SearchNode:
    def __init__(self, state, action=None, cost=0, parent=None):    
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent

    def getActionPlan(self):
        actionPlan = []
        node = self
        while node.parent is not None:
            actionPlan.append(node.action)
            node = node.parent
        return actionPlan[::-1]
    
    def getChildNode(self, new_state, action, cost):
        return SearchNode(
            state = new_state,
            action = action,
            cost = self.cost + cost,
            parent = self
        )

def getStartNode(problem: SearchProblem):
    return SearchNode(state=problem.getStartState(), action=None, cost=0,  parent=None)
