from operator import *

actions = {
    'remind':[1,-1],
    'charge':[-1,1]
}
principal = [[-1,-1] , [-2, 1]]


def isActionPreferrable(action1tup, action2tup):
    action1 = action1tup[1]
    action2 = action2tup[1]
    print action1
    print action2
    PosCase = map(sub, action1, action2)
    NegCase = map(sub, action2, action1)
    actionPrincipal = myPrincipal
    if (any(map(lambda i: all(map(ge, PosCase, i)), actionPrincipal))
        and not any(map(lambda i: all(map(ge, NegCase, i)), actionPrincipal))):
            return 1
    elif (any(map(lambda i: all(map(ge, NegCase, i)), actionPrincipal))
        and not any(map(lambda i: all(map(ge, PosCase, i)), actionPrincipal))):
            return -1
    elif sum(action1) > sum(action2):
        return 1
    elif sum(action2) > sum(action1):
        return -1
    else:
        return 0


def mySorted(actionList, principal):
    global myPrincipal
    myPrincipal = principal
    return sorted(actionList, cmp=isActionPreferrable)

print mySorted(actions.iteritems(),principal)