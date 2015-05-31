from WorldModel import WorldModel
class TextFileReader:
    def __init__(self,fileName):
        self.file = fileName
        self.textDescArray = []
        self.caseArray = []
        self.world = WorldModel()

    def readData(self):
        actionsArray = []
        textArray = []
        prevLine = ""
        with open(self.file) as test:
            for line in test:
                if "Description:" in line:
                    textArray.append(line[13:len(line)-1])
                if "Duties:" in line:
                    prevLine = prevLine.lower()
                    actionsArray.append(prevLine[1:len(prevLine)-1])
                prevLine = line
        self.textDescArray = textArray
        self.caseArray = self.createCaseArray(actionsArray)

    def createCaseArray(self,actionsArray):
        count = 0
        tempAction = ""
        caseArray = []
        world = self.world.getWorld()
        for action in actionsArray:
            if count==0:
                tempAction = action
                count+=1
            else:
                caseArray.append([world[tempAction],world[action]])
                count = 0
        return caseArray
