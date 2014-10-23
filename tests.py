from operator import *

c2a1 = [1,-1,-1,0,0]
c2a2 = [1,-1,1,0,0]
#False

c3a1 = [1,1,-1,0,0]
c3a2 = [1,-1,1,0,0]
#True

c4a1 = [0,0,-1,1,-1]
c4a2 = [0,0,1,-1,1]
#False

c5a1 = [-1,0,-1,0,2]
c5a2 = [-2,0,1,0,-2]
#True

c6a1 = [0,0,-1,2,0]
c6a2 = [0,0,1,-2,0]
#True

c7a1 = [0,0,-1,0,1]
c7a2 = [0,0,1,0,-1]
#True

c8a1 = [2, 2, 2]
c8a2 = [1, 1, 1]
principal89 = [[1,-4,-2], [-1,-3,-1],[-4,-4,3], [-4,3,-2]]
#True

c9a1 = [1,1,1]
c9a2 = [1,1,1]
#False
actionList = [c2a1,c2a2,c3a1,c3a2,c4a1,c4a2,c5a1,c5a2,c6a1,c6a2,c7a1,c7a2]


principal2 = [[-4,1,-2,-2,-4],[1,-2,-2,-2,-4],[-4,-2,-2,-2,1],[-4,-1,-1,-1,-1],[-4,-2,-2,1,-1]]


def isActionPreferred(action1, action2, principal):

    PosCase = map(sub, action1, action2)
    NegCase = map(sub, action2, action1)
    if (any(map(lambda i: all(map(ge, PosCase, i)), principal))
        and not any(map(lambda i: all(map(ge, NegCase, i)), principal))):
            return 1
    elif (any(map(lambda i: all(map(ge, NegCase, i)), principal))
        and not any(map(lambda i: all(map(ge, PosCase, i)), principal))):
            return -1
    elif sum(action1) > sum(action2):
        return 1
    elif sum(action2) > sum(action1):
        return -1
    else:
        return 0
        

'''
print isActionPreferred(action1, action2, principal) #False
print isActionPreferred(c2a1, c2a2, principal2)     #False
print isActionPreferred(c3a1, c3a2, principal2)     #True
print isActionPreferred(c4a1, c4a2, principal2)     #False
print isActionPreferred(c5a1, c5a2, principal2)     #True
print isActionPreferred(c6a1, c6a2, principal2)     #True
print isActionPreferred(c7a1, c7a2, principal2)     #True
print isActionPreferred(c8a1, c8a2, principal89)    #True   
print isActionPreferred(c9a1, c9a2, principal89)    #False
'''

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

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


global myPrincipal


def mySortedKey(actionList, principal):
    global myPrincipal
    myPrincipal = principal
    return sorted(actionList, key=cmp_to_key(isActionPreferrable))
"""
print ""
print "Sorting with CMP, parameters are global variables: actionList and principal2"
print "mySorted(actionList, principal2)"
print mySorted(actionList, principal2)
print ""
print "Sorting by key, parameters are same as above"
print "mySortedKey(actionList, principal2)"
print mySortedKey(actionList, principal2)
"""
