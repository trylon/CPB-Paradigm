class ActionPair:
    def __init__(self,case,textDesc):
        self.case = case #example: [[1,0,0,0],[-1,-1,0,0]]
        self.textDesc = textDesc #example: 'There are no reminders to give.'               

    @staticmethod
    def createActionPairs(caseArray,textArray):#assumes data is an ordered list
        actionPairs = []
        for case,text in zip(caseArray,textArray):
            actionPairs.append(ActionPair(case,text))
        return actionPairs
