import re
from WorldModel import WorldModel
class TextFileReader:
    def __init__(self,fileName):
        self.file = fileName
        self.textDescArray = []
        self.caseArray = []
        self.dutyNames = []
        self.dutyMinimums =[]
        self.principle = []
        #self.world = WorldModel()#is this even needed?

    def readData(self):
        actionsArray = []
        dutiesProfile = ""
        correctAction = ""
        prevLine = ""
        isDuty = False
        with open(self.file) as test:
            for line in test:  # iterate over every line
                if "Description:" in line:  # textual description
                    self.textDescArray.append(line[13:len(line)-1])
                elif "Duties:" in line:
                    if correctAction in prevLine:  # puts action name in front of preferred action
                        actionsArray.append(correctAction)
                    isDuty = True
                elif isDuty:  # creates a list of all the numbers corresponding to a duty
                    if(bool(re.match('.*\d',line))):  # if there is a number
                        dutiesProfile += line
                    else:
                        actionsArray.append(map(int,re.findall('\-?\d+',dutiesProfile)))  # creates a list of each actions profile
                        dutiesProfile = ""
                        isDuty = False
                elif "Correct Action:" in line:  # tells you which action goes first in the pair
                    correctAction = line[16:len(line)-1]
                elif "range:" in line:  # line hold the duty names and minimums
                    temp = map(int,re.findall('\-?\d+',line[8:]))
                    self.dutyMinimums.append(temp[0]-temp[1])
                    self.dutyNames.append(line[8:line.find('[')-2].lower())
                elif "((" in line:  # lines hold the principle
                    for textPrinciple in line.split(")) "):
                        self.principle.append(map(int,re.findall(' \-?\d+',textPrinciple)))
                prevLine = line
        self.caseArray = self.createCaseArray(actionsArray)

    def createCaseArray(self,actionsArray):#formats the caseArray so that preferred action goes first
        count = 0
        caseArray = []
        for index,action in enumerate(actionsArray):
            if count==0 and type(action) is str:
                caseArray.append([actionsArray[index+1],actionsArray[index+2]])
            elif count==1 and type(action) is str:
                caseArray.append([actionsArray[index+1],actionsArray[index-1]])
            count+=1
            if count==3:
                count=0
        return caseArray