# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
from decimal import Decimal

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """



    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        score = successorGameState.getScore()
        newWalls = successorGameState.getWalls()
        newCapsules = currentGameState.getCapsules()
        newNumFood = successorGameState.getNumFood()
        oldNumFood = currentGameState.getNumFood()
        """
        newFood[newPos[0]][newPos[1]] = "O"
        newWalls[newPos[0]][newPos[1]] = "O"
        print "~~~~~~~~~~~~~( '<) ~~~~~~~~~~~~~~~~~"
        print "newPos " + str(newPos)
        print "newFood:\n" + str(newFood)
        #print "newNumFood + " + str(newNumFood)
        print "newWalls: "
        print newWalls
        print "newGhostStates: "
        i=0
        for x in newGhostStates:
            print "at " + str(i) + " "+ str(x)
            i += 1
        print "newScaredTimes:"
        i = 0
        for x in newScaredTimes:
          print "at " + str(i) + " "+ str(x)
          i += 1

        print "score: " + str(score)
        """

        "*** YOUR CODE HERE ***"
        if successorGameState.isWin():
            return Decimal('Infinity')


        food = newFood.asList()
        #closestfood = 100
        foodDistances = []
        for x in food:
            foodDistances.append(util.manhattanDistance(x, newPos))
        sorted(foodDistances)
        ghosts = currentGameState.getGhostStates()
        ghostDistances = []
        for x in ghosts:
            ghostDistances.append(util.manhattanDistance(newPos, x.getPosition()))
        #distfromghost = util.manhattanDistance(ghostposition, newPos)
        #score = max(distfromghost, 6) + successorGameState.getScore()
        sorted(ghostDistances)
        
        for x in range(len(ghostDistances)):
            if newScaredTimes[x] >=4:
                score += ghostDistances[x] + 5
            else:
                score += ghostDistances[x]
            if ghostDistances[x] < 3 and newScaredTimes[x] == 0:
                score -= 25

        for x in range(len(ghostDistances)):
            if len(foodDistances) > x:
                if newScaredTimes[x] >=4:
                    score -= (foodDistances[x])+5
                else:
                    score -= (foodDistances[x])
        if (oldNumFood < newNumFood):
            score += 150
        if action == Directions.STOP:
            score -= 15
        if newPos in newCapsules:
            score += 75
        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        def minimin(gameState, agentIndex, depth):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            for_min = Decimal('Infinity')
            for_max = Decimal('-Infinity')
            pac = gameState.getLegalActions(0)
          
            #ghost = gameState.getLegalActions(agentIndex)
            if ((agentIndex)%(gameState.getNumAgents())) == 0:
                for x in pac:
                    for_max = max(for_max, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth))
                #print "2 max at depth " + str(depth) + " " + str(for_max)+ " agentIndex " + str(agentIndex) +" getNumAgents " + str(gameState.getNumAgents()) 
                return for_max
            else:

                if ((agentIndex+1)%(gameState.getNumAgents())) == 0:
                    #ghost = gameState.getLegalActions(agentIndex)
                    for x in gameState.getLegalActions(agentIndex%(gameState.getNumAgents())):
                        for_min = min(for_min, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth-1))
                    #print "1 min at depth " + str(depth) + " " + str(for_min) + " agentIndex " + str(agentIndex) + " getNumAgents " + str(gameState.getNumAgents()) 
                    return for_min 
                else:
                    #ghost = gameState.getLegalActions(agentIndex)
                    for x in gameState.getLegalActions(agentIndex%(gameState.getNumAgents())):
                        for_min = min(for_min, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth))
                    #print "1 min at depth " + str(depth) + " " + str(for_min) + " agentIndex " + str(agentIndex) + " getNumAgents " + str(gameState.getNumAgents()) 
                    return for_min     
            """
            if (agentIndex%(gameState.getNumAgents()+1)) == 0:
                for x in pac:
                    for_min = min(for_min, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()+1), x), agentIndex+1, depth))
                print "0 min at depth " + str(depth) + " " + str(for_max)
                return for_min
            else:
                if ((agentIndex+1)%(gameState.getNumAgents()+1)) != 0:
                    for x in ghost:
                        for_min = min(for_min, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()+1), x), agentIndex+1, depth))
                    print "1 min at depth " + str(depth) + " " + str(for_min) + " agentIndex " + str(agentIndex) + " getNumAgents " + str(gameState.getNumAgents()) 
                    return for_min
                else:
                    for x in ghost:
                        for_max = max(for_max, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()+1), x), agentIndex+1, depth-1))
                    print "2 max at depth " + str(depth) + " " + str(for_max)+ " agentIndex " + str(agentIndex) +" getNumAgents " + str(gameState.getNumAgents()) 
                    return for_max
            """


        #print "depth: " + str(self.depth)
        #print "numagents: " + str(gameState.getNumAgents())
        the_pac_man = gameState.getLegalActions(0)
        default_move = Directions.STOP
        minimax = Decimal('-Infinity')
        for x in the_pac_man:
            moves = gameState.generateSuccessor(0, x)
            old_minimax = minimax
            #depth = ((gameState.getNumAgents()) * self.depth)
            minimax = max(minimax, minimin(moves, 1, self.depth))
            if old_minimax < minimax:
                default_move= x
                old_minimax = minimax
        return default_move

        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def minimin(gameState, agentIndex, depth, alpha, beta):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            for_min = Decimal('Infinity')
            for_max = Decimal('-Infinity')
            pac = gameState.getLegalActions(0)
          
            #ghost = gameState.getLegalActions(agentIndex)
            if ((agentIndex)%(gameState.getNumAgents())) == 0:
                for x in pac:
                    for_max = max(for_max, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth, alpha, beta))
                    if for_max > beta:
                        return for_max
                    alpha = max(alpha, for_max)
                #print "2 max at depth " + str(depth) + " " + str(for_max)+ " agentIndex " + str(agentIndex) +" getNumAgents " + str(gameState.getNumAgents()) 
                return for_max
            else:
                if ((agentIndex+1)%(gameState.getNumAgents())) == 0:
                    for x in gameState.getLegalActions(agentIndex%(gameState.getNumAgents())):
                        for_min = min(for_min, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth-1, alpha, beta))
                        if for_min < alpha:
                          return for_min
                        beta = min(beta, for_min)
                    #print "1 min at depth " + str(depth) + " " + str(for_min) + " agentIndex " + str(agentIndex) + " getNumAgents " + str(gameState.getNumAgents()) 
                    return for_min 
                else:
                    #ghost = gameState.getLegalActions(agentIndex)
                    for x in gameState.getLegalActions(agentIndex%(gameState.getNumAgents())):
                        for_min = min(for_min, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth, alpha, beta))
                        if for_min < alpha:
                          return for_min
                        beta = min(beta, for_min)
                    #print "1 min at depth " + str(depth) + " " + str(for_min) + " agentIndex " + str(agentIndex) + " getNumAgents " + str(gameState.getNumAgents()) 
                    return for_min     


        #print "depth: " + str(self.depth)
        #print "numagents: " + str(gameState.getNumAgents())
        the_pac_man = gameState.getLegalActions(0)
        default_move = Directions.STOP
        minimax = Decimal('-Infinity')
        alpha = Decimal('-Infinity')
        beta = Decimal('Infinity')
        for x in the_pac_man:
            moves = gameState.generateSuccessor(0, x)
            old_minimax = minimax
            #depth = ((gameState.getNumAgents()) * self.depth)
            minimax = max(minimax, minimin(moves, 1, self.depth, alpha, beta))
            if old_minimax < minimax:
                default_move= x
                old_minimax = minimax
            if minimax >= beta:
              return default_move
            alpha = max(minimax, alpha)
        return default_move

        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def minimin(gameState, agentIndex, depth):
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)
            for_expecti = 0.0
            for_max = float('-inf')
            pac = gameState.getLegalActions(0)
          
            #ghost = gameState.getLegalActions(agentIndex)
            if ((agentIndex)%(gameState.getNumAgents())) == 0:
                for x in pac:
                    for_max = max(for_max, minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth))
                #print "2 max at depth " + str(depth) + " " + str(for_max)+ " agentIndex " + str(agentIndex) +" getNumAgents " + str(gameState.getNumAgents()) 
                return for_max
            else:
                if ((agentIndex+1)%(gameState.getNumAgents())) == 0:
                    #ghost = gameState.getLegalActions(agentIndex)
                    for x in gameState.getLegalActions(agentIndex%(gameState.getNumAgents())):
                        for_expecti += float(minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth-1))
                    #print "1 min at depth " + str(depth) + " " + str(for_expecti) + " agentIndex " + str(agentIndex) + " getNumAgents " + str(gameState.getNumAgents()) 
                    return float(for_expecti/ len(gameState.getLegalActions(agentIndex%(gameState.getNumAgents()))))
                else:
                    #ghost = gameState.getLegalActions(agentIndex)
                    for x in gameState.getLegalActions(agentIndex%(gameState.getNumAgents())):
                        for_expecti += float(minimin(gameState.generateSuccessor(agentIndex%(gameState.getNumAgents()), x), agentIndex+1, depth))
                    #print "1 min at depth " + str(depth) + " " + str(for_expecti) + " agentIndex " + str(agentIndex) + " getNumAgents " + str(gameState.getNumAgents()) 
                    return float(for_expecti / len(gameState.getLegalActions(agentIndex%(gameState.getNumAgents()))))   

        #print "depth: " + str(self.depth)
        #print "numagents: " + str(gameState.getNumAgents())
        the_pac_man = gameState.getLegalActions(0)
        default_move = Directions.STOP
        minimax = float('-inf')
        for x in the_pac_man:
            moves = gameState.generateSuccessor(0, x)
            old_minimax = minimax
            #depth = ((gameState.getNumAgents()) * self.depth)
            minimax = max(minimax, minimin(moves, 1, self.depth))
            if old_minimax < minimax:
                default_move= x
                old_minimax = minimax
        return default_move
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    def check_chokepoint(newWalls, initialPos, currPos):
       # xSize = len(newWalls[0])
        #ySize = len(newWalls)
        escapeCount = 0

        #check the possible moves to see if there is an escape route
        #check right
        #if currPos[0] < ySize:
        if newWalls[currPos[0]+1][currPos[1]]:
            escapeCount += 1
        #check down
        #if currPos[1] < xSize:
        if newWalls[currPos[0]][currPos[1]+1]:
            escapeCount += 1
        #check left
        #if currPos[0] > 0:
        if newWalls[currPos[0]-1][currPos[1]]:
            escapeCount +=1 
        #check up
        #if currPos[1] > 0:
        if newWalls[currPos[0]][currPos[1]-1]:
            escapeCount +=1
        return escapeCount




    if currentGameState.isWin():
        return Decimal('Infinity')
    if currentGameState.isLose():
        return -Decimal('Infinity')
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newNumFood = currentGameState.getNumFood()
    newCapsules = currentGameState.getCapsules()
    newWalls = currentGameState.getWalls()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    score = scoreEvaluationFunction(currentGameState)
    """
    print "~~~~~~~~~~~~~( '<) ~~~~~~~~~~~~~~~~~"
    print "pre score: " + str(score)
    print "newPos " + str(newPos)
    print "newFood:\n" + str(newFood)
    print "newNumFood + " + str(newNumFood)
    print "newWalls: "
    print newWalls
    print "newGhostStates: "
    i=0
    for x in newGhostStates:
        print "at " + str(i) + " "+ str(x)
        i += 1
    print "newScaredTimes:"
    i = 0
    for x in newScaredTimes:
      print "at " + str(i) + " "+ str(x)
      i += 1
    """

    #"*** YOUR CODE HERE ***"
    #escapeChance = check_chokepoint(newWalls, newPos,newPos)*25
    #hasFood = currentGameState(newPos[0][1])

    food = newFood.asList()
    #closestfood = 100
    foodDistances = []
    for x in food:
        foodDistances.append(util.manhattanDistance(x, newPos))
    sorted(foodDistances)
    ghosts = currentGameState.getGhostStates()
    ghostDistances = []
    for x in ghosts:
        ghostDistances.append(util.manhattanDistance(newPos, x.getPosition()))
        #distfromghost = util.manhattanDistance(ghostposition, newPos)
        #score = max(distfromghost, 6) + successorGameState.getScore()
    sorted(ghostDistances)
    if newPos in newCapsules:
        score += 75
    
    for x in range(len(ghostDistances)):
        if False:
            score += (ghostDistances[x])*3
        else:
            if ghostDistances[x] < 4:
                score += ghostDistances[x]
            #else:
                #score += abs(ghostDistances[x])*2
        #if ghostDistances[x] < 3 and newScaredTimes[x] == 0:
        #    score -= 25
    foodPos = newFood.asList()
    for x in range(len(ghostDistances)):
        if len(foodDistances) > x:
            #print "is this working?"
            if False:
                score -= (foodDistances[x])*100
            else:
                """
                if len(foodPos) <= 4:
                    tot = 0
                    for x in foodDistances:
                        tot += x

                    score -= (tot/len(foodPos))*1.5

                else:
                    if ghostDistances[x] < 2:
                        score -= foodDistances[x]*2
                    else:
                      """
                if ghostDistances[x] < 2:
                    score -= foodDistances[x]*5
                else:
                    score -= foodDistances[x]

    capsulelocations = currentGameState.getCapsules()
    score -=  len(foodPos) * 4

    score -= len(capsulelocations)



    #print "post score: " + str(score)
    return score
# Abbreviation
better = betterEvaluationFunction

