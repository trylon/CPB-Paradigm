from operator import *
from WorldModel import WorldModel

class EthicalAgent:
    def __init__(self,principal):
        self.world = WorldModel()
        self.principal = principal

    def isActionPreferable(self,action1tup, action2tup):
        action1 = action1tup[1]
        action2 = action2tup[1]
        #print action1
        #print action2
        PosCase = map(sub, action1, action2)
        NegCase = map(sub, action2, action1)
        actionPrincipal = self.principal
        if (any(map(lambda i: all(map(ge, PosCase, i)), actionPrincipal))
            and not any(map(lambda i: all(map(ge, NegCase, i)), actionPrincipal))):
                return -1
        elif (any(map(lambda i: all(map(ge, NegCase, i)), actionPrincipal))
            and not any(map(lambda i: all(map(ge, PosCase, i)), actionPrincipal))):
                return 1
        elif sum(action1) > sum(action2):
            return -1
        elif sum(action2) > sum(action1):
            return 1
        else:
            return 0


    def mySorted(self,actionList):
        return sorted(actionList.iteritems(), cmp=self.isActionPreferable)
    
    def findClause(self,action1,action2):
        result = map(operator.sub,action1,action2)
        for i,v in enumerate(self.principal):
            if all(x >= y for x, y in zip(result, v)):
                return i
        return -1 #none found
        
    def findCase(self,principleClause,actionPairs):
        for i,action in enumerate(actionPairs):
            result = map(operator.sub,action[0],action[1])
            if all(x >= y for x, y in zip(result,principleClause)):
                return i
        return -1 #none found
<<<<<<< HEAD
    
    def getPreferredAction(self,actionList):
      sorted = self.mySorted(actionList)
      bestActions = [] #GC warning spot
      i = 0
      while True: #emulate do-while http://stackoverflow.com/a/743944/1376005
        bestActions.append(sorted[i]) #add the action (do this before checking because you need at least one)
        if i < len(sorted) - 1 #if the length of the array has not been iterated
          and self.isActionPreferable(sorted[i],sorted[i+1]) == 0: #and the actions are equally preferable
            i = i + 1 #i++ and continue
        else:  #otherwise
          break #stop the loop
      return random.choice(bestActions) #pick randomly from the generated list http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python
=======
>>>>>>> b2cefd65fab30dddb8964c6e6a655ae86fc3fd43
